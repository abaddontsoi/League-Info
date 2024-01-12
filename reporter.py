import json

def getChamp():
    result = {}
    with open('data/championFull.json', encoding="utf8") as d:
        file = json.load(d)
        database = file['data']
        for name in database.keys():
            print(name)
        champName = input("\nPlease enter champion's name: ")     
        champData = database[champName]
        d.close()

    result['chamName'] = champData['name']
    result['chamStat'] = champData['stats']
    result['chamPassive'] = champData['passive']
    result['chamSpells'] = champData['spells']

    with open('{}.json'.format(result['chamName']), 'w') as f:
        f.write(json.dumps(result, indent=4))
        f.close()

def getItem():
    itemName = input("\nWhat is the item's name: ")
    pass

print("==============================")
print("Please select which type of info you want to report:")
print("1. Champion")
print("2. Item")
print("==============================")

selection = int(input())


result = {}
if selection == 1:
    result = getChamp()

if selection == 2:
    result = getItem()
