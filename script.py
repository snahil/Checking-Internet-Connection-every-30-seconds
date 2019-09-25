import http.client as httplib
import threading
import json
import logging
import logging.handlers
import itertools
import sys
import os
import socket
count=0
def out_fun():
   with open('snahilindoria/Desktop/file', 'r') as file:
       data = file.read()
   string=json.dumps(data)
   string1=json.loads(string)
   string2=eval(string1)
   return string2
output=out_fun()
def logdata_save():
   #log=open("snahilindoria/Desktop/file", 'a')
   #LOG_FILENAME = 'data.log'
   logging.basicConfig(filename='snahilindoria/Desktop/filedata.log',filemode='a+', format='%(asctime)s - %(levelname)s - %(message)s', level=logging.INFO)
   logger = logging.getLogger('Logger')
   #my_logger.setLevel(logging.DEBUG)
   #f_handler = logging.FileHandler('snahilindoria/Desktop/file/data.log')
   #t_handler = logging.handlers.TimedRotatingFileHandler(when='midnight')
   #f_format = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
   #f_handler.setFormatter(f_format)
   #logger.addHandler(f_handler)
   #logger.addHandler(t_handler)
   logger.info(f'Lost data: {output}')
def logdata_read():
   global count
   with open("snahilindoria/Desktop/file/data.log", "r+") as f:
       for index,line in enumerate(f):
           #f.seek(count)
           #count+=1
           print(line)
           f.truncate(index)
       f.close()
global timeInterval
def check_internet():
   threading.Timer(timeInterval, check_internet).start()
   a=os.system("ping google.com")
   if(a==0):
       logdata_read()
   else:
       logdata_save()
if (__name__ == "__main__"):
   timeInterval= int(30)
   check_internet()
