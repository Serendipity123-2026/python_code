import os

file_list = []
for f in os.listdir('../After-class homework code'):
    if f not in file_list:
        file_list.append(f)
        print(file_list)
print(f"当前目录下所有.py文件的数量为{len(file_list)}")


