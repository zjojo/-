# encoding:utf-8
import os
# import shutil
"""
将当前目录的所有扩展名为“html"文件修改为扩展名为”htm"的文件
shutil 模块有copyfile() 复制文件
"""
# 不简单的代码
file_list = os.listdir(".") # 返回指定路径下的文件和文件夹列表。
for file_name in file_list:
    pos = file_name.rindex(".")  # 当找不到.时会报异常
    if file_name[pos+1:] == "html":
        newname = file_name[:pos+1] + "htm"
        os.rename(file_name, newname)
        print(file_name+"更名为："+newname)

# 使用列表推导式
file_list = [filename for filename in os.listdir(".") if filename.endwith(".html")]
for file in file_list:
    new_name = file[:-4] +"htm"
    os.rename(file, new_name)
    print(file +"更名为："+ new_name)