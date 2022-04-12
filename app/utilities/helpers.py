import json

#Loads a json file
def getJsonFromFile(filePath):
    try:
        with open(filePath) as json_file:
            data = json.load(json_file)
        return data
    except:
        data = None
    return data



#Parse a json file and return value of a key
def get_value_by_key(val, js):
    if val == None or js == None:
        return None
    if "/" in val:
        all_keys = val.split("/")
        value = js
        for each_key in all_keys:  # WORKTODO
            if each_key in value.keys():
                value = value[each_key]
            else:
                return None
        return value
    else:

        if val in js.keys():
            return js[val]
        else:
            return None
