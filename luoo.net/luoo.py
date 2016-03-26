# -*- coding: utf-8 -*-

import requests
import urllib
import urllib2
from bs4 import BeautifulSoup
import os

def getData(url):
    try:
        headers_get = {
        'User-Agent' : 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/48.0.2564.116 Safari/537.36'
        }
        req = urllib2.Request(url, None, headers_get)
        content = urllib2.urlopen(req)
        return content.read()
    except urllib2.URLError,e:
        error = 'error : ' + str(e.code) + ' ' + e.reason
        return error
        
def saveToFile(content, path):
    f = file(path, 'wb')
    f.write(content)
    f.close()    
    
def getCover(path, soup, radioNum):
    coverUrl = soup.find('img', {'class':'vol-cover'}).get('src')
    coverContent = getData(coverUrl)
    saveToFile(coverContent, path + radioNum + '.jpg')
    
def getSongName(soup):
    results = soup.find_all('a', {'class':'trackname btn-play'})
    names = []
    for result in results:
        names.append(result.string)
    return names
    
def getSong(path, names, radioNum):
    url = 'http://luoo-mp3.kssws.ks-cdn.com/low/luoo/radio' + radioNum + '/'
    for name in names:
        songUrl = url + name[:2] + '.mp3'
        content = getData(songUrl)
        saveToFile(content, path + name + '.mp3')

def getAlbumCover(path, soup):
    results = soup.find_all('div', {'class':'player-wrapper'})
    for result in results:
        #albumName = result.img.get('alt').encode('gbk', 'ignore')
        songName = result.find('p', {'class':'name'}).string.encode('gbk', 'ignore')
        coverUrl = result.img.get('src')
        content = getData(coverUrl)
        saveToFile(content, path + songName + '.jpg')
   
def spider(path, url, radioNum):
    content = getData(url)
    soup = BeautifulSoup(content, "html.parser")
    getCover(path, soup, radioNum)
    names = getSongName(soup)
    getSong(path, names, radioNum)
    getAlbumCover(path, soup)
    
def checkPath(path):
    if not (os.path.exists(path)):
        os.mkdir(path)
        
def main():
    radioNum = raw_input('Enter radioNum : ')
    #path = raw_input('Enter path : ')
    path = './' + radioNum + '/'
    checkPath(path)
    url = 'http://www.luoo.net/music/' + radioNum
    spider(path, url, radioNum)
    print 'done'

if __name__ == "__main__":
    main()