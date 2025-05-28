import os
# select the directory whose content  you want to list 
directory_path = '/'
# Use the os module to list the directory contect
contents = os.listdir(directory_path)



for item in contents:
    print(item)