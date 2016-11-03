 # -*- coding: utf-8 -*- 

import requests
import time
import random
from bs4 import BeautifulSoup

def spider():
    headers_1 = {
        'Host': 'student.zucc.edu.cn',
        'Connection': 'keep-alive',
        'Pragma': 'no-cache',
        'Cache-Control': 'no-cache',
        'Upgrade-Insecure-Requests': '1',
        'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/53.0.2785.143 Safari/537.36',
        'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8',
        'Accept-Encoding': 'gzip, deflate, sdch, br',
        'Accept-Language': 'zh-CN,zh;q=0.8',
        'Cookie': 'JSESSIONID=0000tNym9mN7X6c00-yGuyCpPxA:184lrsfjg',
    }
    url_1 = 'http://student.zucc.edu.cn/index.portal'
    r1 = requests.get(url_1, headers = headers_1)
    print r1.headers
    print r1.text.encode('utf-8')
    # print r1.history
    # cookie = r1.headers['Set-Cookie'].split(';')[0]
    # print cookie

def main():
    spider()
    print 'done...'

if __name__ == "__main__":
    main()