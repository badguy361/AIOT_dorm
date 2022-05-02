#**************************************************** 
# Import Package                                                                           
import pymysql
import time  
import requests  
import json  
import datetime  
import threading
import sys  
from serial import Serial as s

class Data:# 為啥是16??
    table=[[i]*16 for i in range(2)]# [0]voltage [1]state
    #[[0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]]

def rx(port):
    buffer = []
    while True:
        flag = 1
        while flag:
            oneByte = port.read(1)
            if oneByte == b'\xed': #byte
                dummy = int.from_bytes(oneByte,byteorder='little') #bytes2int
                buffer.append(dummy)
                for i,val in enumerate(buffer):
                    if val == 85:
                        startbyte = i
                        buffer = buffer[i:]
                print (buffer)
                a = buffer
                #print (buffer.split())
                buffer = []
                flag = 0
            else:
                dummy = int.from_bytes(oneByte,byteorder='little')
                buffer.append(dummy)
        
        
        if len(a) == 0: 
            time.sleep(0.1)# for test
            continue
        a=list(a)
        print(a)
        b=sum(a[1:23])%255# check sum
        print(b, a[23])
        
        if a[0]==85 and a[1]==51 and a[23]==b  and a[24]==237:# start point and check what kind of device is it and checkSum and endkpoint
            n1=len("{0:b}".format(a[21]))#Read the state of first 8 devices
            print("{0:b}".format(a[21]))

            state1="0"*(8-n1)+"{0:b}".format(a[21])
            state1 = state1[::-1]
            print('state1 ',state1)
            n2=len("{0:b}".format(a[22]))#Read the state of later 8 devices
            state2="0"*(8-n2)+"{0:b}".format(a[22])
            state2 = state2[::-1]
            
            print('state2 ',state2)
            
            for i in range(1,17):   
                Data.table[0][i-1]=a[i+4]*0.02#put voltage data into Data.table
                if i<9:
                    Data.table[1][i-1]=state1[i-1]# put the state of that area into Data.table
                else:
                    Data.table[1][i-1]=state2[i-9] 
            for i in range(1,17):          
                print(Data.table[0][i-1],Data.table[1][i-1])

def client_job(status, data): # 顯示狀態與響應
    result = requests.post(status, data=data) # 用put
    print('Status Code = ' + str(result.status_code) + ', Response = ' + result.text)

def postdata():#資料放置的位置(要改成我們的伺服器)
    while 1:
        web_url = 'http://140.115.200.38:80/postdorm/'
        facilities = 'washing machine'
        dorm=11
        floor=4
        temperature_location = 'male'+str(dorm)+'dorm'# MaleDorm11
        fTimeTest=time.time()
        t = time.time()
        #upperDate開始時間
        Date = datetime.datetime.fromtimestamp(t).strftime('%Y%m%d%H%M%S')#Those are used to describe the year, mouth and date
        #lowerDate結束時間
        # lowerDate = datetime.datetime.fromtimestamp(t).strftime('%H%M%S')#Those are describe the other timestamp. It in order to makes the appmaker better to employ this date to figure out when user leave thier area. 
        Y=datetime.datetime.fromtimestamp(t).strftime('%Y')
        m=datetime.datetime.fromtimestamp(t).strftime('%m')
        d=datetime.datetime.fromtimestamp(t).strftime('%d')
        H=datetime.datetime.fromtimestamp(t).strftime('%H')
        M=datetime.datetime.fromtimestamp(t).strftime('%M')
        S=datetime.datetime.fromtimestamp(t).strftime('%S')
        #**************************************************** 
        # Insert Data                                                                              
        #**************************************************** 

        #label=1#先寫死 之後等更多sensor後要改 階段性任務結束
        floor = 4
        #for floor in range(1,2):#It means how many floor we need to handle
        worker_pool = []
        
        for thread in range(1,11):
            data = {'Date':Date, 'facilities_name':facilities,'facilities_info': Data.table[1][thread-1],\
                'facilities_voltage':  str(Data.table[0][thread-1])}
            print('upload--------------------------------')
            print(data)            
            print('upload--==============================')
            t = threading.Thread(target=client_job, args=(web_url, data))#建立10個子執行序
            worker_pool.append(t)
            t.start()

        for t in worker_pool:# 等待所有子執行序結束
            t.join()
        
        fDelay=time.time()-fTimeTest
        if fDelay < 10:
            time.sleep(10-fDelay)
'''
def mysql():
    while 1:
        mTimeTest=time.time()
        t = time.time()
        upperDate = datetime.datetime.fromtimestamp(t).strftime('%Y%m%d')#Those are used to describe the year, mouth and date
        lowerDate = datetime.datetime.fromtimestamp(t).strftime('%H%M%S')#Those are describe the other timestamp. It in order to makes the appmaker better to employ this date to figure out when user leave thier area. 
        Y=datetime.datetime.fromtimestamp(t).strftime('%Y')
        m=datetime.datetime.fromtimestamp(t).strftime('%m')
        d=datetime.datetime.fromtimestamp(t).strftime('%d')
        H=datetime.datetime.fromtimestamp(t).strftime('%H')
        M=datetime.datetime.fromtimestamp(t).strftime('%M')
        S=datetime.datetime.fromtimestamp(t).strftime('%S')
        conne = pymysql.connect(host = '35.189.182.165',
        user = 'root', password = 'dannywu', db = 'test')
        dorm=9
        floor=1
        #label=1階段性任務結束
        connection = pymysql.connect(host='35.189.182.165',
            user='root',
            port=3306,
            password='dannywu',
            db='test',
            cursorclass=pymysql.cursors.DictCursor)
        try:
            for label in range(1,11):#the number of label
                with connection.cursor() as cursor:
                    sqlQuery =  "INSERT INTO new_table(`building`,`floor`,`label`,`state`,`voltage`,`year`,`mouth`,`date`,`hour`,`mintue`,`second`) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)"  ###################需改
                    cursor.execute(sqlQuery, (dorm,floor,label,Data.table[1][label-1],Data.table[0][label-1],Y,m,d,H,M,S))################################需改 資料同上行
                    connection.commit()
        finally:
            connection.close()#--------------從265到278行(這一行)都是上傳到資料庫
        mDelay=time.time()-mTimeTest
        if mDelay < 10:
            time.sleep(10-mDelay)
'''

