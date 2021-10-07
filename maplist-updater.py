import requests
import json

# Fix for unicode characters
def unescape(in_str):
    """Unicode-unescape string with only some characters escaped."""
    return in_str.encode('unicode-escape').replace(b'\\\\u', b'\\u').decode('unicode-escape')

def missingids(name, ids):
    missinglist = ""
    for i in range(len(ids.split(', '))):
        if ids.split(', ')[i] == 'null':
            missinglist += name.split(', ')[i]
    return missinglist

input_file = open('MapsWithMappers.json', encoding='utf-8')
map_list = json.load(input_file)
map_names = []
for map_info in map_list:
    map_names.append(map_info['name'])

maps = []
for offset in range(3):
    map_offset = {'offset':str(offset*500), 'is_validated':'true'}
    r = requests.get('https://kztimerglobal.com/api/v2/maps', params = map_offset)
    maps = maps + r.json()


API_map_names = []
for map_info in maps:
    API_map_names.append(map_info['name'])


missing_global_map_names = [x for x in API_map_names if x not in set(map_names)]
non_global_map_names = [x for x in map_names if x not in set(API_map_names)]
print('Missing maps from API:' + str(missing_global_map_names))
print('Maps that no longer exist in API:' + str(non_global_map_names))


for map_info in maps:
    if map_info['name'] in missing_global_map_names:
        map_list.append({"id": str(map_info['id']), "name": map_info['name'], "difficulty": str(map_info['difficulty']), "workshop_url": map_info['workshop_url'], 'mapper_name': {}, 'mapper_steamid64': {}})

with open('MapsWithMappers.json', 'w', encoding='utf-8') as file:
    file.write(unescape(json.dumps(map_list, indent = 4)))

non_global_maps = []
global_maps = []
for map_info in map_list:
    if map_info['name'] in non_global_map_names:
        non_global_maps.append(map_info)
    else:
        global_maps.append(map_info)


with open('MapsWithMappers.json', 'w', encoding='utf-8') as file:
    file.write(unescape(json.dumps(map_list, indent = 4)))
    
with open('MapsWithMappers_Global.json', 'w+', encoding='utf-8') as file:
    file.write(unescape(json.dumps(global_maps, indent = 4)))

with open('MapsWithMappers_NonGlobal.json', 'w+', encoding='utf-8') as file:
    file.write(unescape(json.dumps(non_global_maps, indent = 4)))

incompleted_list = []
incompleted_maps = []

for map_info in map_list:
    if not ('mapper_name' in map_info):
        incompleted_list.append(map_info)
        incompleted_maps.append(map_info['name']+(' - Missing mapper name'))
    elif map_info['mapper_name'] == "None":
        incompleted_list.append(map_info)
        incompleted_maps.append(map_info['name']+(' - Missing mapper name'))
    elif not ('mapper_steamid64' in map_info):
        incompleted_list.append(map_info)
        incompleted_maps.append(map_info['name']+(' - Missing SteamID(s): {0}').format(map_info['mapper_name']))
    elif 'null' in map_info['mapper_steamid64']:
        incompleted_list.append(map_info)
        incompleted_maps.append(map_info['name']+(' - Missing SteamID(s): {0}').format(missingids(map_info['mapper_name'], map_info['mapper_steamid64'])))
output_file = open('IncompletedMaps.json', 'w', encoding='utf8')
output_file.write(unescape(json.dumps(incompleted_list, indent=4)))
incompleted_maps_file = open('IncompletedMaps_Simple.txt', 'w', encoding='utf8')
incompleted_maps_file.writelines(["%s\n" % incompleted_map  for incompleted_map in incompleted_maps])
print('Missing maps dumped to IncompletedMaps.json and IncompletedMaps_Simple.txt.')