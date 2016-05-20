# -*- coding: utf-8 -*-
from bs4 import BeautifulSoup
import re
import json

def readFile(path):
    f = open(path, 'r')
    str = f.read()
    f.close()
    return str
    
def parseTable(str):
    soup = BeautifulSoup(str, "html.parser")
    list = []
    #读取每一行记录
    for tag in soup.find('table', {'id':'Datagrid1'}).find_all('tr')[1:]:
        #使用keys列表来遍历字典，因为直接并行遍历字典，顺序会乱
        keys = ['xn', 'xq',  'kcdm', 'kcmc', 'kcxz', 'kcgs', 'xf', 'cj', 'fxbj', 'bkcj', 'xymc', 'bz']
        dict = {'xn':'', 'xq':'', 'kcdm':'', 'kcmc':'', 'kcxz':'', 'kcgs':'', 'xf':'', 'cj':'', 'fxbj':'', 'bkcj':'', 'xymc':'', 'bz':''}
        #zip并行遍历并赋值
        for key,td in zip(keys, tag.find_all('td')):
            if(td.string is None):
                td.string = ''
            dict[key] = td.string
            #dict[key] = td.string.encode('gb2312', 'ignore')
        '''
        for k,v in dict.iteritems():
            print '%s : %s' % (k, v)
        print '--------------'
        '''
        list.append(dict)
    return list
    
        
def main():
    #do something
    str = readFile('grade.html')
    list = parseTable(str)
    json.dump(list, open('grade.txt', 'w'))
        
if __name__ == "__main__":
    main()
    
    
#===========----------以后可能要用到的分割线----------===========   

"""
#遍历table：
#读取每一行记录
for tag in soup.find('table', {'id':'Datagrid1'}).find_all('tr'):
    #读取每一行中的每条字段
    for i in tag.find_all('td')[:-1]:
        print i.string.encode('gbk', 'ignore')
    print '---'
"""

"""
Error:
UnicodeEncodeError: 'gbk' codec can't encode character u'\xa0' in position 0: illegal multibyte sequ
解决方案：
td.string.encode('gb2312', 'ignore')
"""