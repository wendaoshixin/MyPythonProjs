#!/usr/bin/python
import os
from xml.dom.minidom import parse
import xml.dom.minidom
import xdrlib, xlrd
import sys
import xml.etree.ElementTree as ET

# 查询没有匹配的字符串


isNeedOverride = False			#如果需要覆盖原有的xml资源文件，请置为 True

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



def writeResourceXmlHeader(fd):
	if fd is None:
		return

	fd.write('<?xml version="1.0" encoding="utf-8"?>')
	fd.write('\n')
	fd.write('<resources>')
	fd.write('\n\n')


def writeResourceXmlFooter(fd):
	if fd is None:
		return

	fd.write('\n')
	fd.write('</resources>')
	fd.write('\n')


def createAndWriteString2XmlByLang(sheet, path, col):

	if len(path) <= 0 or sheet is None:
		return

	fd = open(path, 'w', encoding='utf-8')
	
	writeResourceXmlHeader(fd)

	rowTotal = sheet.nrows
	for i in range(1,rowTotal):
		key = sheet.cell(i,0).value
		value = sheet.cell(i,col).value

		value = value.replace('&amp;', '&')
		value = value.replace('&', '&amp;')
		
		line = '    <string name="' + key + '">' + value + '</string>' + '\n'

		fd.write(line)


	writeResourceXmlFooter(fd)

	fd.close()


def appendString2XmlByLang(sheet, path, col):

	if len(path) <= 0 or sheet is None:
		return

	keys = ParseKey(path)

	tmppath = path + '.tmp'

	fd2 = open(tmppath, 'w', encoding = 'utf-8')

	with open(path, 'rU', encoding = 'utf-8') as fd:	
		while(1):
			line = fd.readline()
			if not line:
				break

			ret = line.find('</resources>')
			if ret != -1:
				break

			fd2.write(line)

	#write new key,value
	rowTotal = sheet.nrows
	for i in range(1,rowTotal):
		key = sheet.cell(i, 0).value
		value = sheet.cell(i, col).value
		
		value = value.replace('&amp;', '&')
		value = value.replace('&', '&amp;')

		line = '    <string name="' + key + '">' + value + '</string>' + '\n'

		fd2.write(line)

	#write footer
	writeResourceXmlFooter(fd2)
	
	fd2.close()

	os.remove(path)
	os.rename(tmppath, path)
	


def start():

	#stringPath = os.getcwd() + os.sep + '../palmplay61/src/main' + os.sep + "res"
	stringPath = os.getcwd() + os.sep + 'res'

	excel_name = os.getcwd() + os.sep + 'strings.xls'

	if not os.path.exists(excel_name):
		print("file not exist!")
		return

	if not os.path.exists(stringPath):
		os.makedirs(stringPath)

	workbook = xlrd.open_workbook(excel_name)

	sheet = workbook.sheets()[0]
	if sheet is None:
		print("There is no strings in excel table.")
		return

	rowTotal = sheet.nrows
	colTotal = sheet.ncols

	rowsData = sheet.row_values(0)

	for col in range(1, colTotal):
		lang = sheet.cell(0, col).value
		if lang is None or len(lang) <= 0:
			continue

		folder = 'values'
		if lang.lower() != 'en':
			folder = folder + '-' + lang

		path = stringPath + os.sep + folder

		if not os.path.exists(path):
			os.makedirs(path)

		path = path + os.sep + 'strings.xml'

		if not os.path.exists(path):
			createAndWriteString2XmlByLang(sheet, path, col)
		else:
			if isNeedOverride:
				createAndWriteString2XmlByLang(sheet, path, col)
			else:
				appendString2XmlByLang(sheet, path, col)
			
		print('Language:[ ', folder, ' ] is write OK.')
			

	print('\nTotal Language is:', (colTotal-1))

	print('\n')

	print("Done.")


def readAllExcel(allList):


	excel_name = os.getcwd() + os.sep + 'IM项目多语言文档的副本.xlsx'

	if not os.path.exists(excel_name):
		print("file not exist!")
		return

	workbook = xlrd.open_workbook(excel_name)

	sheet = workbook.sheets()[0]
	if sheet is None:
		print("There is no strings in excel table.")
		return

	rowTotal = sheet.nrows
	colTotal = sheet.ncols

	rowsData = sheet.row_values(0)


	for rowIndex in range (0, rowTotal):
		value = sheet.cell(rowIndex, 2).value
		allList.append(value)
		print(value)

	print("Done.")

def readAndroidExcel(androidList):


	excel_name = os.getcwd() + os.sep + '即话Android精简后字符串.xlsx'

	if not os.path.exists(excel_name):
		print("file not exist!")
		return

	workbook = xlrd.open_workbook(excel_name)

	sheet = workbook.sheets()[0]
	if sheet is None:
		print("There is no strings in excel table.")
		return

	rowTotal = sheet.nrows
	colTotal = sheet.ncols

	rowsData = sheet.row_values(0)


	for rowIndex in range (0, rowTotal):
		value = sheet.cell(rowIndex, 1).value
		androidList.append(value)
		# print(value)

	print("Done.")

if __name__ == '__main__':

	print("Begin write key,value to [string.xml] file....")

	allList = []
	androidList = []
	resultList = []


	# start()
	readAllExcel(allList)
	readAndroidExcel(androidList)

	for androidItemStr in androidList:
		if androidItemStr in allList:
			resultList.append(androidItemStr)

	print(f"匹配的长度：{len(resultList)}")


	# count = 0
	# for androidItemStr in androidList:
	# 	if not androidItemStr in allList:
	# 		print(androidItemStr)
	# 		count = count+1
	# print(f"匹配不上的个数{count}")













