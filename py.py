import json

with open('modrinth.index.json') as f:
    data = json.load(f)

mods = []
for file in data['files']:
    mods.append(file['path'].split('/')[-1])

with open('mods.txt', 'w') as f:
    f.write('\n'.join(mods))