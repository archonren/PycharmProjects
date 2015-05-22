__author__ = 'Archon_ren'
from gensim.models import Word2Vec
from gensim import matutils
from numpy import float32 as REAL,\
    array
import numpy as np
from scivq import *


def get_vector(data):
    '''
    :param data: array that contain all tags
    :return: vectors: dict {key : tag, value dim 300 vector from GoogleNews database}
    '''
    model = Word2Vec.load_word2vec_format('c:/GoogleNews.bin', binary=True)
    vectors={}
    no_match = []
    for item in data:
        try:
            vec = model[item]
            vectors[item] = vec
        except KeyError:
            try:
                mean = []
                for word in item.split():
                     mean.append(model[word])
                mean = matutils.unitvec(array(mean).mean(axis=0)).astype(REAL)
                vectors[item] = mean
            except:
                print('ooops!',item,"does not appear in the google database")
                no_match.append(item)

    return vectors,no_match

def get_tag_id(vectors,k):
    '''
    :param vectors: dict of tags{key:tag, value: 300 dim vector}
    :param k: number of cluster
    :return: dict that tells which tag belongs to which cluster {key: tag, value: cluster id}
    '''
    vec = []
    vec_key = []
    for key in vectors.keys():
        vec_key.append(key)
        vec.append(vectors[key])
    vec_array = np.array(vec).reshape((-1,300))
    centers,dist = kmeans(vec_array,k)
    code,distance = vq(vec_array,centers)
    vec_dict = {}
    for i in range(len(code)):
        vec_dict[vec_key[i]] = code[i]
    return vec_dict

