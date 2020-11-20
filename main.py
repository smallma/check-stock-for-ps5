# coding=UTF-8

import os
import sys
import requests
from bs4 import BeautifulSoup
import threading

URL = 'https://store.sony.com.tw/product/show/ff808081748fa5060174908e4ff000a8'
frequency = 2500
duration = 1000

def setInterval(func,time):
    e = threading.Event()
    while not e.wait(time):
      func()

def _getHTML(searchKey):
  page = requests.get(URL)
  soup = BeautifulSoup(page.content.decode('utf8'), 'html.parser')
  results = soup.find(text=searchKey)
  return results

def _beep():
  sys.stdout.write('\a')
  sys.stdout.flush()
  

def _checkStock():
  searchResult = _getHTML('缺貨中...')

  if not searchResult:
    print '有現貨！！！！！！！！！'
    print searchResult
    _beep()
  else :
    print '缺貨中...'
    
if __name__ == '__main__':
  
  setInterval(_checkStock, 5)