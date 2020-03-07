from os import walk

def testing():
    print('testing')


def get_file_list(dir_name):
    f = []
    for (dirpath, dirnames, filenames) in walk(dir_name.get()):
 #       f.extend(dirpath)
        print(dirpath, dirnames, filenames)
    return f