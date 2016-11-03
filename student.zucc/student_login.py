 # -*- coding: utf-8 -*- 

import requests
import time
import random

def getCookie(username, password):
    headers_0 = {
        'Host': 'ca.zucc.edu.cn',
        'Connection': 'keep-alive',
        'Pragma': 'no-cache',
        'Cache-Control': 'no-cache',
        'Upgrade-Insecure-Requests': '1',
        'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/53.0.2785.143 Safari/537.36',
        'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8',
        'Accept-Encoding': 'gzip, deflate, sdch, br',
        'Accept-Language': 'zh-CN,zh;q=0.8',
    }
    url_0 = 'http://ca.zucc.edu.cn/cas/login?service=http%3A%2F%2Fstudent.zucc.edu.cn%2Findex.portal'
    r0 = requests.get(url_0, headers = headers_0, allow_redirects=False)
    cookie = r0.headers['Set-Cookie'].split(';')[0]

    headers_1 = {
        'Host': 'ca.zucc.edu.cn',
        'Connection': 'keep-alive',
        'Pragma': 'no-cache',
        'Cache-Control': 'no-cache',
        'Upgrade-Insecure-Requests': '1',
        'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/53.0.2785.143 Safari/537.36',
        'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8',
        'Accept-Encoding': 'gzip, deflate, sdch, br',
        'Accept-Language': 'zh-CN,zh;q=0.8',
        'Cookie': cookie,
    }
    url_1 = 'http://ca.zucc.edu.cn/cas/login?service=http%3A%2F%2Fstudent.zucc.edu.cn%2Findex.portal'
    r1 = requests.get(url_1, headers = headers_1, allow_redirects=False)
    cookie = r1.headers['Set-Cookie'].split(';')[0]

    headers_2 = {
        'Host': 'ca.zucc.edu.cn',
        'Origin': 'http://ca.zucc.edu.cn',
        'Referer': 'http://ca.zucc.edu.cn/cas/login?service=http%3A%2F%2Fstudent.zucc.edu.cn%2Findex.portal',
        'Connection': 'keep-alive',
        'Pragma': 'no-cache',
        'Cache-Control': 'no-cache',
        'Upgrade-Insecure-Requests': '1',
        'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/53.0.2785.143 Safari/537.36',
        'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8',
        'Accept-Encoding': 'gzip, deflate, sdch, br',
        'Accept-Language': 'zh-CN,zh;q=0.8',
        'Cookie': cookie,
    }
    postData = {
        'authType':'0',
        'username':username,
        'password':password,
        'lt':'',
        'execution':'e2s1',
        '_eventId':'submit',
        'submit':'',
        'randomStr':'',
    }
    url_2 = 'http://ca.zucc.edu.cn/cas/login?service=http%3A%2F%2Fstudent.zucc.edu.cn%2Findex.portal'
    r2 = requests.post(url_2, headers = headers_2, data = postData, allow_redirects=False)

    headers_3 = {
        'Host': 'student.zucc.edu.cn',
        'Referer': 'http://ca.zucc.edu.cn/cas/login?service=http%3A%2F%2Fstudent.zucc.edu.cn%2Findex.portal',
        'Connection': 'keep-alive',
        'Pragma': 'no-cache',
        'Cache-Control': 'no-cache',
        'Upgrade-Insecure-Requests': '1',
        'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/53.0.2785.143 Safari/537.36',
        'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8',
        'Accept-Encoding': 'gzip, deflate, sdch, br',
        'Accept-Language': 'zh-CN,zh;q=0.8',
    }
    url_3 = r2.headers['Location']
    r3 = requests.post(url_3, headers = headers_3, allow_redirects=False)
    cookie = r3.headers['Set-Cookie'].split(';')[0]
    return cookie

def main():
    username = raw_input('username: ')
    print getCookie(username, password)

if __name__ == "__main__":
    main()