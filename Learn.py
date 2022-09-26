!/usr/bin/env python3
# -*- encoding: utf-8 -*-
# https://docs.python.org/zh-cn/3.9/
import os
import sys
# import subprocess
print(sys.executable)
print(os.listdir("/root"))
print("显示中文？")
# os.remove()             #删除文件
# os.rename()             #重命名文件
# os.walk()               #生成目录树下的所有文件名
# os.chdir()              #改变目录
# os.mkdir/makedirs       #创建目录/多层目录
# os.rmdir/removedirs     #删除目录/多层目录
# os.listdir()            #列出指定目录的文件
# os.getcwd()             #取得当前工作目录
# os.chmod()              #改变目录权限
# os.path.basename()      #去掉目录路径，返回文件名
# os.path.dirname()       #去掉文件名，返回目录路径
# os.path.join()          #将分离的各部分组合成一个路径名
# os.path.getsize()       #返回文件大小
# os.path.exists()        #是否存在
# os.path.isabs()         #是否为绝对路径
# os.path.isdir()         #是否为目录
# os.path.isfile()        #是否为文件
command = 'ls -lh'
os.system(command)
os.system('ip a && pwd')
