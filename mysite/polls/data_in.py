import json
def loadData(data_in):

    data = \
        {
            'User A':['art', 'phy', 'history', 'career', 'esl'],
            'User B':['phy', 'chem', 'math', 'writing', 'visual', 'university', 'health', 'social'],
            'User C':['phy'],
            'User D':['art', 'math', 'number', 'bio', 'social'],
            'User E':['chem', 'art', 'math', 'phy', 'native', 'health', 'esl'],
            'User F':['chem', 'phy', 'math', 'tech', 'native', 'social', 'health', 'music'],
            'User G':['chem', 'math', 'tech', 'social', 'health', 'music'],
            'User H':['chem', 'math', 'tech', 'tech', 'health', 'music']
        }
    try:
        result = json.loads(data_in.readall().decode('utf-8'))
    except:
        print('file dose not read properly. mistake in data_in code')
    return data,data_in
