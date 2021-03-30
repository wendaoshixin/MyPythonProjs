import requests
import os
#账号配置信息
url = "https://upload.pgyer.com/apiv2/app/upload"
uKey = "your_ukey"
api_key="35a765942433e1652406448830bafeab"


apkPath ="/Users/lm188/AndroidStudioProjects/im_android_devlop/JiaguPlugin/channels/app_yunTest_V1.0.6.20210309162208_None.apk"
apkfile = {"file":open(apkPath,"rb")}
headers = {"enctype":"multipart/form-data"}
payload= {
    # "uKey":uKey,
    "_api_key":api_key,
    "buildInstallType":2,
    "buildPassword":"123456",
    "buildUpdateDescription":"云环境包\n版本号：1.0.6.20210309162208 \n  1.1.0.6全部功能\n 2.加固封板包",
    "buildName":"即话",
    "buildChannelShortcut":"IM_yunTest",
#     IM_yunTest

}

r = requests.post(url,data= payload,headers=headers,files = apkfile)
jsonResult = r.json()
print(jsonResult)

#保存二维码至本地
appQRCodeURL = jsonResult["data"]["buildQRCodeURL"]
print("appQRCodeURL: %s "%appQRCodeURL)

