from django.shortcuts import render
from django.http import HttpResponse
import json,urllib.request
from .import data_in,FP_tree,suggestion


def post(url):
    #url = "http://maps.googleapis.com/maps/api/geocode/json?address=googleplex&sensor=false"
    req = urllib.request.Request(url)
    response = urllib.request.urlopen(req)
    result = json.loads(response.readall().decode('utf-8'))
    data,in_data = data_in.loadData(result)
    D = map(set, data.values())
    F, support_data = FP_tree.fpgrowth(data.values(), 0.6)
    H, rules = FP_tree.generate_rules(F, support_data, 0.6)
    response_data = suggestion.suggestion_for_user(data,rules)
    #tag_suggestion = suggestion_for_tag(rules,tag)
    return HttpResponse(json.dumps(response_data), content_type="application/json")
