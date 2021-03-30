import json
import os

import xlrd

def jsonTest():
    json_str = {'key1': 'value1', 'key2': 'value2'}

    # 写入文件
    # 可以通过json包，将json串（可以是字符串类型、字典类型、json类型）直接写入到文件中
    with open('something.json', "w") as sjw:
        json.dump(json_str, sjw)

    # 读取文件
    data = open("country.json", encoding='utf-8')
    json_read = json.load(data)
    # print(json_read)

    for country in json_read:
        print(f"{country['cn']}")

    print(f"长度：{len(json_read)}")
    # json_read.close()

def readCountryJson():
    # 读取文件
    data = open("country.json", encoding='utf-8')
    json_read = json.load(data)
    # print(json_read)

    # for country in json_read:
    #     print(f"{country['cn']}")

    return json_read

def readCountryExcel():
    countryList = []
    fantiList =[]
    enList = []
    codeList=[]
    excel_name = os.getcwd() + os.sep + '国家在线表.xlsx'
    if not os.path.exists(excel_name):
        print("file not exist!")

    workbook = xlrd.open_workbook(excel_name)

    sheet = workbook.sheets()[2]
    if sheet is None:
        print("There is no strings in excel table.")

    rowTotal = sheet.nrows

    for rowIndex in range(1, rowTotal):
        value = sheet.cell(rowIndex, 0).value
        countryList.append(value)
        fantiList.append(sheet.cell(rowIndex, 1).value)
        enList.append(sheet.cell(rowIndex, 2).value)
        codeList.append(sheet.cell(rowIndex, 3).value)
        # print(value)
    print(f"表格长度：{len(countryList)}")
    return countryList, fantiList, enList, codeList

# {
#     "cn": "也门",
#     "en": "Yemen",
#     "phone_code": "967"
#   },
def writeJson():
    valueMapList = []
    for i in range(0, len(codeList)):
        tempMap = {}
        tempMap["cn"] = countryList[i]
        tempMap["tw"] = fantiList[i]
        tempMap["en"] = enList[i]
        tempMap["phone_code"] = int(codeList[i])
        valueMapList.append(tempMap)

    with open('生成country.json', "w", encoding='utf-8') as sjw:
        json.dump(valueMapList, sjw,ensure_ascii=False,indent=4)




if __name__ == '__main__':
    print(f"开始对比字符串 [string.xml] file....")
    countryList, fantiList, enList,codeList = readCountryExcel()

    # json_read = readCountryJson()
    #
    # for i in range(0, len(json_read)):
    #     if json_read[i]['cn'] == countryList[i]:
    #         # pass
    #         print(f"相等数据：{countryList[i]}")
    #     else:
    #         print(f"不相等的数据：{countryList[i]}")
    writeJson()


