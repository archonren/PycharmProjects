import sys
import json

import data_in    # mock data, currently MetaFilter data dump
import suggestion # the code making the suggestion


def post(data):
    a = suggestion.auto_suggest(data)
    a.find_rules()
    a.suggestion_for_user()
    return a.response_data_user

def compare(input):
    data = data_in.loadData()
    data["USER"] = input.split(",")
    proc = post(data)
    print(proc["USER"])    

if __name__ == '__main__':
    compare(sys.argv[1])
