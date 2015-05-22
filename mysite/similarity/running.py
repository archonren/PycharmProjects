from clustering import *
from tag_bag import *
from scivq import *
from vote import *
from user_data import *

def similarity(tag_data,user_data,k):
    '''
    :param tag_data: tag data (array)
    :param user_data: user data (dict)
    :param k: number of cluster
    :return: dict that tells which tag belongs to which cluster {key: tag, value: cluster id}


    sample running code
    #k=8
    #tag_data = tag_bank()
    #user_data,data_in = loadData(tag_data)
    '''
    vectors,no_match = get_vector(tag_data)
    vec_dict = get_tag_id(vectors,k)
    corr_dict = vote(vec_dict,user_data,k)
    return corr_dict
