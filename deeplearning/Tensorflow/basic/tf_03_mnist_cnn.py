import tensorflow as tf
from tensorflow.examples.tutorials.mnist import input_data

def weight_varible(shape):
    initial = tf.truncated_normal(shape, stddev=0.1)
    return tf.Variable(initial)

def bias_variable(shape):
    initial = tf.constant(0.1, shape=shape)
    return tf.Variable(initial)

def conv2d(x, W):
    return tf.nn.conv2d(x, W, strides=[1, 1, 1, 1], padding='SAME')

def max_pool_2x2(x):
    return tf.nn.max_pool(x, ksize=[1, 2, 2, 1], strides=[1, 2, 2, 1], padding='SAME')


mnist = input_data.read_data_sets("MNIST_data/", one_hot=True)
print("Download Done!")

class MNIST_NN(object):
    """docstring for MNIST_NN"""
    def __init__(self):
        super(MNIST_NN, self).__init__()
        self._baseModelPath = "./tmp/model.ckpt"
        self._sess = tf.InteractiveSession()


    def buildArchitecture(self):
        # paras
        self._W_conv1 = weight_varible([5, 5, 1, 32])
        self._b_conv1 = bias_variable([32])

        # conv layer-1
        self._x = tf.placeholder(tf.float32, [None, 784])
        self._x_image = tf.reshape(self._x, [-1, 28, 28, 1])

        self._h_conv1 = tf.nn.relu(conv2d(self._x_image, self._W_conv1) + self._b_conv1)
        self._h_pool1 = max_pool_2x2(self._h_conv1)

        # conv layer-2
        self._W_conv2 = weight_varible([5, 5, 32, 64])
        self._b_conv2 = bias_variable([64])

        self._h_conv2 = tf.nn.relu(conv2d(self._h_pool1, self._W_conv2) + self._b_conv2)
        self._h_pool2 = max_pool_2x2(self._h_conv2)

        # full connection
        self._W_fc1 = weight_varible([7 * 7 * 64, 1024])
        self._b_fc1 = bias_variable([1024])

        self._h_pool2_flat = tf.reshape(self._h_pool2 , [-1, 7 * 7 * 64])
        self._h_fc1 = tf.nn.relu(tf.matmul(self._h_pool2_flat, self._W_fc1) + self._b_fc1)

        # dropout
        self._keep_prob = tf.placeholder(tf.float32)
        self._h_fc1_drop = tf.nn.dropout(self._h_fc1, self._keep_prob)

        # output layer: softmax
        self._W_fc2 = weight_varible([1024, 10])
        self._b_fc2 = bias_variable([10])

        self._y_conv = tf.nn.softmax(tf.matmul(self._h_fc1_drop, self._W_fc2) + self._b_fc2)
        self._y_ = tf.placeholder(tf.float32, [None, 10])

        self._definelose()

    def _definelose(self):
        # model training
        cross_entropy = -tf.reduce_sum(self._y_ * tf.log(self._y_conv))
        self._train_step = tf.train.AdamOptimizer(1e-4).minimize(cross_entropy)

        correct_prediction = tf.equal(tf.arg_max(self._y_conv, 1), tf.arg_max(self._y_, 1))
        self._accuracy = tf.reduce_mean(tf.cast(correct_prediction, tf.float32))
        

    def train(self):
        self._sess.run(tf.global_variables_initializer())

        for i in range(100):
            batch = mnist.train.next_batch(50)

            if i % 100 == 0:
                train_accuacy = self._accuracy.eval(feed_dict={self._x: batch[0], self._y_: batch[1], self._keep_prob: 1.0})
                print("step %d, training accuracy %g"%(i, train_accuacy))
            self._train_step.run(feed_dict = {self._x: batch[0], self._y_: batch[1], self._keep_prob: 0.5})

    def valid(self):
        for i in range(10):
            batch = mnist.train.next_batch(50)
            print("test accuracy %g"%self._accuracy.eval(feed_dict={self._x: batch[0], self._y_: batch[1], self._keep_prob: 1.0}))

    def realse(self):
        self._sess.close()

    def restore(self):
        saver = tf.train.Saver()
        saver.restore(self._sess, self._baseModelPath)
        print "Model restore in file: ", self._baseModelPath
        pass

    def saveModel(self):
        saver = tf.train.Saver()
        save_path = saver.save(self._sess, self._baseModelPath)
        print "Model restored from ", save_path

    def inference(self,y):
        pass

def main():
    #buidNN()
    nn = MNIST_NN()
    nn.buildArchitecture()
    nn.restore()
    #nn.train()
    nn.valid()
    nn.saveModel()
    nn.realse()

if __name__ == '__main__':
    main()