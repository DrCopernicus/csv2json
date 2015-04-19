import csv
import json
import string

# wow i've never seen a more beautiful code
# i deserve an oscar or something


def add_to_output(outlist, cat, value):
    if isinstance(cat, str) or len(cat) == 1:
        outlist[cat[0]] = value
    else:
        if cat[0] not in outlist:
            outlist[cat[0]] = {}
        tiger = outlist[cat[0]]  # why is this called tiger?
        add_to_output(tiger, cat[1:], value)

def make_a_list(filename):
    output = {filename: []}
    with open(filename+'.csv') as csv_file:
        for molecule in csv.DictReader(csv_file):  # and why is this called molecule??
            outarea = {}
            for key in molecule:
                if molecule[key].startswith('$$FILE.'):
                    add_to_output(outarea, string.split(key,'.'), make_a_list((string.split(molecule[key],'.',maxsplit=1))[1]))
                else:
                    add_to_output(outarea, string.split(key,'.'), molecule[key])
            output[filename].append(outarea)
    return output[filename]

superfilename = raw_input('Enter file without ext: ')
superout = make_a_list(superfilename)

f = open(superfilename+'.json','w')
f.write(json.dumps(superout[0], sort_keys=True, indent=2))
f.close()