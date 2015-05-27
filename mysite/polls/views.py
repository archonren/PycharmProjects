import data_in,suggestion
import sys
import json

def post():
    data = data_in.loadData()
    a = suggestion.auto_suggest(data)
    a.find_rules()
    a.suggestion_for_user()
    return json.dumps(a.response_data_user)

if __name__ == '__main__':
    print(post())

