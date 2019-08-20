from keras import backend as K
from keras.models import load_model
import matplotlib.pyplot as plt

model = load_model('real_model_path')
def show_feature_map(idx,X):
        layer = K.function([model.layers[0].input], [model.layers[idx].output])
        f1 = layer([X])[0]

        for _ in range(f1.shape[3]):
            show_img = f1[0, :, :, _]
            title_str = "layer " + str(idx) + ", map " + str(_) + "shape="+str(show_img.shape[0]) +"x"+ str(show_img.shape[1])
            print "layer ",idx,show_img.shape

            plt.title(title_str)
            plt.imshow(show_img, cmap='gray')

for i in range(1,len(model.layers)):
    show_feature_map(idx=i,X=imageToUse)