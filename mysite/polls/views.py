from django.http import HttpResponse
import json,urllib.request
import data_in,suggestion
from simplejson.compat import StringIO
import urllib.request
import data_in,suggestion
import sys
def post(arg):
    #url = "http://maps.googleapis.com/maps/api/geocode/json?address=googleplex&sensor=false"

    req = urllib.request.Request(arg)
    response = urllib.request.urlopen(req)
    data,in_data = data_in.loadData(response)
    a = suggestion.auto_suggest(data)
    a.find_rules()
    a.suggestion_for_user()
    io = StringIO()
    json.dump(a.response_data_user, io)
    io.getvalue()
    #tag_suggestion = suggestion_for_tag(rules,tag)


if __name__ == '__main__':
    post(sys.argv[1])

