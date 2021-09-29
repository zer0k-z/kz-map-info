import requests
import json

def MWM_simplifier():
    input_file = open('MapsWithMappers.json', encoding='utf-8')
    map_list = json.load(input_file)
    simple_list = []
    for map_info in map_list:
        simple_list.append(map_info['name'])
    return simple_list

map_names = MWM_simplifier()
maps = []
for offset in range(3):
    map_offset = {'offset':str(offset*500), 'is_validated':'true'}
    r = requests.get('https://kztimerglobal.com/api/v2/maps', params = map_offset)
    maps = maps + r.json()
API_map_names = []
for map_info in maps:
    API_map_names.append(map_info['name'])


temp3 = [x for x in API_map_names if x not in set(map_names)]
temp4 = [x for x in map_names if x not in set(API_map_names)]
print('Missing maps from API:' + str(temp3))
print('Maps that no longer exist in API:' + str(temp4))