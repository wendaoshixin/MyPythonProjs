import zipfile, os
# -*- coding:utf-8 -*-
# from zipfile import  PyZipFile
# https://blog.csdn.net/dou_being/article/details/81546172
def get_zip_file(input_path, result):
    """
    对目录进行深度优先遍历# -*- coding:utf-8 -*-
    :param input_path:
    :param result:
    :return:
    """
    files = os.listdir(input_path)
    for file in files:
        if os.path.isdir(input_path + '/' + file):
            get_zip_file(input_path + '/' + file, result)
        else:
            result.append(input_path + '/' + file)


def zip_file_path(input_path, output_path, output_name):
    """
    压缩文件，相对路径
    :param input_path: 压缩的文件夹路径
    :param output_path: 解压（输出）的路径
    :param output_name: 压缩包名称
    :return:
    """
    f = zipfile.ZipFile(output_path + '/' + output_name, 'w', zipfile.ZIP_DEFLATED)
    filelists = []
    get_zip_file(input_path, filelists)
    for file in filelists:
        f.write(file)
    # 调用了close方法才会保证完成压缩
    f.close()
    return output_path + r"/" + output_name


def zip_file_abspath(abspath, output_name, cust_output=''):
    '''
        压缩绝对路径
        :param abspath:         压缩的文件夹的绝对路径
        :param cust_output:     输出路径  可选
        :param output_name:     输出文件名
        :return:		        压缩文件的保存路径。
    '''
    # path=R'C:\Users\Administrator.PC-20190202ENDJ\Desktop\aa\a'
    path = abspath
    os.chdir(path)
    output_path = os.path.abspath(os.path.join(os.getcwd(), ".."))
    os.chdir(output_path)
    for i in os.listdir():
        if i == path.split('\\')[-1] or i == path.split('/')[-1]:
            input_path = '.\\' + i
            if cust_output != '':
                return zip_file_abspath(input_path, cust_output, output_name)
            else:
                return zip_file_path(input_path, output_path, output_name)


# 1.由于用extractall遇到中文有机会乱码
# 2.整体思路是：一个一个提取，并用正确文件名命名。
def extract_file(zip_path, out_path):
    '''
    解压缩文件到指定目录
    '''
    import os
    path = out_path
    zfile = zipfile.ZipFile(zip_path)
    for f in zfile.namelist():
        # 防止中文乱码
        try:
            f1 = f.encode('cp437').decode('gbk')
        except Exception as e:
            f1 = f.encode('utf-8').decode('utf-8')
        zfile.extract(f, path)
        os.chdir(path)  # 切换到目标目录
        os.rename(f, f1)


if __name__ == '__main__':
    # demo
    path = R'D:\projects_workspace\Visual Studio 2019\venus_new_git\01_AndroidBox\AndroidBox_Dbg'
    print(zip_file_abspath(path,'234.rar'))
    # print(zip_file_abspath(path,'234.zip'))
    # print(zip_file_abspath(path,'234.gz'))

    # print(zip_file_path(r"./testing", 'F:', '123.rar'))
    # print(zip_file_path(r"./testing", 'F:', '123.zip'))
    # print(zip_file_path(r"./testing", 'F:', '123.gz'))

    # extract_file(R'C:\Users\Administrator.PC-20190202ENDJ\Desktop\aa\234.zip',R'C:\Users\Administrator.PC-20190202ENDJ\Desktop\aa\231')
    # extract_file(R'C:\Users\Administrator.PC-20190202ENDJ\Desktop\aa\234.gz',R'C:\Users\Administrator.PC-20190202ENDJ\Desktop\aa\232')
    # extract_file(R'C:\Users\Administrator.PC-20190202ENDJ\Desktop\aa\234.rar',R'C:\Users\Administrator.PC-20190202ENDJ\Desktop\aa\233')

    # 压缩单个文件：
    # 	直接用zipfile 就可以了

# https://www.cnblogs.com/yaoshen/p/8671344.html
# https://blog.csdn.net/dou_being/article/details/81546172
# https://blog.csdn.net/ZenG_xiangt/article/details/81869177
# 获取上层目录
# https://www.cnblogs.com/xiyuan2016/p/9187695.html