#-*- coding: utf-8 -*-　
#引用必要函數
import tensorflow as tf
import numpy as np


def getTrain_X():
	# creat data
	#創造 亂數100個亂數 值介於0~1之間
	x_data = np.random.rand(100).astype(np.float32)
	return  x_data

def getTrain_Y(x_data):
	#訂出要學習的函數  這裡要學的是 weight:0.1  biases:0.3
	y_data = x_data*0.1+0.3
	return y_data

def build_NN(train_x,train_y):
	###creat tensorflow structure start###
	#定立 weights 的 範圍 和初始化
	Weights = tf.Variable(tf.random_uniform([1],-1.0,1.0))
	biases = tf.Variable(tf.zeros([1]))

	#定立 給 tensorflow 學習的函數
	y = Weights * train_x + biases

	#建立 loss 規則
	loss = tf.reduce_mean(tf.square(y-train_y))

	#選擇學習機制
	optimizer = tf.train.GradientDescentOptimizer(0.5)  #learning rate

	#像tensorflow 說 訓練規則就是把 loss 減到最小 最好是0
	train = optimizer.minimize(loss)

	return (train,Weights,biases)

def main():
	x_data = getTrain_X()
	y_data = getTrain_Y(x_data)
	(train,Weights,biases) = build_NN(x_data,y_data)

	sess = tf.Session()
	sess.run(tf.initialize_all_variables())     #Very important

	"""
	跑 for 迴圈 更新wight201次
	然後每訓練20次 印出一次 Weight
	"""
	for step in range(501):
	    sess.run(train)
	    if step % 20 ==0:
	        print(step,sess.run(Weights),sess.run(biases))

if __name__ == '__main__':
	main()