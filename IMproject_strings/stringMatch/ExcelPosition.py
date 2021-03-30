#!/usr/bin/python
import os

# 用来匹配没有匹配到的字符串
import xlrd


def getAllList(allList):
	allFile = os.getcwd() + os.sep + '全字符串.txt'
	with open(allFile, "r", encoding="utf-8") as f:
		for line in f:
			allList.append(line.replace("\n", ""))

# 读取总表翻译的字符串表格式
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

    for rowIndex in range(0, rowTotal):
        value = sheet.cell(rowIndex, 2).value
        allList.append(value)
        # print(value)

    print("all Done.")
    return sheet


def realExcelByPosition(allSheet, allIndex):
	print(f"realExcelByPosition, index={index}")


	checkValue = allSheet.cell_value(allIndex, 2)
	print(f"checkValue={checkValue}")
	ftValue = allSheet.cell_value(allIndex, 3)
	print(f"ftValue={ftValue}")
	enValue = allSheet.cell_value(allIndex, 4)
	print(f"enValue={enValue}")




# sheet.write(0, col_index, col_name)

def matchPartString(allList, keyword):
	for str in allList:
		if keyword in str:
			print(f"str={str}")



if __name__ == '__main__':

	print("Begin write key,value to [string.xml] file....")

	allList = []
	androidList = []
	resultList = []

	# getAllList(allList)
	allSheet = readAllExcel(allList)

	while True:
		keyword = input('Enter versionName:')
		print("你输入的版本名是=" + keyword)
		if keyword == "exit":
			break;


		if keyword in allList:
			index = allList.index(keyword)
			if index > 0:
				print(f"找到位置是={index}, 对应的次是：{allList[index]}")
				realExcelByPosition(allSheet, index)

		else:
			print(f"没有找到找到位置")
			matchPartString(allList, keyword)

















