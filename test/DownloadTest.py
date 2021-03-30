#!/usr/bin/python
import httplib2 as httplib2

h = httplib2.Http()
url = 'https://docs.google.com/spreadsheets/d/1iCpuSqtXDPbPGLv_EQv59Djp9So49cutcYPQY6Dj80A/edit#gid=1529214590'
resp, content = h.request(url)
filename="字符串翻译.xlsx"
if resp['status'] == '200':
    with open(filename, 'wb') as f:
        f.write(content)




