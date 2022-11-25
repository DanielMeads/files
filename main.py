__winc_id__ = "ae539110d03e49ea8738fd413ac44ba8"
__human_name__ = "files"

import os
import shutil
import zipfile

cwd = os.getcwd() 
cache_dir = os.path.join(cwd, "files\\cache")
cache_zip_file = os.path.join(cwd, "files\\data.zip")

def main():
    #print (clean_cache())
    #print (cache_zip(cache_zip_file, cache_dir))
    #print (cached_files())
    print (find_password(cached_files()))

def clean_cache():
    try:
        os.mkdir(cache_dir)
    except OSError: 
        shutil.rmtree(cache_dir, ignore_errors=False)
        os.mkdir(cache_dir)

def cache_zip(zip_path, cache_path):
    clean_cache()
    with zipfile.ZipFile(zip_path, 'r') as zip_ref:
        zip_ref.extractall(cache_path)

def cached_files():
    file_list = []
    for root, dirs, file in os.walk(os.path.abspath(cache_dir)):
        for file in file:
            x = os.path.join(root, file)
            file_list.append(x)
    return file_list

def find_password(paths):
    for file in paths:
        with open(file, "r") as file:
            lines = file.readlines()
            for line in lines:
                if line.find('password') != -1:
                    x = line.replace("password: ", '')
                    password = x.rstrip()
                    return password

if __name__ == "__main__":
    main()
