# Write a function that identifies sets of files with identical contents.
# 
#     find_dupes(root_path) → sets/lists of file paths that have identical contents
# 
#     find_dupes(“/home/whatever”) → [
#         [".bashrc", "Backups/2017_bashrc"],
#         ["Photos/Vacation/DSC1234.JPG", "profile.jpeg", ".trash/lej2dp28/87msnlgyr"],
#     ]
# 
# Context:
# - Imagine this function being packaged up into a command-line tool and people running it on their laptops or servers.
# - For scale, imagine hard drives with at most 2 TB of data and at most 1M files.
# 
# For traversing the filesystem, use these library functions:
# - list_folder(path) → list of immediate file and folder children
# - is_folder(path) → boolean

from collections import defaultdict

# list(find_dupes("some_path")) -> [[..., ..], [..., ]]

def find_dupes(root_path):
    all_files = defaultdict(list)

    for size, path in recurse_files(root_path, file_size):
        all_files[size].append(path)

    same_size_files = defaultdict(list)

    for paths in all_files.values():
        for path in paths:
            same_size_files[md5(path)].append(path)

    for paths in same_size_files.values():
        if len(paths) > 1:
            yield paths

# [[..., ....],
#   [..., ...., ...]]


def recurse_files(root_path): # recurse_files("some_path", md5 or file_size)
    for path in list_folder(root_path):
        if is_folder(path):
            recurse_files(path)
        yield file_size(path), path