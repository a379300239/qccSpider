import requests
import re
import settings

def get_companyList(companyName):

    url = "https://www.qcc.com/web/search?key={}".format(companyName)

    payload = ""
    headers = settings.headers

    response = requests.request("GET", url, headers=headers, data=payload)

    return response.text

# 利用正则，提取url
def get_url(html):
    return re.findall(r'href="https://www.qcc.com/firm/.*?\.html" ',html)[0][6:-1]

# 获取keyno 类似文章id 在文章页
def get_keyNo(html):
    return re.findall(r'href="https://www.qcc.com/firm/.*?\.html" ', html)[0][31:-7]

# 获取asyncJsCode 依靠这个值获取json
def get_asyncJsCode(infType,keyNo):
    url='https://www.qcc.com/{}/{}.html'.format(infType,keyNo)

    headers = {'Host': 'www.qcc.com',
               'Connection': 'keep-alive',
               'Cache-Control': 'max-age=0',
               'sec-ch-ua': '" Not;A Brand";v="99", "Google Chrome";v="91", "Chromium";v="91"',
               'sec-ch-ua-mobile': '?0',
               'Upgrade-Insecure-Requests': '1',
               'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36',
               'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
               'Sec-Fetch-Site': 'same-origin', 'Sec-Fetch-Mode': 'navigate', 'Sec-Fetch-User': '?1',
               'Sec-Fetch-Dest': 'document', 'Accept-Encoding': 'gzip, deflate, br',
               'Accept-Language': 'zh-CN,zh;q=0.9'}
    cookies = {'UM_distinctid': '17b04cef413570-075e38eceed43f-6373264-144000-17b04cef414e93',
               '_uab_collina': '162787327737821815847616',
               'zg_de1d1a35bfa24ce29bbf2c7eb17e6c4f': '%7B%22sid%22%3A%201627873277172%2C%22updated%22%3A%201627873592168%2C%22info%22%3A%201627873277174%2C%22superProperty%22%3A%20%22%7B%5C%22%E5%BA%94%E7%94%A8%E5%90%8D%E7%A7%B0%5C%22%3A%20%5C%22%E4%BC%81%E6%9F%A5%E6%9F%A5%E7%BD%91%E7%AB%99%5C%22%7D%22%2C%22platform%22%3A%20%22%7B%7D%22%2C%22utm%22%3A%20%22%7B%5C%22%24utm_source%5C%22%3A%20%5C%22baidu1%5C%22%2C%5C%22%24utm_medium%5C%22%3A%20%5C%22cpc%5C%22%2C%5C%22%24utm_term%5C%22%3A%20%5C%22pzsy%5C%22%7D%22%2C%22referrerDomain%22%3A%20%22www.baidu.com%22%2C%22cuid%22%3A%20%22undefined%22%7D',
               'qcc_did': '37c9a3b1-9d99-485e-b9ca-bba2c119c296', 'QCCSESSID': 'c19b2e919648587ffc3c632fcd',
               'CNZZDATA1254842228': '1718704341-1627871210-https%253A%252F%252Fwww.baidu.com%252F%7C1631347755',
               'MQCCSESSID': 'fv31cf2a3r0rop6j8afdr8vev5',
               'acw_tc': '701ec48f16313550005508132ed5d29d1dfb398a9968375279059dbd45',
               'zg_did': '%7B%22did%22%3A%20%2217b04cef4f15ee-0a87fbe33790a-6373264-144000-17b04cef4f28dd%22%7D',
               'zg_294c2ba1ecc244809c552f8f6fd2a440': '%7B%22sid%22%3A%201631344815547%2C%22updated%22%3A%201631355257468%2C%22info%22%3A%201630938385895%2C%22superProperty%22%3A%20%22%7B%5C%22%E5%BA%94%E7%94%A8%E5%90%8D%E7%A7%B0%5C%22%3A%20%5C%22%E4%BC%81%E6%9F%A5%E6%9F%A5%E7%BD%91%E7%AB%99%5C%22%7D%22%2C%22platform%22%3A%20%22%7B%7D%22%2C%22utm%22%3A%20%22%7B%7D%22%2C%22referrerDomain%22%3A%20%22%22%2C%22cuid%22%3A%20%22undefined%22%2C%22zs%22%3A%200%2C%22sc%22%3A%200%2C%22firstScreen%22%3A%201631344815547%7D'}
    data = {}

    response = requests.get(url, headers=headers, verify=False, cookies=cookies)

    # print(response.text)

    # 定位asyncCode
    find_res=re.findall(r'src="/web/async-js/.*?token',str(response.text))

    try:
        return find_res[0][19:-9]
    except:
        return 'no'

# 获得企业数据
def get_compantInf(asyncJsCode):
    url = "https://www.qcc.com/web/async-js/{}.js?token=bvtkhf9btpi2".format(asyncJsCode)

    payload = ""
    headers=settings.headers

    response = requests.request("GET", url, headers=headers, data=payload)

    return response.text[25:-122]

def get_tecList(keyno):
    url = "https://www.qcc.com/api/datalist/teclist?keyNo={}".format(keyno)

    payload = ""
    headers = {
  'Host': 'www.qcc.com',
  'Connection': 'keep-alive',
  'sec-ch-ua': '" Not;A Brand";v="99", "Google Chrome";v="91", "Chromium";v="91"',
  'Accept': 'application/json, text/plain, */*',
  'dd3e71487b629e680909': 'a0900276151d2012a1725d26aa525ad2a1a9ea7fbb07046fffeb298d761cb38dbbfdb74e738bfaa3d87c0802b290cef5e255a821f555fa8b99894ab9fb9d76da',
  'X-Requested-With': 'XMLHttpRequest',
  'sec-ch-ua-mobile': '?0',
  'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36',
  'Sec-Fetch-Site': 'same-origin',
  'Sec-Fetch-Mode': 'cors',
  'Sec-Fetch-Dest': 'empty',
  'Referer': 'https://www.qcc.com/creport/{}.html'.format(keyno),
  'Accept-Encoding': 'gzip, deflate, br',
  'Accept-Language': 'zh-CN,zh;q=0.9',
  'Cookie': settings.cookie
}

    response = requests.request("GET", url, headers=headers, data=payload)

    return response.text