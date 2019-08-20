from sklearn.decomposition import PCA
import matplotlib.pyplot as plt 
from sklearn import datasets

iris = datasets.load_iris()
X = iris.data

pca = PCA(n_components=None)
pca.fit(X)

def calc(ratios):
    idx = []        
    accumulating_ratio = []
    for i in range(len(ratios)+1):
        temp = 0
        for j in range(0,i):
            temp += ratios[j]
        idx.append(i)
        accumulating_ratio.append(temp)
    return idx,accumulating_ratio

px,py = calc(pca.explained_variance_ratio_)
plt.plot(px,py)
plt.show()


def getIdx(x,y,T=0.95):
    for i in range(len(x)):
        if y[i] > 0.95:   
            return i
    return -1
    
print (getIdx(px,py))