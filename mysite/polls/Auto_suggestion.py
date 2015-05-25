

def post():


    parser = OptionParser()
    parser.add_option("-f", "--file", dest="filename",
                  help="write report to FILE", metavar="FILE")
    parser.add_option("-q", "--quiet",
                  action="store_false", dest="verbose", default=True,
                  help="don't print status messages to stdout")

    (options, args) = parser.parse_args()
    data,in_data = data_in.loadData()
    a = auto_suggest(data)
    a.find_rules()
    a.suggestion_for_user()
    print(a.response_data_user)
    #tag_suggestion = suggestion_for_tag(rules,tag)