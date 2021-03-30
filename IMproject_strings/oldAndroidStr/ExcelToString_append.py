#!/usr/bin/python

import sys


import os
from xml.dom.minidom import parse
import xml.dom.minidom
import xdrlib, xlwt, xlrd
import struct
import math
import re
import string
import shutil 


isFileExist=False
isSpecialStrExist = False


out_folder=""
cur_dir = os.getcwd()
out_dir=cur_dir + "\\" + out_folder


#open xlsx file,read sheet,rows,and cols
myWorkbook = xlrd.open_workbook('Strings.xlsx')

mySheet =myWorkbook.sheets()[0] #myWorkbook.sheet_by_name(u'String')

nrows = mySheet.nrows
print("nrows=%d" % (nrows))

ncols = mySheet.ncols
print("ncols=%d" % (ncols))


#get file path
def GetOutFileFullPath(country) :
	tmpFold=""
	lowerCountry=str.lower(country)
	print("lowerCountry is: %s" % (lowerCountry))
	if lowerCountry == "en" :
		tmpFold=""
		print("-----is equal:%s" % (country))
	else :
		tmpFold="-" + country
		
	out_folder="values" + tmpFold

	if not os.path.exists(out_folder) :
		os.system("md " + out_folder)
		print("out_folder=%s" % (out_folder))

	out_path=out_folder + "\\" + "strings.xml"
	
	return out_path
	



#get country by read row 0 begin
country_list = []
for cl in range(1, ncols):
	country = mySheet.cell_value(0, cl)
	print("countries is: %s" % (country))
	country_list.append(country)
#get country by read row 0 end


#get dst string file name begin
def GetStringFileName(country):
	out_file = out_folder + "\\" + "String_" + country + ".xml"
	#print("begin to write xml header %s" % (out_file))
	return out_file
#get dst string file name end


#write to xml begin
def WriteXmlHeader(pf_out):
	pf_out.write("<?xml version=\"1.0\" encoding=\"utf-8\"?>\n")
	pf_out.write("<resources>\n")
	pf_out.write("\n")
	
def WriteXmlFooter(pf_out):
	#print("begin to write xml rooter")
	pf_out.write("\n\n</resources>")
	pf_out.close()
	
		
def WriteXml(pf_out, inKey, inValue):
	pf_out.write("<string name=\"")
	pf_out.write(inKey)
	pf_out.write("\">")
	pf_out.write(inValue)
	pf_out.write("</string>\n")
	

def WriteContent(pf_out, nrows, isWriteHeader, idx):
	
	if isWriteHeader :
		#write header
		WriteXmlHeader(pf_out)

	for row in range(1, nrows):
		#print("nrows=%d" % (row))
		myCellKey = mySheet.cell_value(row, 0)
		myCellValue = mySheet.cell_value(row, idx)	
		dstCellValue=myCellValue
		
		WriteXml(pf_out, myCellKey, dstCellValue)
		
	#write footer
	WriteXmlFooter(pf_out)
	
#write to xml end



index=0

tmpFileName= out_dir + "\\" + "String_tmp.xml"
for country in country_list:
	fileName = GetOutFileFullPath(country)
	if os.path.exists(fileName):
		isFileExist = True
	else:
		isFileExist = False
		
	print("isFileExist:%d" % (isFileExist))

	index = index + 1
	if isFileExist :
		pf_out = open(fileName, "r", encoding="utf-8")
		
		tmp_file=open(tmpFileName, "w", encoding="utf-8")
		for line in pf_out.readlines():
			if "</resources>" not in line:
				tmp_file.write(line)
				
		tmp_file.close()
		pf_out.close()
		shutil.move(tmpFileName, fileName)
		
		pf_out = open(fileName, "a+", encoding="utf-8")
		
		WriteContent(pf_out, nrows, False, index)
	
	else :
		pf_out = open(fileName, "w", encoding="utf-8")
		WriteContent(pf_out, nrows, True, index)

	pf_out.close()
	print("Export to file [%s] success" % (fileName))	



print("\n")
print("Done.")




    
    











