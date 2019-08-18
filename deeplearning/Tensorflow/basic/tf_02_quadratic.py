import tensorflow as tf
import numpy as np
import matplotlib.pyplot as plt

#define ayer
def add_layer(inputs, in_size, out_size, activation_function=None):
    Weights = tf.Variable(tf.random_normal([in_size, out_size]))
    biases = tf.Variable(tf.zeros([1, out_size]) + 0.1)
    Wx_plus_b = tf.matmul(inputs, Weights) + biases   

    #free to choose activity founction
    if activation_function is None:
        outputs = Wx_plus_b
    else:
        outputs = activation_function(Wx_plus_b)
        
    return outputs


def buildNN():
    xs = tf.placeholder(tf.float32, [None, 1])
    ys = tf.placeholder(tf.float32, [None, 1])

    #config and build nn
    # add hidden layer
    l1 = add_layer(xs, 1, 10, activation_function=tf.nn.relu)
    # add output layer
    prediction = add_layer(l1, 10, 1, activation_function=None)

    # set loss founction
    loss = tf.reduce_mean(tf.reduce_sum(tf.square(ys - prediction),reduction_indices=[1]))
    train_step = tf.train.GradientDescentOptimizer(0.1).minimize(loss)

    return (train_step,xs,ys,prediction)

def buildPlot(x_data,y_data):
    fig = plt.figure()
    ax = fig.add_subplot(1,1,1)
    ax.scatter(x_data, y_data)
    plt.ion()
    plt.show()

    return (fig,ax)

def main():

    #make some data and noise
    x_data = np.linspace(-1,1,300)[:, np.newaxis]
    noise = np.random.normal(0, 0.05, x_data.shape)
    y_data = np.square(x_data) - 0.5 + noise

    (fig,ax) = buildPlot(x_data,y_data)
    (train_step,xs,ys,prediction) = buildNN()

    
    sess = tf.Session()
    init = tf.global_variables_initializer()
    sess.run(init)

    for i in range(10000):

        sess.run(train_step, feed_dict={xs: x_data, ys: y_data})

        # plot current model prediction
        if i % 50 == 0:
            try:
                ax.lines.remove(lines[0])
            except Exception:
                pass
            
            prediction_value = sess.run(prediction, feed_dict={xs: x_data})
            lines = ax.plot(x_data, prediction_value, 'r-', lw=5)
            plt.pause(0.1)

    sess.close()

if __name__ == '__main__':
    main()
