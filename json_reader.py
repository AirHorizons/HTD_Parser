import os, sys, json
import fnmatch

file_path = './output/'

def filter_path(path_list):
    # since macOS has redundant DS_Store file, filter this file
    ign = '.DS_Store'
    if ign in path_list:
        path_list.remove(ign)
    return path_list

def get_files():
    global file_path
    matches = []
    for root, subdir, filenames in os.walk(file_path):
        for filename in fnmatch.filter(filenames, '*.json'):
            matches.append(os.path.join(root, filename))
    return matches

def get_dict(filename):
    dct = None
    with open(filename, 'r') as fr:
        dct = json.load(fr)
    return dct

print(get_dict(get_files()[100]))
