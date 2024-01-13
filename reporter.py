import json

def getChamp():
    result = {}
    with open('data/championFull.json', encoding="utf-8") as d:
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
    result = {}
    with open('data/item.json', 'r', encoding='utf-8') as f:
        database = json.load(f)['data']
        for k in database:
            print('{}. {}'.format(k, database[k]['name']))
        itemID = input("\nWhat is the item's id: ")
        itemData = database[itemID]
        f.close()
    with open('{}.json'.format(itemData['name']), 'w', encoding='utf-8') as w:
        json.dump(itemData, w, indent=4, ensure_ascii=False)
        w.close()

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
