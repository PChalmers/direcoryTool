from os import listdir
from os import path


class DirectoryTools:
    def __init__(self):
        self.fileNames = []

    def get_directory_contents(self, dir_path):

        only_files = [f for f in listdir(dir_path) if path.isfile(path.join(dir_path, f))]
        only_dirs = [d for d in listdir(dir_path) if path.isdir(path.join(dir_path, d))]

        for file_name in only_files:
            self.fileNames.append(path.join(dir_path, file_name))

        for dir_name in only_dirs:
            self.get_directory_contents(path.join(dir_path, dir_name))

        return self.fileNames

#
# if __name__ == '__main__':
#     dt = DirectoryTools()
#     files = dt.get_directory_contents(r'c:\@Training')
#
#     with open('files.txt', 'w') as f:
#         for file in files:
#             f.write(file + '\n')
