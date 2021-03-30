#!/usr/bin/python
# -*- coding:utf-8 -*-
import os
import shutil


back_file_dir = "./replace_res"
# /home/liuzhi/AndroidStudioProjects_Test/PalmstoreNew685/PalmstoreNew6.8.5
porject_root_dir = "./"
mainMoudleName = "palmplay61"
allFileList = []
replaceFileMap = {}
replaceStrMap = {}

def initDir():
    global porject_root_dir
    # default_dir = "/home/liuzhi/AndroidStudioProjects_Test/PalmstoreNew685/PalmstoreNew6.8.5/palmplay61"
    # "/home/liuzhi/AndroidStudioProjects_Test/PalmstoreNew685/PalmstoreNew6.8.5/doc/改包名/rename_to_old_package.py"
    curDir = os.getcwd()
    print(curDir)

    parent_path = os.path.dirname(curDir)  # 获得d所在的目录,即d的父级目录
    # "/home/liuzhi/AndroidStudioProjects_Test/PalmstoreNew685/PalmstoreNew6.8.5"
    porject_root_dir = os.path.dirname(parent_path)  ##获得parent_path所在的目录即parent_path的父级目录
    print("android工程目录" + porject_root_dir)


def initReplaceStrMap():
    replaceStrMap["import com.transsnet.store.R;"] = "import com.hzay.market.R;"
    replaceStrMap["import com.transsnet.store.BuildConfig;"] = "import com.hzay.market.BuildConfig;"
    replaceStrMap["package=\"com.transsnet.store\""] = "package=\"com.hzay.market\""
    replaceStrMap["applicationId \"com.transsnet.store\""] = "applicationId \"com.hzay.market\""
    replaceStrMap["Android/data/com.transsnet.store/"] = "Android/data/com.hzay.market/"
    replaceStrMap["<string name=\"palmstore_package_name\" translatable=\"false\">com.transsnet.store</string>"] = "<string name=\"palmstore_package_name\" translatable=\"false\">com.hzay.market</string>"
    replaceStrMap["signingConfig signingConfigs.config"] = "signingConfig signingConfigs.oldconfig"

def FuncPathJoin(parent, dirname):
    return  parent+os.sep+dirname


def searchAllFiles(rootDir):

    for parent, dirnames, filenames in os.walk(rootDir):

        for filename in filenames:  # files in parent
            # if filename in RSmaliFilesList:
            #     continue
            if filename in replaceFileList:
                replaceFileMap[filename] = FuncPathJoin(parent, filename)

            if filename.endswith(".png"):
                continue
            elif filename.endswith(".jpg"):
                continue
            elif filename.endswith(".gif"):
                continue
            elif filename.endswith(".webp"):
                continue
            elif filename.endswith(".so"):
                continue
            elif filename.endswith(".apk"):
                continue
            elif filename.endswith(".jar"):
                continue
            elif filename.endswith(".aar"):
                continue
            # print("filename===========%s" % (filename))
            allFileList.append(FuncPathJoin(parent, filename))

        for dirname in dirnames:  # folders in parent
            if dirname == "build":
                continue
            tmpDir = FuncPathJoin(parent, dirname)
            # print(tmpDir)
            searchAllFiles(tmpDir)

        break

def alterFileRepaceStr(file):

    file_data = ""
    foundOldStr = False
    with open(file, "r", encoding="utf-8") as f:

        for line in f:

            line, result = repaceStr(line)
            file_data += line
            if(result):
                foundOldStr = True

    if foundOldStr:
        print("修改了文件　filename===========%s" % (file))
        with open(file, "w", encoding="utf-8") as f:
            f.write(file_data)

def repaceStr(lineStr):
    """
    替换字符串
    :param old_str:就字符串
    :param new_str:新字符串
    :return:
    """
    file_data = ""
    foundOldStr = False
    for old_str in replaceStrMap.keys():
        if old_str in lineStr:
            foundOldStr = True
            lineStr = lineStr.replace(old_str, replaceStrMap[old_str])
            break
    return lineStr, foundOldStr

# 拷贝旧的icon和google服务器josn文件
def moveConstResFile():
    for oldFileName in replaceFileMap.keys():
        shutil.copyfile(back_file_dir+os.sep+oldFileName, replaceFileMap[oldFileName])


def reNameVersionInfo():
    mainMoudleBuildGradle = "/home/liuzhi/AndroidStudioProjects_Test/PalmstoreNew685/palmplay61/build.gradle"
    # mainMoudleBuildGradle = porject_root_dir + os.sep + mainMoudleName + os.sep + "build.gradle"
    versionCode = input('Enter versionCode:\n')
    if type(eval(versionCode)) != int:
        print("版本好必须是整数")
    print("你输入的版本号是=" + versionCode)

    versionName = input('Enter versionName:\n')
    print("你输入的版本名是=" + versionName)

    # "versionCode 1004"
    # "versionName \"6.8.5\""
    # 版本信息的前一行
    versionPreLineStr = "targetSdkVersion rootProject.ext.android.targetSdkVersion"

    file_data = ""
    foundVersionCode = False
    foundVersionName = False

    with open(mainMoudleBuildGradle, "r", encoding="utf-8") as f:
        for line in f:
            if (foundVersionCode):
                foundVersionCode = False
                foundVersionName = True
                # line = line.replace(old_str, new_str)
                splitLines = line.split("versionCode")
                line = splitLines[0] + "versionCode " + versionCode + "\n"
                # print(line.split("versionCode"))
                print(line)
            elif foundVersionName:
                foundVersionName = False
                # line = line.replace(old_str, new_str)
                splitLines = line.split("versionName")
                line = splitLines[0] + "versionName " + '"{first}"'.format(first=versionName) + "\n"
                # print(line.split("versionName"))
                print(line)

            elif versionPreLineStr in line:
                foundVersionCode = True

            file_data += line

    with open(mainMoudleBuildGradle, "w", encoding="utf-8") as f:
        f.write(file_data)

# 打包功能
def excPackageCmd():
    cmdFileName = "gradlew"
    cmdFullPath = porject_root_dir + os.sep + cmdFileName
    cmd = "cd " + porject_root_dir
    result = os.popen(cmd)
    res = result.read()
    for line in res.splitlines():
        print(line)
    cmd = "chmod +x " + cmdFullPath
    result = os.popen(cmd)
    res = result.read()
    for line in res.splitlines():
        print(line)

    # cmd = "cd " + porject_root_dir + "\n" + cmdFullPath + " assembleRelease"
    cmd = "cd " + porject_root_dir + "\n" + cmdFullPath + " assembleTranssionNewRelease"

    os.system(cmd)

if __name__ == '__main__':

    print("***************开始***************")
    #初始化目录
    initDir()
    #初始化, 替换字符串映射关系
    initReplaceStrMap()
    replaceFileList = os.listdir(back_file_dir)

    searchRootPath = porject_root_dir + os.sep + mainMoudleName
    searchAllFiles(searchRootPath)
    print("定位到的模块目录: " + searchRootPath)
    
    print(replaceFileList)
    print(replaceFileMap)

    # 替换字符串
    print("***************替换字符串***************")
    print(allFileList)
    for file in allFileList:

        alterFileRepaceStr(file)

    # 替换文件
    moveConstResFile()

    # 输入新版本号和名称,用于执行打包
    reNameVersionInfo()

    # 执行打包
    print("***************执行打包***************")
    excPackageCmd()