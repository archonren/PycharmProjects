__author__ = 'Archon_ren'
def suggestion_for_user(data, rules):
    suggestions = {}
    for user in data.keys():
        suggestion = set([])
        for rule in rules:
            if rules[rule]['prior'].issubset(data[user]):
                suggestion = suggestion.union(rules[rule]['post'])
        suggestions[user] = list(suggestion)
    return suggestions

def suggestion_for_tag(rules,tag):
    key = frozenset(tag)
    if key in rules.keys():
        return rules[key]['post']
    else:
        return {}