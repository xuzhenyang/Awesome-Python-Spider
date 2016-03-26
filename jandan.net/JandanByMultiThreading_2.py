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
        
def producer(page_q, out_q):
    page = page_q.get()
    #pic - 无聊图 ooxx - 妹子图
    url = 'http://jandan.net/pic/'
    url = url + 'page-' + str(page) + '#comments'
    #print 'url : ' + url
    
    content = getData(url)
    soup = BeautifulSoup(content, "html.parser")
    
    imgs = soup.find_all('img')
    for img in imgs:
        #print 'find out ' + img['src']
        if(cmp(img['src'], 'http://s.jandan.com/static/gggg/blank.png') != 0 and cmp(img['src'], 'http://s.jandan.com/static/img/chart.png') != 0):
            src = ''
            #通过下载原图来下载gif文件
            if img.has_attr('org_src'):
                src = img['org_src']
            else:
                src = img['src']
            out_q.put(src)
            print 'put : ' + src
            
def consumer(in_q):
    while True:
        src = in_q.get()
        saveImg(src, src.split('/')[-1])
        print 'save : ' + src
        in_q.task_done
        
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
    
if __name__ == "__main__":
    start = time.clock()
    
    page_q = Queue()
    queue = Queue()
    threadNum = 20
    
    #以下语句实际获得的路径是“C:\”
    #path = os.path.dirname(__file__)
    path = os.path.split(os.path.realpath(__file__))[0]
    path = path + '/image'
    
    #清理文件夹
    removeFolder(path)
    createFolder(path)
    
    for num in range(8400,8406):
        page_q.put(num)
    
    for i in range(threadNum):
        t1 = Thread(target = producer, args = (page_q, queue, ))
        t1.start()
        
    for i in range(threadNum):
        t2 = Thread(target = consumer, args = (queue, ))
        t2.start()
    
    
    
    queue.join()
    page_q.join()
        
    end = time.clock()
    print 'Running time : %s Seconds' %(end - start)  
