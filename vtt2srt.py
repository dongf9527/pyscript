# -*- coding:utf-8 -*-
# script name: vtt2srt.py
# author: dongf9527
# this script is only used to replace vtt to srt, and update timer to 00:00:00:00
# date: 2019/7/25

__author__ = 'dongf9527'

import os,glob

runPath = "c:\\lx\\updateString"

def updateExt():

    files = os.listdir(runPath)  #列出当前目录下所有的文件
 
    for filename in files:
     portion = os.path.splitext(filename)  #分离文件名字和后缀
     #print(portion)
 
     if portion[1] ==".vtt":  #根据后缀来修改,如无后缀则空
         newname = portion[0]+".srt"     #要改的新后缀
         os.chdir(runPath)  #切换文件路径,如无路径则要新建或者路径同上,做好备份
         os.rename(filename,newname)
    #print("file extention are changed to srt")

ret = updateExt()

srts = glob.glob(runPath+'/*.srt')
for one_srt in srts:
    print(one_srt)
    f = open(one_srt, 'r+', encoding='utf-8')
    all_the_lines = f.readlines()
    f.seek(0)
    f.truncate()
    for line in all_the_lines:
        line = line.replace('WEBVTT', 'file is updated!!!')
        line = line.replace('00:', '00:00:')
        line = line.replace('01:', '00:01:')
        line = line.replace('02:', '00:02:')
        line = line.replace('03:', '00:03:')
        line = line.replace('04:', '00:04:')
        line = line.replace('05:', '00:05:')
        line = line.replace('06:', '00:06:')
        line = line.replace('07:', '00:07:')
        line = line.replace('08:', '00:08:')
        line = line.replace('09:', '00:09:')
        f.write(line)
    f.close()
print("Attention! All srt files are updated!!!")


