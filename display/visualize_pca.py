import numpy as np
from glob import glob
import sys
import matplotlib.image as mpimg
import matplotlib.pyplot as plt
import pdb
import cPickle as pickle
from sklearn.decomposition import PCA

sbj_id_all = ["d6532718", "cb46fd46", "fcb01f7a", "a86a4375", "c95c1e82", "e70923c4" ]
dates_all = [[4,5,6,7], [7,8,9,10], [8,10,11,12], [4,5,6,7], [4,5,6,7], [4,5,6,7]]

mymap = plt.get_cmap("rainbow")
colorspace = np.r_[np.linspace(0.1, 1, 6), np.linspace(0.1, 2, 6)]
colors = mymap(colorspace)

for s, sbj_id in enumerate(sbj_id_all):
    print sbj_id
    for day in dates_all[s]:
        pca = pickle.load(open("D:\\ecog_processed\\d_reduced\\transformed_pca_model_" + sbj_id + "_" + str(day) + ".p", "rb"))
        variance = np.cumsum(pca.explained_variance_ratio_)
        plt.plot(variance, color=colors[s])
    plt.plot(variance, color=colors[s], label=("Subject " + str(s+1)))
    #plt.title("PCA cumulative variance for all subjects ")
    plt.xlabel("Number of components")
    plt.ylabel("Cumulative Variance Explained")
    plt.ylim([0,1])
    plt.legend()
    #plt.legend()
plt.savefig("D:\\ecog_processed\\d_reduced\\transformed_pca_variance.eps")
plt.close()
