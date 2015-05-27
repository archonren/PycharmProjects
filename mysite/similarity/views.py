from similarity import *
from tag_bag import *
from user_data import *
from simplejson.compat import StringIO

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

def main(model_path):
    tag_data = tag_bank()
    user_data,data_in = loadData(tag_data)
    io = StringIO()
    response = example(tag_data,user_data, 8, model_path)
    json.dump(response, io)
    io.getvalue()
    
if __name__ == '__main__':
    main(argv[1])
