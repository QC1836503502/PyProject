import re
import os
import numpy as np
from bs4 import BeautifulSoup
import requests
#选择目标网站进行爬取
def zqip():
    print("正在爬取IP,请等待")
    url = 'https://www.proxy-list.download/HTTP'
    get = requests.get(url)
    html = get.text
    #解析网站
    bf = BeautifulSoup(html)
    #筛选内容        屎堆
    text = bf.find_all('div',class_ = 'tbcontai col-sm-12')
    texta = text[0].text.replace('\xa0'*8,'\n\n')
    textaa = texta.strip('IP Address\nPort\nAnonymity\nCountry\nSpeed')
    textab = textaa.strip(" ")
    testlist = textab.split()
    testlista = "\r".join(testlist)
    read = re.sub('[a-zA-Z]','',testlista)
    #将内容写入文本
    f = open("IP.txt","w")
    a = re.sub('','',read)
    f.write(a)
    f.close()
    r = open("IP.txt","r")
    file2 = open("file2.txt","w")
    #删除空白行(代码来自博客网https://blog.csdn.net/zhe_ge_sha_shou/article/details/78919127)
    for line in r.readlines():
                if line == '\n':
                    line = line.strip("\n")
                file2.write(line)
    print("正在将IP写入文本")
    r.close()
    file2.close()
    #创建目录 来自https://cloud.tencent.com/developer/article/1406443
    print("检测是否存在输出目录")
    def mkdir(path):
        # 去除首位空格
        path=path.strip()
        # 去除尾部 \ 符号
        path=path.rstrip("\\")
        # 判断路径是否存在
        # 存在:True,  不存在:False
        isExists=os.path.exists(path)
        if not isExists:
            # 创建目录操作函数
            print("正在创建输出目录/export/")
            os.makedirs(path)

    # 定义要创建的目录
    mkpath="export"
    # 调用函数
    mkdir(mkpath)
    dq = open("file2.txt","r")
    xr = open("export/ip.txt","w")
    dk = open("export/port.txt","w")
    #开始进行ip prot组合
    for line in dq.readlines():
        if len(line)>7 or len(line)==5 or len(line)<=3:
            # xr.write(line)
            while True:
                if len(line)>8:
                    xr.write(line)
                if len(line)==5 or len(line) == 3:
                    dk.write(line)
                break
    xr.close()
    dq.close()
    dk.close()
    #删除不必要文件
    print("正在删除不必要文件")
    os.remove("file2.txt")
    os.remove("IP.txt")