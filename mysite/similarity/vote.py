__author__ = 'Archon_ren'
from numpy import sum,zeros
from scipy.stats.stats import pearsonr

def unified(vec):
    return vec/sum(vec)

def vote(vec_dict,user_data,k, topn = 3):
    '''
    :param vec_dict: dict that tells which tag belongs to which cluster {key: tag, value: cluster id}
    :param user_data: user data
    :param k: number of cluster
    :param topn: optional, default 3, return top n similar user
    :return: dict that contain top n most similar user {key : user, value: suggest users}
    '''
    user_item_dict = {}
    for key in user_data.keys():
        vote_array = zeros((k,1))
        for item in user_data[key]:
            vote_array[vec_dict[item]] += 1
        user_item_dict[key] = unified(vote_array)
    corr_dict = {}
    for key1 in user_data.keys():
        corr_max = -1
        dict = {}
        short_list = []
        for key2 in user_data.keys():
            if key2!=key1:
                dict[key2] = (pearsonr(user_item_dict[key1],user_item_dict[key2])[0])
        most_similar = sorted(dict, key=dict.get,reverse=True)
        for i in range(topn):
            short_list.append(most_similar[i])
        corr_dict[key1] = short_list
    return corr_dict