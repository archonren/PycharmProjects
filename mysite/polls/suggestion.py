__author__ = 'Archon_ren'
from FP_tree import *

class auto_suggest(object):
    def __init__(self,user_data):
        self.user_data = user_data

        self.F = []
        self.support_data= {}

        self.H = []
        self.rules = {}

        self.response_data_user = {}
        self.response_data_tag = {}

    def find_rules(self):
        self.F,self.support_data = fpgrowth(self.user_data.values(), 0.6)
        self.H,self.rules = generate_rules(self.F, self.support_data, 0.6)

    def suggestion_for_user(self):
        for user in self.user_data.keys():
            suggestion = set([])
            for rule in self.rules:
                if self.rules[rule]['prior'].issubset(self.user_data[user]):
                    suggestion = suggestion.union(self.rules[rule]['post'])
            self.response_data_user[user] = list(suggestion)

    def suggestion_for_tag(self,tag):
        key = frozenset(tag)
        if key in self.rules.keys():
            return self.rules[key]['post']
        else:
            return {}
    def flush(self):
        pass
