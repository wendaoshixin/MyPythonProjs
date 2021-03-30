#!/usr/bin/python
import os
import re
import xml.dom.minidom

map_list = []
string_keys = []
stringPath = ''
excel_name = ''

def ParseKey(fileName):
    DOMTree = xml.dom.minidom.parse(fileName)
    collection = DOMTree.documentElement
    if collection:
        values = collection.getElementsByTagName("string")
        
    keys = []
    if values:
        for value in values:
            if value.hasAttribute("name"):
                map_key = value.getAttribute("name")
                keys.append(map_key)

    return keys


def ParseXml(fileName):
    print("begin to parse %s" % (fileName))
    DOMTree = xml.dom.minidom.parse(fileName)
    value_map = {}
    collection = DOMTree.documentElement
	#values = []
    if collection:
        values = collection.getElementsByTagName("string")

    if values:
        for value in values:
            if value.hasAttribute("name"):
                map_key = value.getAttribute("name")

                
                children = value.childNodes;
                if children:
                    map_value = value.childNodes[0].data
                    map_value = map_value.replace('&amp;', '&')
                else:
                    map_value = ""
                
                value_map[map_key] = map_value 
    
    
    return value_map




def grepStrings(projectDir):
	commandProjStr = f'find {projectDir} -name "*.java" |xargs cat  |grep -Hsn  "ToastUtils" --binary-files=without-match > grep1.txt'
	print("执行命令=>> " + commandProjStr)
	os.system(commandProjStr)

	commandProjStr = f'cat grep1.txt | grep "ToastUtils.show" > grep2.txt'
	print("执行命令=>> " + commandProjStr)
	os.system(commandProjStr)

	commandProjStr = f'cat grep2.txt | grep -nv "//" > grep3.txt'
	print("执行命令=>> " + commandProjStr)
	os.system(commandProjStr)

	commandProjStr = f'cat grep3.txt | grep  "R.string" > result.txt'
	print("执行命令=>> " + commandProjStr)
	os.system(commandProjStr)

def matchString(resultOut):
	with open('result.txt', mode='r', encoding='utf-8') as f:
		for line in f:
			# print(line.strip())
			# ret = line.find(r"R.string.");
			#
			# tmpStr = line[ret + 9:]
			# retEnd = tmpStr.find(")");
			#
			#
			# print(tmpStr)
			# print(ret)
			# print(retEnd)
			# print(tmpStr[0:retEnd])
			splitLines = line.split(":")

			for tmpLine in  splitLines:
				m = re.match(r'.*R\.string\.(.*)\).*', tmpLine)
				if not m:
					continue

				tmpResult = m.groups()[0].replace("))", "").replace(")", "")
				resultOut.append(tmpResult)
				# print(tmpResult)

			# # print(m.groups().count())
			# print( m.groups().__len__())
			# # print(m.groups()[0])

if __name__ == '__main__':
	projectDir = "/Users/lm188/AndroidStudioProjects/im_android"

	# grepStrings(projectDir)
	resultOut = []
	matchString(resultOut)

	stringsFielPath = "/Users/lm188/AndroidStudioProjects/im_android/BusinessLib/src/main/res/values/strings.xml"



	saveList =[]

	value_map = ParseXml(stringsFielPath)
	keys = value_map.keys();
	# for key, value in value_map.items():
	# 	if key in resultOut:
	# 		print(keyValue[key])
	for key in resultOut:
		if key in keys:
			# print(value_map[key])

			saveList.append(key)
		else:
			pass
			# print(key + "不存在")
	# print(keyValue)

	saveList =list(set(saveList))
	for vaule in saveList:
		print(vaule)












