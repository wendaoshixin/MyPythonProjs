#!/usr/bin/python
import os
import re
from xml.dom.minidom import parse
import xml.dom.minidom

from IMproject_strings.uselessString.nouseStringRestore import removeNoUseString


def ParseXml(fileName):
    print("begin to parse %s" % (fileName))
    DOMTree = xml.dom.minidom.parse(fileName)
    value_map = {}
    collection = DOMTree.documentElement
    if collection:
        values = collection.getElementsByTagName("string")

    if values:
        for value in values:
            if value.hasAttribute("name"):
                map_key = value.getAttribute("name")

                children = value.childNodes;
                if children:
                    map_value = value.childNodes[0].data
                else:
                    map_value = ""

                value_map[map_key] = map_value

    return value_map

def getResult(resultLines):
    ret = False
    for line in resultLines:
        # print(line)
        ret = True
        break
        # versionList = re.findall(r"^==========.*==========$", line)
        # if versionList:
        #     countList = re.findall(r"[0-9]\d*", versionList[0])
        #     if countList and len(countList) == 4:
        #         errorCount = int(countList[1])
        #         if errorCount > 0:
        #             print(f"编译出现了{errorCount}个错误")
        #             ret = errorCount

    return  ret

def grepJavaStr(key, projectDir):
    # result = os.system(commandProjStr)
    # cmdOutLines = os.popen(commandProjStr)
    # commandProjStr = f'find {projectDir} -name "*.java" |xargs cat  |grep -Hsn  "R.string.{key}" --binary-files=without-match > grep1.txt'
    commandProjStr = f'find {projectDir} -name "*.java" |xargs cat  |grep -Hsn  "R.string.{key}" --binary-files=without-match'
    # print("执行命令=>> " + commandProjStr)
    # os.system(commandProjStr)
    cmdOutLines = os.popen(commandProjStr)
    return getResult(cmdOutLines)
    # return  cmdOutLines.

def grepXmlStr(key, projectDir):
    commandProjStr = f'find {projectDir} -name "*.xml" |xargs cat  |grep -Hsn  "@string/{key}" --binary-files=without-match'
    # print("执行命令=>> " + commandProjStr)
    cmdOutLines = os.popen(commandProjStr)
    return getResult(cmdOutLines)

def findNotFoudString(notFoundList, value_map):
    string_keys = value_map.keys()
    keyList = list(string_keys)
    size = len(keyList);
    # size = min(size, 10)
    for i in range(0, size):
        key = keyList[i]

        print(f'第{i}个是：{key}')
        result = grepJavaStr(key, rootPath)
        if not result:
            result = grepXmlStr(key, rootPath)
            if not result:
                notFoundList.append(key)

if __name__ == '__main__':
    print("Begin write key,value to [string.xml] file....")
    rootPath = "/Users/lm188/AndroidStudioProjects/im_android_devlop/"
    print("字符串："+rootPath)
    # stringFileNnam = rootPath + "reslibrary/src/main/res/values/strings.xml"
    # values values-zh-rCN  values-zh-rTW
    stringFileNnam = rootPath + "reslibrary/src/main/res/values-zh-rTW/strings.xml"
    print("字符串2：" + rootPath)


    value_map = ParseXml(stringFileNnam)

    notFoundList = []
    # findNotFoudString(notFoundList, value_map)
    removeNoUseString(value_map, notFoundList)

    print(f"没有使用的字符串：{notFoundList}")



    # for i in range(0, len(string_keys)):
    #     key = keyList[i]
    #     value = value_map[key]
    #     if not value:
    #         value = ""


    # print(value_map)

    print("Done.")