import os
import shutil

def search_dir(path,result):
    child_files = os.listdir(path)
    for child in child_files:
        child = os.path.join(path,child)
        result.append(child)
        if os.path.isdir(child):
            search_dir(child,result)

input_dir = input("输入待搜索的目录：")
output_dir = input("输入保存文件目录：")

files = list()

search_dir(input_dir,files)

for file in files:
    print("find %s"%(file))

    if os.path.isfile(file)and file.endswith(".docx"):
        print("move %s"%(file))
        shutil.move(file,output_dir)