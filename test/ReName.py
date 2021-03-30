#!/usr/bin/python

import os

# path为批量文件的文件夹的路径
path = '/Users/lm188/PycharmProjects/untitled/fengli/walletool/JiaguPlugin/channels'

path = '/Users/lm188/fengli/fengli_im_temp/JiaguPlugin/channels'

# app_yunTest_V1.0.6.20210308142111_10620210308142111_jiagu_sign_aligned_signed_oppo
# 文件夹中所有文件的文件名
file_names = os.listdir(path)

# 外循环遍历所有文件名，内循环遍历每个文件名的每个字符
for name in file_names:
    print("文件名称："+name)
    newName = name.replace("_105_jiagu_sign_aligned_signed", "")
    os.renames(os.path.join(path, name), os.path.join(path, newName))