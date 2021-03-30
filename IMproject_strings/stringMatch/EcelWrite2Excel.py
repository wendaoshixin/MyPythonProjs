#!/usr/bin/python
import os
from xml.dom.minidom import parse
import xml.dom.minidom
import xdrlib, xlwt

import xlrd

# 从总表过滤出来字符串，依赖在线表格式

def write_excel(resultSheet,allSheet, androidSheet, resultIndex, allIndex, androidIndex):
    print(f"write_excel")
    key = androidSheet.cell_value(androidIndex, 0)
    print(f"key={key}")
    zwValue = androidSheet.cell_value(androidIndex, 1)
    print(f"zwValue={zwValue}")
    ftValue = allSheet.cell_value(allIndex, 3)
    print(f"ftValue={ftValue}")
    enValue = allSheet.cell_value(allIndex, 4)
    print(f"enValue={enValue}")
    checkValue = allSheet.cell_value(allIndex, 2)
    print(f"checkValue={checkValue}")

    # sheet.cell(rowIndex, 1).value
    resultSheet.write(resultIndex, 0,key)
    resultSheet.write(resultIndex, 1, zwValue)
    resultSheet.write(resultIndex, 2, ftValue)
    resultSheet.write(resultIndex, 3, enValue)
    resultSheet.write(resultIndex, 4, checkValue)
    # sheet.write(0, col_index, col_name)
    #
    # for i in range(0, len(keys)):
    #     key = list(keys)[i]
    #     value = value_map[key]
    #     if not value:
    #         value = ""
    #
    #     sheet.write((i + 1), col_index, value)




# 读取总表翻译的字符串表格式
def readAllExcel(allList):
    excel_name = os.getcwd() + os.sep + 'IM项目多语言文档2021022302.xlsx'
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

    for rowIndex in range(0, rowTotal):
        value = sheet.cell(rowIndex, 2).value
        allList.append(value)
        # print(value)

    print("all Done.")
    return sheet


def readAndroidExcel(androidList):
    excel_name = os.getcwd() + os.sep + 'IM项目多语言文档2021022302.xlsx'
    # excel_name = "/Users/lm188/PycharmProjects/untitled/IMproject_strings/new/strings2021012601.xlsx"
    if not os.path.exists(excel_name):
        print("file not exist!")

    workbook = xlrd.open_workbook(excel_name)



    sheet = workbook.sheets()[5]
    # sheet = workbook.sheets()[0]
    if sheet is None:
        print("There is no strings in excel table.")

    rowTotal = sheet.nrows
    colTotal = sheet.ncols
    rowsData = sheet.row_values(0)

    for rowIndex in range(0, rowTotal):
        value = sheet.cell(rowIndex, 1).value
        androidList.append(value)
        print(value)
    print("android Done.")
    return sheet

def writeExcelNotMatch(resultSheet, androidSheet, resultIndex, androidIndex):
    print(f"writeExcelNotMatch, resultIndex={resultIndex}, androidIndex={androidIndex}")
    key = androidSheet.cell_value(androidIndex, 0)
    print(f"key={key}")
    zwValue = androidSheet.cell_value(androidIndex, 1)
    # sheet.cell(rowIndex, 1).value
    resultSheet.write(resultIndex, 0,key)
    resultSheet.write(resultIndex, 1, zwValue)

def creatExcel():
    print("Auto gen Excel from string value in res folder")

    excel_name = "对比后的Strings2021022302.xlsx"

    try:
        os.remove(excel_name)
    except:
        print("file not exist!")

    excel_file = xlwt.Workbook()
    sheet = excel_file.add_sheet(u'String', cell_overwrite_ok=True)
    return sheet, excel_file, excel_name

def saveExcel(excel_file ,excel_name):
    excel_file.save(excel_name)
    print("保存excel文件")

if __name__ == '__main__':
    print(f"开始对比字符串 [string.xml] file....")

    allList = []
    androidList = []
    unMatchIndexList = []
    unMatchStringList = []

    # genExcel()
    allSheet = readAllExcel(allList)
    androidSheet = readAndroidExcel(androidList)

    resultSheet, excel_file, excel_name =creatExcel()

    resultIndex=0
    androidIndex=0
    for androidIndex in range(1, len(androidList)):
        androidItemStr = androidList[androidIndex]
        if androidItemStr in allList:
            allIndex = allList.index(androidItemStr)
            if allIndex > 0:
                resultIndex = resultIndex + 1
                print(f"androidItemStr={androidItemStr},androidIndex={androidIndex}, allIndex={allIndex}, resultIndex={resultIndex}")
                write_excel(resultSheet,allSheet, androidSheet, resultIndex, allIndex, androidIndex)
        else:
            unMatchIndexList.append(androidIndex)
            unMatchStringList.append(androidItemStr)




    for i in range(0, len(unMatchIndexList)):
        resultIndex = resultIndex + 1
        androidIndex = unMatchIndexList[i]
        print(f'不匹配第{androidIndex + 1}行: {unMatchStringList[i]}')
        writeExcelNotMatch(resultSheet, androidSheet, resultIndex, androidIndex)


    saveExcel(excel_file, excel_name)