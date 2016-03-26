# -*- coding: utf-8 -*-

import urllib
import urllib2
from bs4 import BeautifulSoup
import os
import time
import shutil
from threading import Thread
import random
from Queue import Queue
from time import sleep

#用以下两行code模拟浏览器 被403 forbidden
#user_agent = 'Mozilla/4.0 (compatible; MSIE 5.5; Windows NT)'
#headers = {'User-Agent' : user_agent }
#神tm多加了点浏览器暂时用一用Orz
#headers = {'User-Agent':'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/31.0.1650.63 Safari/537.36'}
headers = {'User-Agent':'Mozilla/5.0 (Windows; U; Windows NT 6.1; en-US; rv:1.9.1.6) Gecko/20091201 Firefox/3.5.6'}

def getData(url):
    try:
        req = urllib2.Request(url, None, headers)
        content = urllib2.urlopen(req)
        return content.read()
    #except urllib2.URLError,e:
        #print 'error : ' + str(e.code) + ' ' + e.reason
    except urllib2.HTTPError, e:
        print e.code
    except urllib2.URLError, e:
        print e.args
        
def getImgList(page):
    #pic - 无聊图 ooxx - 妹子图
    url = 'http://jandan.net/pic/'
    url = url + 'page-' + str(page) + '#comments'
    #print 'url : ' + url
    
    content = getData(url)
    soup = BeautifulSoup(content, "html.parser")
    
    imgs = soup.find_all('img')
    imgList = []
    for img in imgs:
        #print 'find out ' + img['src']
        if(cmp(img['src'], 'http://s.jandan.com/static/gggg/blank.png') != 0 and cmp(img['src'], 'http://s.jandan.com/static/img/chart.png') != 0):
            src = ''
            #通过下载原图来下载gif文件
            if img.has_attr('org_src'):
                src = img['org_src']
            else:
                src = img['src']
            imgList.append(src)
    return imgList 
        
def saveImg(url, filename):
    image = getData(url)
    f = file('./image/' + filename, 'wb')
    f.write(image)
    f.close()
    
def createFolder(path):
    if not os.path.exists(path):
        print 'now create folder : ' + path
        
        os.mkdir(path)
        
def removeFolder(path):
    if os.path.exists(path):
        shutil.rmtree(path)

def spider(page):
    #print 'path : ' + os.path.abspath(path)
    imgList = getImgList(page)
    idx = 0
    for url in imgList:
        print 'get page:' + str(page) + '->' + str(idx) + ":" + url
        #通过split获取文件名后缀
        #print 'name : ' + url.split('.')[-1]
        saveImg(url, str(page) + '_' + str(idx) + '.' + url.split('.')[-1])
        idx = idx + 1

def working():
    while True:
        page = queue.get()
        spider(page)
        sleep(1)
        queue.task_done()
        
    
if __name__ == "__main__":
    start = time.clock()
    
    queue = Queue()
    threadNum = 5
    
    #以下语句实际获得的路径是“C:\”
    #path = os.path.dirname(__file__)
    path = os.path.split(os.path.realpath(__file__))[0]
    path = path + '/image'
    
    #清理文件夹
    removeFolder(path)
    createFolder(path)
    
    for i in range(threadNum):
        t = Thread(target = working)
        t.setDaemon(True)
        t.start()
    
    for num in range(8400,8406):
        queue.put(num)
    
    queue.join()
        
    end = time.clock()
    print 'Running time : %s Seconds' %(end - start)  
