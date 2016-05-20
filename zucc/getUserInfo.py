# -*- coding: utf-8 -*-

import requests
import urllib
import urllib2
from bs4 import BeautifulSoup
import os

#Url = 'http://10.61.2.3/(mqz143rkch0a4pm1rnkh5332)/xs_main.aspx?xh=31301368'
#Url为登陆后的url
global Url
global Session
global UserInfoUrl
global MainUrl

headers_get = {
    'User-Agent' : 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/48.0.2564.116 Safari/537.36'
}

def saveHtml(page):
    f = file('UserInfo.html', 'wb')
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
    
def getUserInfoUrl():
    global Url
    content = getData(Url, headers_get)
    soup = BeautifulSoup(content, "html.parser")
    url = Url.split(')/')[0] + ')/' + soup.find('a', {'onclick':"GetMc('个人信息');"}).get('href')
    return url
    
def getUserInfoPage():
    global UserInfoUrl
    global Session
    global MainUrl
    
    Session = getSession()
    UserInfoUrl = getUserInfoUrl()
    MainUrl = Url
    
    headers_getInfo = {
        'Accept' : 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
        'Referer' : MainUrl,
        'Accept-Language' : 'zh-CN,zh;q=0.8',
        'User-Agent' : 'Mozilla/5.0 (Windows NT 6.3; WOW64; rv:40.0) Gecko/20100101 Firefox/40.0',
        'Content-Type' : 'application/x-www-form-urlencoded',
        'Accept-Encoding' : 'gzip, deflate, sdch',
        'Host' : '10.61.2.3',
        'Connection' : 'Keep-Alive',
        'Upgrade-Insecure-Requests' : '1',
    }
    
    content = getData(UserInfoUrl, headers_getInfo)
    return content
    
def handleUserInfo(content):
    soup = BeautifulSoup(content, "html.parser")
    #学号 姓名 学院 专业名称 行政班
    xh = soup.find('span', {'id':'xh'}).text
    xm = soup.find('span', {'id':'xm'}).text
    lbl_xy = soup.find('span', {'id':'lbl_xy'}).text
    lbl_zymc = soup.find('span', {'id':'lbl_zymc'}).text
    lbl_xzb = soup.find('span', {'id':'lbl_xzb'}).text
    dict = {'xh':xh, 'xm':xm, 'lbl_xy':lbl_xy, 'lbl_zymc':lbl_zymc, 'lbl_xzb':lbl_xzb}
    return dict
    
def run(url):
    global Url
    Url = url
    dict = handleUserInfo(getUserInfoPage())

def main(url):
    global Url
    Url = url
    dict = handleUserInfo(getUserInfoPage())
    print dict

if __name__ == "__main__":
    main('http://10.61.2.3/(mqz143rkch0a4pm1rnkh5332)/xs_main.aspx?xh=31301368')
    

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
        'Referer' : UserInfoUrl,
        'Accept-Encoding' : 'gzip, deflate',
        'Accept-Language' : 'zh-CN,zh;q=0.8',
    }
    """