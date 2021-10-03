# 爬取qcc的数据

## url配置
	get_data/main.py
	asyncJsCode = get_asyncJsCode('cassets',keyNo) 把cassets替换成自己想要的页面

## 获取需要的数据
       try:
            for i in cmp['datalist']['weibolist']['data']:
                s='{}\t{}\t{}\t{}'.format(i['Name'],cmp['company']['companyDetail']['Name'], i['Tags'], i['Fans'])
                print(s)
                f.write( s+'\n' )
        except:
            noInfNum+=1
所有数据爬取完以后在format/find_jsonPath.py里配置需要的字段即可

## 找到jsonPath
如果无法确定自己要的数据的json位置，用find_path()来找就可以了