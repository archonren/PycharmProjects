from tag_bag import *
from scivq import *
from user_data import *
from gensim.models import Word2Vec
from gensim import matutils
from numpy import float32 as REAL,array,sum,zeros
from scipy.stats.stats import pearsonr

class data(object):
    def __init__(self,tag_data,user_data,k,path):
        self.tag_data = tag_data
        self.user_data = user_data
        self.k = k
        self.model = Word2Vec.load_word2vec_format(path, binary=True)
        self.minimium_model = {}
        self.no_match_tag = []
        self.vec_dict = {}
        self.corr_dict = {}

    def get_minimium_model(self):
        '''
        :return: minimium model: dict contain just the tag in the bank and corresponding 300 dim vector
        '''
        for item in self.tag_data:
            try:
                vec = self.model[item]
                self.minimium_model[item] = vec
            except KeyError:
                try:
                    mean = []
                    for word in item.split():
                        mean.append(self.model[word])
                    mean = matutils.unitvec(array(mean).mean(axis=0)).astype(REAL)
                    self.minimium_model[item] = mean
                except KeyError:
                    print('ooops!',item,"does not appear in the google database")
                    self.no_match_tag.append(item)
        if self.no_match_tag != []:
            print('missing tags', self.no_match_tag)



    def clustering(self):
        '''
        :return: dict that tells which tag belongs to which cluster {key: tag, value: cluster id}
        '''
        if self.minimium_model == {}:
            print('minimium model has not been load')
            raise AttributeError
        elif type(self.minimium_model) != dict:
            raise TypeError
        else:
            vec = []
            vec_key = []
            for key in self.minimium_model.keys():
                vec_key.append(key)
                vec.append(self.minimium_model[key])
            vec_array = array(vec).reshape((-1,300))
            centers,dist = kmeans(vec_array,self.k)
            code,distance = vq(vec_array,centers)
            for i in range(len(code)):
                self.vec_dict[vec_key[i]] = code[i]


    def vote(self,topn = 3):
        '''
        :param vec_dict: dict that tells which tag belongs to which cluster {key: tag, value: cluster id}
        :param user_data: user data
        :param k: number of cluster
        :param topn: optional, default 3, return top n similar user
        :return: dict that contain top n most similar user {key : user, value: suggest users}
        '''
        if self.vec_dict == {}:
            print('clustering not completed')
            raise AttributeError
        elif type(self.vec_dict) != dict:
            raise TypeError
        else:
            user_item_dict = {}
            for key in self.user_data.keys():
                vote_array = zeros((self.k,1))
                for item in self.user_data[key]:
                    vote_array[self.vec_dict[item]] += 1
                user_item_dict[key] = vote_array/sum(vote_array)

            for key1 in self.user_data.keys():
                temp_dict = {}
                short_list = []
                for key2 in self.user_data.keys():
                    if key2!=key1:
                        temp_dict[key2] = (pearsonr(user_item_dict[key1],user_item_dict[key2])[0])
                most_similar = sorted(temp_dict, key=temp_dict.get,reverse=True)
                for i in range(topn):
                    short_list.append(most_similar[i])
                self.corr_dict[key1] = short_list



def example(tag_data,user_data,k,path):
    '''
    :param tag_data: tag data (array)
    :param user_data: user data (dict)
    :param k: number of cluster
    :return: dict that tells which tag belongs to which cluster {key: tag, value: cluster id}
    '''

    x = data(tag_data,user_data,k,path)
    x.get_minimium_model()
    x.clustering()
    x.vote(topn=4)
    return x.corr_dict

tag_data = tag_bank()
user_data,data_in = loadData(tag_data)
print(example(tag_data,user_data, 8, 'c:/GoogleNews.bin'))