# -*- coding: utf-8 -*-

import requests
import urllib
import urllib2
from bs4 import BeautifulSoup
import os

#Url = 'http://10.61.2.3/(spsga3epy44l1r55ve1p5uzc)/xs_main.aspx?xh=31301368'
#Url为登陆后的url
global Url
global Session
global GradeUrl
global Viewstate

headers_get = {
    'User-Agent' : 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/48.0.2564.116 Safari/537.36'
}

def saveHtml(page):
    f = file('grade.html', 'wb')
    f.write(page)
    f.close()

def getData(url, headers):
    try:
        req = urllib2.Request(url, None, headers)
        content = urllib2.urlopen(req)
        return content.read()
    except urllib2.URLError,e:
        print 'error : ' + str(e.code) + ' ' + e.reason
        
def getSession():
    global Url
    return ''.join(Url.split('/')[-2:-1])[1:-1]
    
def getViewstate():
    global Url
    headers_getViewstate = {
        'Accept' : 'text/html, application/xhtml+xml, image/jxr, */*',
        'Referer' : Url,
        'Accept-Language' : 'zh-Hans-CN,zh-Hans;q=0.5',
        'User-Agent' : 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/46.0.2486.0 Safari/537.36 Edge/13.10586',
        'Accept-Encoding' : 'gzip, deflate',
        'Host' : '10.61.2.3',
        'Connection' : 'Keep-Alive',
    }
    url = getGradeUrl()
    r = requests.get(url, headers = headers_getViewstate)
    soup = BeautifulSoup(r.text, "html.parser")
    return soup.input.get('value')
    
def getGradeUrl():
    global Url
    content = getData(Url, headers_get)
    soup = BeautifulSoup(content, "html.parser")
    url = Url.split(')/')[0] + ')/' + soup.find('a', {'onclick':"GetMc('成绩查询');"}).get('href')
    return url
    
def getGradePage():
    global GradeUrl
    global Viewstate
    global Session
    Session = getSession()
    GradeUrl = getGradeUrl()
    Viewstate = getViewstate()
    
    postData = {
        '__VIEWSTATE' : Viewstate,
        'ddIXN' : '',
        'ddIXQ' : '',
        'Button2' : '%D4%DA%D0%A3%D1%A7%CF%B0%B3%C9%BC%A8%B2%E9%D1%AF',
    }
    #'\xD4\xDA\xD0\xA3\xD1\xA7\xCF\xB0\xB3\xC9\xBC\xA8\xB2\xE9\xD1\xAF'

    headers_post = {
        'Accept' : 'text/html, application/xhtml+xml, image/jxr, */*',
        'Referer' : GradeUrl,
        'Accept-Language' : 'zh-Hans-CN,zh-Hans;q=0.5',
        'User-Agent' : 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/46.0.2486.0 Safari/537.36 Edge/13.10586',
        'Content-Type' : 'application/x-www-form-urlencoded',
        'Accept-Encoding' : 'gzip, deflate',
        'Host' : '10.61.2.3',
        'Connection' : 'Keep-Alive',
        'Pragma' : 'no-cache',
    }
    
    r = requests.post(GradeUrl, data = postData, headers = headers_post)
    #编码为gb2312
    page = r.text.encode('gb2312')
    saveHtml(page)
    #print r.text

def run(url):
    global Url
    Url = url
    getGradePage()
    print 'getGradePage successful'

def main(url):
    global Url
    Url = url
    getGradePage()

if __name__ == "__main__":
    main()
    

#===========----------以后可能要用到的分割线----------===========   
    #chrome post请求的headers
    """
    headers_post = {
        'Host' : '10.61.2.3',
        'Connection' : 'keep-alive',
        'Cache-Control' : 'max-age=0',
        'Accept' : 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8',
        'Origin' : 'http://10.61.2.3',
        'Upgrade-Insecure-Requests' : '1',
        'User-Agent' : 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/48.0.2564.116 Safari/537.36',
        'Content-Type' : 'application/x-www-form-urlencoded',
        'Referer' : GradeUrl,
        'Accept-Encoding' : 'gzip, deflate',
        'Accept-Language' : 'zh-CN,zh;q=0.8',
    }
    """