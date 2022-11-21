__winc_id__ = "ae539110d03e49ea8738fd413ac44ba8"
__human_name__ = "files"

import os
import shutil
import zipfile

def clean_cache():
    directory = "cache"
    parent_dir = r"C:\Users\Daniel\Winc\files" # or os.getcwd() but im being safe and specifying
    cache_dir = r"C:\Users\Daniel\Winc\files\cache" # for deleting could also be os.getcwd() + "\\cache" but is riskier?
    path = os.path.join(parent_dir, directory)
    try:
        os.mkdir(path)
    except OSError as error: 
        shutil.rmtree(cache_dir, ignore_errors=False)
        os.mkdir(path)

def cache_zip(zip_path, cache_path):
    clean_cache() #check the cache is clean
    with zipfile.ZipFile(zip_path, 'r') as zip_ref:
        zip_ref.extractall(cache_path)

def cached_files():
    file_list = []
    for root, dirs, files in os.walk(os.path.abspath(r"C:\Users\Daniel\Winc\files\cache")):
        for file in files:
            x = os.path.join(root,file) #generate file path
            file_list.append(x)  #create list
    return file_list

def find_password(paths):
    for file in paths:
        with open(file, "r") as file:
            lines = file.readlines()
            for line in lines:
                if line.find('password') != -1: #lines that dont have password ignore
                    x = line.replace("password: ","") #shorten to just password
                    password = x.replace("\n","") #to solve new line issue theres probably a better way for this
                    return password

if __name__ == "__main__":
    #print (cache_zip(r"C:\Users\Daniel\Winc\files\data.zip", r"C:\Users\Daniel\Winc\files\cache"))
    #print (cached_files())
    print (find_password(cached_files()))