import collections
import numpy as np
import tensorflow as tf

class AncientNN(object):
	"""docstring for AncientNN"""
	def __init__(self):
		super(AncientNN, self).__init__()
		self._dataSouce = []
		self._batch_size = 64


	def loadTrainSet(self,filename):
		with open(filename, "r") as f:
			for line in f:
				try:
					title, content = line.strip().split(':')
					content = content.replace(' ','')


					if '_' in content or '(' in content or '(' in content or '<<' in content or '[' in content:
						continue
					if len(content) < 5 or len(content) > 79:
						continue
					content = '[' + content + ']'


					self._dataSouce.append(content)
				except Exception as e: 
					pass
		#data order
		self._dataSouce = sorted(self._dataSouce,key=lambda line: len(line))

	def _dataClean(self,line):
		title, content = line.strip().split(':')
		content = content.replace(' ','')

		hasData = True

		if '_' in content or '(' in content or '(' in content or '<<' in content or '[' in content:
			hasData = False
		if len(content) < 5 or len(content) > 79:
			hasData = False

		content = '[' + content + ']'
		return (hasData,content)

	def getCommonWords(self):
		#statistics every word 
		all_words = []
		for itme in self._dataSouce:
			all_words += [word for word in itme]


		counter = collections.Counter(all_words)
		count_pairs = sorted(counter.items(), key=lambda x: -x[1])
		words, _ = zip(*count_pairs)
		 
		#get common words
		self._words = words[:len(words)] + (' ',)

		#mapping word in id
		self._word_num_map = dict(zip(self._words, range(len(self._words))))

		#translate to vector
		to_num = lambda word: self._word_num_map.get(word, len(self._words))
		self._data_vector = [ list(map(to_num, itme)) for itme in itme]
		#[[314, 3199, 367, 1556, 26, 179, 680, 0, 3199, 41, 506, 40, 151, 4, 98, 1],
		#[339, 3, 133, 31, 302, 653, 512, 0, 37, 148, 294, 25, 54, 833, 3, 1, 965, 1315, 377, 1700, 562, 21, 37, 0, 2, 1253, 21, 36, 264, 877, 809, 1]
		#....]

	def _translate2batchData(self):
		self.getCommonWords()

		self._n_chunk = len(self._data_vector) // self._batch_size
		self._x_batches = []
		self._y_batches = []

		for i in range(self._n_chunk):
			start_index = i * self._batch_size
			end_index = start_index + self._batch_size
		 
			batches = self._data_vector[start_index:end_index]
			length = max(map(len,batches))
			xdata = np.full((self._batch_size,length), self._word_num_map[' '], np.int32)
			for row in range(self._batch_size):
				xdata[row,:len(batches[row])] = batches[row]
			ydata = np.copy(xdata)
			ydata[:,:-1] = xdata[:,1:]
			"""
			xdata             ydata
			[6,2,4,6,9]       [2,4,6,9,9]
			[1,4,2,8,5]       [4,2,8,5,5]
			"""
			self._x_batches.append(xdata)
			self._y_batches.append(ydata)

	def _buildArchitecture(self,model='lstm',rnn_size=128, num_layers=2):
		self._translate2batchData()

		self._input_data = tf.placeholder(tf.int32, [self._batch_size, None])
		self._output_targets = tf.placeholder(tf.int32, [self._batch_size, None])

		if model == 'rnn':
			cell_fun = tf.nn.rnn_cell.BasicRNNCell
		elif model == 'gru':
			cell_fun = tf.nn.rnn_cell.GRUCell
		elif model == 'lstm':
			cell_fun = tf.nn.rnn_cell.BasicLSTMCell

		cell = cell_fun(rnn_size, state_is_tuple=True)
		cell = tf.nn.rnn_cell.MultiRNNCell([cell] * num_layers, state_is_tuple=True)
	 
		initial_state = cell.zero_state(self._batch_size, tf.float32)
	 
		with tf.variable_scope('rnnlm'):
			softmax_w = tf.get_variable("softmax_w", [rnn_size, len(self._words)+1])
			softmax_b = tf.get_variable("softmax_b", [len(self._words)+1])
			with tf.device("/cpu:0"):
				embedding = tf.get_variable("embedding", [len(self._words)+1, rnn_size])
				inputs = tf.nn.embedding_lookup(embedding, self._input_data)
	 
		outputs, last_state = tf.nn.dynamic_rnn(cell, inputs, initial_state=initial_state, scope='rnnlm')
		output = tf.reshape(outputs,[-1, rnn_size])
	 
		logits = tf.matmul(output, softmax_w) + softmax_b
		probs = tf.nn.softmax(logits)
		return logits, last_state, probs, cell, initial_state
	
	def train_neural_network(self):
		
	

		logits, last_state, _, _, _ = self._buildArchitecture()
		targets = tf.reshape(self._output_targets, [-1])
		loss = tf.contrib.legacy_seq2seq.sequence_loss_by_example([logits], [targets], [tf.ones_like(targets, dtype=tf.float32)], len(self._words))
		cost = tf.reduce_mean(loss)
		learning_rate = tf.Variable(0.1, trainable=False)
		tvars = tf.trainable_variables()
		grads, _ = tf.clip_by_global_norm(tf.gradients(cost, tvars), 5)
		optimizer = tf.train.AdamOptimizer(learning_rate)
		train_op = optimizer.apply_gradients(zip(grads, tvars))
	 
		with tf.Session() as sess:
			sess.run(tf.global_variables_initializer())
	 
			saver = tf.train.Saver(tf.global_variables())
	 
			for epoch in range(50):
			#train_loss = 100
			#epoch = 1
			#while train_loss > 1 and epoch < 500:
				sess.run(tf.assign(learning_rate, 0.002 * (0.97 ** epoch)))
				n = 0
				for batche in range(self._n_chunk):
					train_loss, _ , _ = sess.run([cost, last_state, train_op], feed_dict={self._input_data: self._x_batches[n], self._output_targets: self._y_batches[n]})
					n += 1
					print(epoch, batche, train_loss)
				if epoch % 7 == 0:
					saver.save(sess, './models/poetry.module', global_step=epoch)
				epoch = epoch + 1



	def SaveModel(model_name,global_step):
		self._saver = tf.train.Saver()
		saver.save(sess, model_name, global_step=epoch)

	def to_word(self,weights):
		t = np.cumsum(weights)
		s = np.sum(weights)
		sample = int(np.searchsorted(t, np.random.rand(1)*s))
		return words[sample]

	def inference(self):
		_, last_state, probs, cell, initial_state = self._buildArchitecture()
		with tf.Session() as sess:
			sess.run(tf.global_variables_initializer())
	 
			saver = tf.train.Saver(tf.global_variables())
			saver.restore(sess, './models/poetry.module-49')
	 
			state_ = sess.run(cell.zero_state(1, tf.float32))
	 
			x = np.array([list(map(self._word_num_map.get, '['))])
			print x
			[probs_, state_] = sess.run([probs, last_state], feed_dict={self._input_data: x, initial_state: state_})
			word = self.to_word(probs_)
			#word = words[np.argmax(probs_)]
			poem = ''
			while word != ']':
				poem += word
				x = np.zeros((1,1))
				x[0,0] = self._word_num_map[word]
				[probs_, state_] = sess.run([probs, last_state], feed_dict={self._input_data: x, initial_state: state_})
				word = self.to_word(probs_)
				#word = words[np.argmax(probs_]
		return poem
def main():
	model = AncientNN()
	model.loadTrainSet(filename='poetry.txt')
	#model.train_neural_network()

	print model.inference()
	pass

if __name__ == '__main__':
	main()