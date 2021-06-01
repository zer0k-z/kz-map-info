import json

# Fix for unicode characters because of p's name
def unescape(in_str):
    """Unicode-unescape string with only some characters escaped."""
    return in_str.encode('unicode-escape').replace(b'\\\\u', b'\\u').decode('unicode-escape')

input_file = open('MapsWithMappers.json', encoding='utf-8')
map_list = json.load(input_file)
incompleted_list = []
incompleted_maps = []

for map_info in map_list:
    if not ('mapper_name' in map_info):
        incompleted_list.append(map_info)
        incompleted_maps.append(map_info['name']+(' (Missing mapper name)'))
    elif not ('mapper_steamid64' in map_info) or 'null' in map_info['mapper_steamid64']:
        incompleted_list.append(map_info)
        incompleted_maps.append(map_info['name']+(' (Missing mapper steamID)'))

output_file = open('IncompletedMaps.json', 'w', encoding='utf8')
output_file.write(unescape(json.dumps(incompleted_list, indent=4)))
print('Missing maps dumped to IncompletedMaps.json.')
print('Remaining maps with missing information:')
print(*incompleted_maps, sep='\n')