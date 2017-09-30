import json


def loadJSON():
    json_file = 'static/unibooks.json'
    json_dump = open(json_file)
    topics = json.load(json_dump)
    json_dump.close()
    return topics

def getAttributes(unibooks, keys):
    for course in unibooks['categories']:
        attribute = json.dumps(course[keys])
    return attribute


# json2 = loadJSON()

# print(getAttributes(json, 'name'))
'''
for course in categories['categories']:
    categoryName = json.dumps(course['name'])
    categoryDir = json.dumps(course['dir'])
    print(categoryName)
    print(categoryDir)

'''