import csv
import json
import string

# wow i've never seen a more beautiful code
# i deserve an oscar or something


filename = raw_input('Enter file without ext: ')
output = {filename: []}

def add_to_output(outlist, cat, value):
    if isinstance(cat, str) or len(cat) == 1:
        outlist[cat[0]] = value
    else:
        if cat[0] not in outlist:
            outlist[cat[0]] = {}
        tiger = outlist[cat[0]] # why is this called tiger?
        add_to_output(tiger, cat[1:], value)

with open(filename+'.csv') as csv_file:
    for molecule in csv.DictReader(csv_file): # and why is this called molecule??
        outarea = {}
        for key in molecule:
            add_to_output(outarea, string.split(key,'.'), molecule[key])
        output[filename].append(outarea)

output_json = json.dumps(output[filename], sort_keys=True, indent=2)

f = open(filename+'.json','w')
f.write(output_json)
f.close()