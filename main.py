# coding=UTF-8

import os
import sys
import requests
from bs4 import BeautifulSoup
import threading
from datetime import datetime

import os



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
  
def _sendNotification():
  os.system("""
    osascript -e 'display notification "{}" with title "{}"'
  """.format('快買喔！！', 'PS5 有貨啦！！！'))


def _recordStockStatus(status):
  f = open("stocklog", "a")
  record = status + '\n'
  f.write(record)
  f.close()

def _getNowDate():
  now = datetime.now()
  dateTime = now.strftime("%m/%d/%Y, %H:%M:%S")
  return dateTime

def _checkStock():
  status = ''
  searchResult = _getHTML('缺貨中...')
  dateTime = _getNowDate()

  if not searchResult:
    status = ' - 有現貨！！！！！！！！！'
    _beep()
    _sendNotification()
    _recordStockStatus(dateTime + status)

  else :
    status = ' - 缺貨中...'

  record = dateTime + status
  print record

def _main():
  setInterval(_checkStock, 3)

if __name__ == '__main__':
  _main()