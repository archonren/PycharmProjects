from django.http import HttpResponse
import json,urllib.request
import data_in,suggestion
import argparse
def post():
    #url = "http://maps.googleapis.com/maps/api/geocode/json?address=googleplex&sensor=false"
    parser = argparse.ArgumentParser(description='Pass a file url')
    parser.add_argument('input_url',
                   help='an file url')

    argument = parser.parse_args()
    req = urllib.request.Request(argument.input_url)
    response = urllib.request.urlopen(req)
    data,in_data = data_in.loadData(response)
    a = suggestion.auto_suggest(data)
    a.find_rules()
    a.suggestion_for_user()
    print(a.response_data_user)
    #tag_suggestion = suggestion_for_tag(rules,tag)

