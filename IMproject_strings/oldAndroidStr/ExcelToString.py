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



myWorkbook = xlrd.open_workbook('Strings.xlsx')

mySheet = myWorkbook.sheet_by_name(u'String')

nrows = mySheet.nrows
print("nrows=%d" % (nrows))

ncols = mySheet.ncols
print("ncols=%d" % (ncols))


country_list = []
titles = mySheet.row_values(0)
i=0
for country in titles:
	if i > 0:
		country_list.append(country)
		i=i+1
	
for cl in range(1, ncols):
	country = mySheet.cell_value(0, cl)
	print("countries is: %s" % (country))
	country_list.append(country)


def GetStringFileName(country):
	out_file =  "String_" + country + ".xml"
	print("begin to write xml header %s" % (out_file))
	return out_file



def WriteXmlHeader(pf_out):
	pf_out.write("<?xml version=\"1.0\" encoding=\"utf-8\"?>\n")
	pf_out.write("<resources>\n")
	pf_out.write("\n")
	
def WriteXmlFooter(pf_out):
	print("begin to write xml rooter")
	pf_out.write("\n\n</resources>")
	pf_out.close()
	
		
def WriteXml(pf_out, inKey, inValue):
	pf_out.write("<string name=\"")
	pf_out.write(inKey)
	pf_out.write("\">")
	pf_out.write(inValue)
	pf_out.write("</string>\n")
		
index=0

for country in country_list:
	fileName = GetStringFileName(country)
	pf_out = open(fileName, 'w', encoding='utf-8')
	#write header
	WriteXmlHeader(pf_out)

	index=index+1
	for row in range(1, nrows):
		#print("nrows=%d" % (row))
		myCellKey = mySheet.cell_value(row, 0)
		myCellValue = mySheet.cell_value(row, index)	
		dstCellValue=myCellValue
		
		WriteXml(pf_out, myCellKey, dstCellValue)
		
	#write footer
	WriteXmlFooter(pf_out)
	
	pf_out.close()
	
	



print("Success.")




    
    











