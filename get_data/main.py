import time

from get_inf import *
from settings import dividech

if __name__=='__main__':
    # 获取爬取内容
    companyList=[]
    with open('companyList.txt','r',encoding='utf-8') as rfile:
        companyList=rfile.read()
        companyList=companyList.split('\n')

    # 爬取的数据存放在data.txt中
    with open('data.txt','w') as wfile:
        wfile.write('')

    fsave=open('data.txt','a+')

    for companyName in companyList:
        try:
            # 获取公司列表
            companyList = get_companyList(companyName)

            # 获取公司url
            keyNo = get_keyNo(companyList)

            # 在这里修改要爬取的内容
            asyncJsCode = get_asyncJsCode('cassets',keyNo)

            companyInf = get_compantInf(asyncJsCode)

            fsave.write(companyInf)
            fsave.write(dividech)

            print('成功爬取{}'.format(companyName))

            time.sleep(3)
        except:
            with open('erro.txt','a+') as ferro:
                ferro.write(companyName + '\n')
            print('爬取{}时出错！！！！！！！'.format(companyName))

    fsave.close()
