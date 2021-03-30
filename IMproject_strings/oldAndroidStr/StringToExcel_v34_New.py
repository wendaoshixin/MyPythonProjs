#!/usr/bin/python
import os
from xml.dom.minidom import parse
import xml.dom.minidom
import xdrlib, xlwt

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


def write_excel(sheet, keys, value_map, col_index, col_name):
    
    sheet.write(0, col_index, col_name)
    
    for i in range(0, len(keys)):
        key = list(keys)[i]
        value = value_map[key]
        if not value:
            value = ""
        
        sheet.write((i+1), col_index, value)
        
        
        



print("Auto gen Excel from string value in res folder")

excel_name = "res\\string.xls" 

try:
    os.remove(excel_name)
except:
    print("file not exist!")

valueFiles = os.listdir("res")

print(valueFiles)

map_list = []

string_keys = []




    

excel_file = xlwt.Workbook()

sheet = excel_file.add_sheet(u'String', cell_overwrite_ok=True)

col_index = 0


for file_name in valueFiles:
    
    if not file_name.endswith(".xml"):
        continue
    
    
    value_map = ParseXml("res" + "\\" + file_name)
    map_list.append(value_map)

    if file_name == "strings.xml":
        string_keys = value_map.keys()
        
        sheet.write(0, col_index, "Language")
        
        for i in range(0, len(string_keys)):

            key = list(string_keys)[i]
        
            sheet.write((i+1), col_index, key)

       
       
        col_index += 1   
      
    col_name = file_name[len("strings"):-len(".xml")]
    
    if  len(col_name) <= 0:
        col_name = "en"
    
    write_excel(sheet, string_keys, value_map, col_index, col_name)
    
    col_index += 1   
    

excel_file.save(excel_name);


print("Done.")





    
    











