Qimport json
json_file = 'unibooks.json'
unibooks = open(json_file)
categories = json.load(unibooks)
unibooks.close()

#print "Courses:\n"

#print()
for course in categories['categories']:
    jsonstring = json.dumps(course['name'])
    print(jsonstring)