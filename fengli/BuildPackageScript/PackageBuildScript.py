#!/usr/bin/python
# -*- coding:utf-8 -*-
import datetime
import os
import re
import shutil

from ProjectConfigModify import checkServerTypeModifyMacro, getIntputNewVersionThenModify
from ZipPackage import zip_file_abspath

# 判断失败的个数，如果非0.返回True，其他返回False
# ========== 生成: 成功 3 个，失败 0 个，最新 3 个，跳过 0 个 ==========
def getErrorCount(resultLines):
    ret = 0
    for line in resultLines:
        print(line)
        versionList = re.findall(r"^==========.*==========$", line)
        if versionList:
            countList = re.findall(r"[0-9]\d*", versionList[0])
            if countList and len(countList) == 4:
                errorCount = int(countList[1])
                if errorCount > 0:
                    print(f"编译出现了{errorCount}个错误")
                    ret = errorCount

    return  ret

# 清理解决方案
#devenv SolutionName / Clean
def clean_solution(solutionFullPath):
    #devenv SolutionName / Clean
    commandProjStr = f'devenv "{solutionFullPath}" /Clean {SolnConfigName}'
    print("编译工程 命令=>> " + commandProjStr)
    os.system(commandProjStr)

# 单独编译一个项目
# devenv "%USERPROFILE%\source\repos\MySolution.sln" /build Debug /project "CSharpWinApp\CSharpWinApp.csproj" /projectconfig Debug
def build_project(solutionFullPath, projectName):
    isError = False
    print("开始编译项目 ...." + projectName)
    projectRelativePath = f'{projectName}\{projectName}.csproj'
    commandProjStr = f'devenv "{solutionFullPath}" /build {SolnConfigName} /project "{projectRelativePath}" /projectconfig {SolnConfigName}'
    print("编译工程 项目 命令=>> " + commandProjStr)
    # result = os.system(commandProjStr)
    cmdOutLines = os.popen(commandProjStr)
    return getErrorCount(cmdOutLines)

def checkServerTypeAndModify(serverProjectConfigFilePath, isTestServerFlag):

    checkServerTypeModifyMacro(serverProjectConfigFilePath, isTestServerFlag)
    return

def deleteFilesBeforZip(zipDir):
    currDirPath = zipDir
    files = os.listdir(currDirPath)
    deleteDirs = {"Exts","Logs","app.publish","UpdateClient_temp"}
    deleteExcludeFiles = {"AndroidBox.Gui.exe", "AndroidBox.Gui.exe.config"}
    for name in files:
        fileFullPath = os.path.join(currDirPath, name)
        if os.path.isfile(fileFullPath):

            if(not name in deleteExcludeFiles):
                os.remove(fileFullPath)
                print("删除文件：" + fileFullPath)
        elif os.path.isdir(fileFullPath):

            if ( name in deleteDirs):
                shutil.rmtree(fileFullPath)
                print("删除目录：" + fileFullPath)


    # store目录清理，除了ToolApks.xml文件和Tools目录
    storeExcludeFiles = {"ToolApks.xml"}
    storeExcludeDirs = {"Tools"}
    currDirPath = os.path.join(zipDir, "store")
    files = os.listdir(currDirPath)
    for name in files:
        fileFullPath = os.path.join(currDirPath, name)
        if os.path.isfile(fileFullPath):
            if (not name in storeExcludeFiles):
                os.remove(fileFullPath)
                print("删除文件：" + fileFullPath)
        elif os.path.isdir(fileFullPath):
            if (not name in storeExcludeDirs):
                shutil.rmtree(fileFullPath)
                print("删除目录：" + fileFullPath)
    pass

if __name__ == '__main__':

    solutionName = "AndroidBox.sln"
    build_outputDirName = "AndroidBox_Dbg"
    SolnConfigName = "Debug|Win32"
    solutionDir = ""
    curDir = os.getcwd()
    print("当前目录=  " + curDir)
    solutionDir = os.path.dirname(curDir)  # 获得d所在的目录,即d的父级目录
    print("工程目录=" + solutionDir)
    # 解決方案绝对路径
    solutionFullPath = solutionDir + os.sep + solutionName
    # 输出压缩包前缀
    zipFileNamePrefix = "正式服务器"
    project_sort_list = [
        "UpdateClient",
        "AndroidBox.Logging",
        "AndroidBox.Basic",
        "AndroidBox.OpenFramework",
        "AndroidBox.Services",
        "AndroidBox.ApkInstaller",
        "AndroidBox.Gui"]

    inputCase = int(input("""
    选择执行编译打包选项如下：
        1.编译debug版本，测试服务器的包
        2.编译debug版本，正式服务器的包
        3.编译release版本，测试服务器的包
        4.编译release版本，正式服务器的包
    请输入你想要执行选项前的数字："""))

    isDebug = False
    isTestServer = False
    if inputCase <= 0 or inputCase > 4:
        print("你输入选项非法")
        exit(0)
    elif inputCase == 1:
        isDebug = True
        isTestServer = True
    elif inputCase == 2:
        isDebug = True
        isTestServer = False
    elif inputCase == 3:
        isDebug = False
        isTestServer = True
    elif inputCase == 4:
        isDebug = False
        isTestServer = False

    if isDebug:
        build_outputDirName = "AndroidBox_Dbg"
        SolnConfigName = "Debug"
    else:
        build_outputDirName = "AndroidBox_Rls"
        SolnConfigName = "Release"

    if isTestServer:
        zipFileNamePrefix = "TServer"
    else:
        zipFileNamePrefix = "RServer"

    # 修改版本号，输入非法为默认不修改版本号继续编译
    buildVersion = getIntputNewVersionThenModify(solutionDir + os.sep + "AndroidBox.Gui"+ os.sep +"Properties" + os.sep + "AssemblyInfo.cs")

    #修改服务器类型的宏定义：测试服务器 or 正式服务器
    checkServerTypeAndModify(solutionDir + os.sep + "AndroidBox.Services" + os.sep + "AndroidBox.Services.csproj", isTestServer)

    #清理解决方案
    clean_solution(solutionFullPath)
    #逐个项目编译
    for projectName in project_sort_list:
        errorCount = build_project(solutionFullPath, projectName)
        if errorCount > 0:
            print("编译出错，请检查项目配置情况")
            exit(0)
            break;

    #压缩编译结果
    build_outputDir_fullpath = solutionDir + os.sep + build_outputDirName
    # 清理掉多余的目录和文件
    deleteFilesBeforZip(build_outputDir_fullpath)

    dt = datetime.datetime.now().strftime('%Y%m%d%H%M%S')
    zipOutputFile = f'{build_outputDirName}_V{buildVersion}_{zipFileNamePrefix}_{dt}.zip'
    print("压缩目录=" + build_outputDir_fullpath)
    print("压缩结果文件=" + zipOutputFile)
    print(zip_file_abspath(build_outputDir_fullpath, zipOutputFile))






