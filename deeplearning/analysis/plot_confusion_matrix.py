# -*- coding: UTF-8 -*-

from sklearn.metrics import classification_report

import itertools
import matplotlib.pyplot as plt
from sklearn.metrics import confusion_matrix
import numpy as np
 

 

#將繪制圖表的部份程式碼整理程一個函式，方便調用：
def plot_confusion_matrix(cm, classes,
                          normalize=False,
                          title='Confusion matrix',
                          cmap=plt.cm.Blues):
    """
    This function prints and plots the confusion matrix.
    Normalization can be applied by setting `normalize=True`.
    """
    if normalize:
        cm = cm.astype('float') / cm.sum(axis=1)[:, np.newaxis]
        print("Normalized confusion matrix")
    else:
        print('Confusion matrix, without normalization')

    print(cm)

    plt.imshow(cm, interpolation='nearest', cmap=cmap)
    plt.title(title)
    plt.colorbar()
    tick_marks = np.arange(len(classes))
    plt.xticks(tick_marks, classes, rotation=45)
    plt.yticks(tick_marks, classes)

    fmt = '.2f' if normalize else 'd'
    thresh = cm.max() / 2.
    for i, j in itertools.product(range(cm.shape[0]), range(cm.shape[1])):
        plt.text(j, i, format(cm[i, j], fmt),
                 horizontalalignment="center",
                 color="white" if cm[i, j] > thresh else "black")

    plt.ylabel('True label')
    plt.xlabel('Predicted label')
    plt.tight_layout()


def main():
    y_predict = m.predict(X_test, batch_size=None, verbose=0, steps=None)

    y_pred = convert_to_labels(y_predict)
    y_true = convert_to_labels(y_test)
    target_names = [ 'Hunger','Sleepy' ,'Diaper','Painful']
    print ("month = " + str(month))
    print(classification_report(y_true, y_pred, target_names=target_names))
    print ("**************************************************************")

    plt.figure()
    cnf_matrix = confusion_matrix(y_true, y_pred)
    plot_confusion_matrix(cnf_matrix, classes=target_names,normalize=True,
                    title="month = " + str(month) + ' confusion matrix')

    plt.show()

if __name__ == "__main__":
    main()