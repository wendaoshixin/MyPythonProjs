#!/usr/bin/python  
#-*-coding:utf-8-*-

#keystore信息
#Windows 下路径分割线请注意使用\\转义
# keystorePath = "../PushLib/imTempKeystore.jks"
# keyAlias = "temp"
# keystorePassword = "8610086"
# keyPassword = "8610086"

keystorePath = "../PushLib/testKeystore.jks"
keyAlias = "fengli"
keystorePassword = "19841001"
keyPassword = "19841001"

#加固后的源文件名（未重签名）
protectedSourceApkName = "app_release_V1.0.4.20210128161245_10420210128161245_jiagu_sign.apk"
#加固后的源文件所在文件夹路径(...path),注意结尾不要带分隔符，默认在此文件夹根目录
protectedSourceApkDirPath = "../JiaguPlugin/jiaguApks"
#渠道包输出路径，默认在此文件夹Channels目录下
channelsOutputFilePath = "../JiaguPlugin/channels"
#渠道名配置文件路径，默认在此文件夹根目录
channelFilePath = ""
#额外信息配置文件（绝对路径，例如/Users/mac/Desktop/walle360/config.json）
#配置信息示例参看https://github.com/Meituan-Dianping/walle/blob/master/app/config.json
extraChannelFilePath = ""
#Android SDK buidtools path , please use above 25.0+
#替换成本机的SDK路径
#sdkBuildToolPath = "/Users/lm233/Library/Android/sdk/build-tools/28.0.2"
sdkBuildToolPath = "/Users/lm188/Library/Android/sdk/build-tools/28.0.3"
