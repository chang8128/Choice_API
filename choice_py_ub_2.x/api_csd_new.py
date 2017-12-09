#!/usr/bin/python
# encoding: utf-8
import MySQLdb

import pandas as pd
from sqlalchemy import create_engine  
# pandas.set_option('display.max_rows',None)    

# 检索股票代码
db = MySQLdb.connect("localhost","fmtc","FMTC@2017","fmtcdb" )
cursor = db.cursor()
sql1 = """select CODES from t_sector_20171202"""
a = cursor.execute(sql1)
codes = cursor.fetchmany(a)

# 数一数有多少个列表值
numrows = int(cursor.rowcount)
print numrows

# for i in range(0,len(codes)):
# 	print list(codes[i])[0]
    
db.close()


__author__ = 'Administrator'

from EmQuantAPI import *

#调用登录函数（激活后使用，不需要用户名密码）
loginResult = c.start("ForceLogin=0")

if(loginResult.ErrorCode != 0):
    print "login in fail"    
    

# csd使用范例，有用：序列函数，获取股票，指数，基金，等证券品种的，日频历史行情序列数据，
data = c.csd(codes, "open,close,high,low,preclose,AVERAGE,CHANGE,PCTCHANGE,VOLUME,HIGHLIMIT,AMOUNT,TURN,TRADESTATUS,LOWLIMIT,AMPLITUDE,TNUM,TAFACTOR,FRONTTAFACTOR,ISSTSTOCK,ISXSTSTOCK", "2017-11-01", "2017-11-30", "RowIndex=1,period=1,adjustflag=1,curtype=1,pricetype=1,year=2017,Ispandas=1") 

# 显示DataFrame 中的数据
# print data

# 调用sqlalchemy 方法将DataFrame 中的数据写入数据库中。
connect_fmtc = create_engine('mysql+mysqldb://fmtc:FMTC@2017@localhost:3306/fmtcdb?charset=utf8')  
pd.io.sql.to_sql(data,'t_csd_history', connect_fmtc, schema='fmtcdb', if_exists='append')  


