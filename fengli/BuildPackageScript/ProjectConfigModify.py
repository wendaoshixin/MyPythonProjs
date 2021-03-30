#!/usr/bin/python
# -*- coding:utf-8 -*-
import re
from pip._vendor import chardet
try:
    import xml.etree.cElementTree as ET
except ImportError:
    import xml.etree.ElementTree as ET


def checkServerTypeModifyMacro(fileName, isTestServer, defaultMacro="TEST"):
    nameSpace = "http://schemas.microsoft.com/developer/msbuild/2003"
    ET.register_namespace('', nameSpace)
    tree = ET.ElementTree(file=fileName)
    nodelist = tree.findall("{"+nameSpace+ "}PropertyGroup")
    # print(nodelist)

    needModifyTargetFile = False
    for parent_node in nodelist:
        children = parent_node.getchildren()
        for child in children:
            if (child.tag == "{"+nameSpace+ "}DefineConstants"):
                foundTestMacro = False
                needModifyTargetMacro = False;
                newMacoStr = ""
                macroList = child.text.split(";")
                for tmpMacro in macroList:
                    if(tmpMacro == defaultMacro):
                        foundTestMacro = True
                        if(isTestServer):
                            newMacoStr += tmpMacro;
                            continue
                        else:
                            print("正式服务器删除宏")
                            needModifyTargetMacro = True
                            continue
                    else:
                        newMacoStr += tmpMacro+";";

                if(not foundTestMacro and isTestServer):
                    print("测试服务器追加宏")
                    needModifyTargetMacro = True
                    newMacoStr += defaultMacro

                if(needModifyTargetMacro):
                    if(newMacoStr.endswith(";")):
                        newMacoStr = newMacoStr[0:-1]
                    print(f"修改前的宏={child.text}")
                    needModifyTargetFile = True
                    child.text = newMacoStr;
                    print(f"修改后的宏={child.text}")



    if(needModifyTargetFile):
        tree.write(fileName, encoding="utf-8", xml_declaration=True)
    return
# utf-8 or gb2312
def get_encoding(file):
    # 二进制方式读取，获取字节数据，检测类型
    with open(file, 'rb') as f:
        return chardet.detect(f.read())['encoding']

def getVersion(assemblyInfoFilePath):
    result = "";
    encodingType = get_encoding(assemblyInfoFilePath)
    with open(assemblyInfoFilePath, 'r', encoding=encodingType) as f:
        for line in f:
            if 'AssemblyVersion' in line:
                versionList = re.findall(r"(?:[0-9]{1,3}\.){3}[0-9]{1,3}", line)
                if versionList:
                    result = versionList.pop(0)
                    break
    return  result

def modifyVersion(assemblyInfoFilePath, oldVerion, newVersion):
    # 打开文件，用只读'r'的模式打开，把数据读到内存中
    encodingType = get_encoding(assemblyInfoFilePath)
    f = open(assemblyInfoFilePath, 'r', encoding=encodingType)
    lines = f.readlines()  # readlines()把文件一行一行读出来，并存成一个列表
    f.close()  # 关闭文件

    # 再次打开同一文件，这次采用w模式，对文件进行覆盖修改
    with open(assemblyInfoFilePath, 'w', encoding=encodingType) as f2:
        for line in lines:  # 对列表进行遍历，把每一行写入原文件中。此时：因为w模式打开文件，文件内容为空！
            line = line.replace(oldVerion, newVersion)
            f2.write(line)
        f2.flush()
    return

def getIntputNewVersionThenModify(assemblyInfoFilePath):
    oldVersion = getVersion(assemblyInfoFilePath)
    newVersion = ""
    # print("获得的版本号是：" + oldVersion)
    inputVersionStr = str(input(f"你当前的版本号是:{oldVersion}, 请输入你的新版本号："))
    versionList = re.findall(r"(?:[0-9]{1,3}\.){3}[0-9]{1,3}", inputVersionStr)
    if versionList:
        newVersion = versionList.pop(0)

    if (not newVersion):
        print(f"你输入的版本:{inputVersionStr}, 是非法的。编译版本号保持不变:{oldVersion}")
        return  oldVersion
    elif (oldVersion == newVersion):
        print(f"你输入的版本当前版本一致。编译版本号保持不变:{oldVersion}")
        return oldVersion
    else:
        print(f"你旧版本号是:{oldVersion}, 你的新版本号是:{newVersion}")
        modifyVersion(assemblyInfoFilePath, oldVersion, newVersion)
        return newVersion

if __name__ == "__main__":
    # checkServerTypeModifyMacro("./Service.xml", False)
    # getIntputNewVersionThenModify("assembly")
    pass








