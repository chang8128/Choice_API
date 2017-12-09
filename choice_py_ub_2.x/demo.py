
# -*- coding:utf-8 -*-

# import numpy as np  
# np.set_printoptions(threshold=np.inf) 

# pd.set_option('display.max_columns',None)

import pandas
pandas.set_option('display.max_rows',None)    

__author__ = 'Administrator'


from EmQuantAPI import *

def startCallback(message):
    print "[EmQuantAPI Python]", message
    return 1
def demoQuoteCallback(quantdata):
    """
    DemoCallback 是EM_CSQ订阅时提供的回调函数模板。该函数只有一个为c.EmQuantData类型的参数quantdata
    :param quantdata:c.EmQuantData
    :return:
    """
    print "demoQuoteCallback,", str(quantdata)

def cstCallBack(quantdata):
    """
    cstCallBack 是EM_CST订阅时提供的回调函数模板。该函数只有一个为c.EmQuantData类型的参数quantdata
    :param quantdata:c.EmQuantData
    :return:
    """
    for i in range(0, len(quantdata.Codes)):
        length = len(quantdata.Dates)
        for it in quantdata.Data.keys():
            print it
            for k in range(0, length):
                for j in range(0, len(quantdata.Indicators)):
                    print quantdata.Data[it][j * length + k], " ",
                print ""

#调用登录函数（激活后使用，不需要用户名密码）
loginResult = c.start("ForceLogin=0")

if(loginResult.ErrorCode != 0):
    print "login in fail"


# # csc使用范例，暂时没用，历史分钟K线
# data = c.csc("300059.SZ", "OPEN,CLOSE,HIGH", "2016-08-10", "2016-08-11","RowIndex=2,Ispandas=1")
# print u"csc输出结果======分隔线======"
# if(not isinstance(data, c.EmQuantData)):
#     print data
# else:
#     if data.ErrorCode != 0:
#         print "request csc Error, ", data.ErrorMsg
#     else:
#         for i in range(0, len(data.Indicators)):
#             for j in range(0, len(data.Dates)):
#                 print "indicator=%s, value=%s" % (data.Indicators[i], str(data.Data[i][j]))
            
# csd使用范例，有用：序列函数，获取股票，指数，基金，等证券品种的，日频历史行情序列数据，
data = c.csd("000036.SZ,600425.SH", "PRECLOSE,open,high,low,close", "2017-08-10", "2017-08-17", "RowIndex=1,period=1,adjustflag=1,curtype=1,pricetype=1,year=2016,Ispandas=0")

print u"csd输出结果======分隔线======"
if(not isinstance(data, c.EmQuantData)):
    print data
else:
    if data.ErrorCode != 0:
        print "request csd Error, ", data.ErrorMsg
    else:
        for code in data.Codes:
            for i in range(0, len(data.Indicators)):
                for j in range(0, len(data.Dates)):
                    print data.Data[code][i][j]

# css使用范例,暂时没用；截面数据，获取股票，指数，基金，等各个证券品种的基本资料，财务，估值等截面数据。下面获取的是 20170308 当天的数据（未复权），其中显示的 2017-09-14 只是程序运行日，没有实际意义。
# data = c.css("300059.SZ, 000002.SZ, 000002.SH", "open,close", "TradeDate=20170308, ispandas=1")
# data = c.css("000036.SZ, 002241.SZ, 000002.SH", "open,close,high,low", "TradeDate=20170308, ispandas=1")
# data = c.css("001004", "BLSWSIND", “ClassiFication=1”, "TradeDate=20170915, ispandas=1")
# print u"css输出结果======分隔线======"
# if(not isinstance(data, c.EmQuantData)):
#     print data
# else:
#     if data.ErrorCode != 0:
#         print "request css Error, ", data.ErrorMsg
#     else:
#         for code in data.Codes:
#             for i in range(0, len(data.Indicators)):
#                     print data.Data[code][i]




# sector使用范例，某个股票所属的二级行业。
# data = c.sector("001004", "2016-04-26")
# data = c.sector("011019002001", "2016-04-26")
# if data.ErrorCode != 0:
#     print "request sector Error, ", data.ErrorMsg
# else:
#     print "sector输出结果======分隔线======"
#     for code in data.Data:
#         print code



# os.chdir("/var/www")
# f = open ("stock_hangye.txt","w")
# 
# code = c.sector("001004","20170915")
# data = c.css(code.Codes,"NAME,SW2014","ClassiFication=4,Ispandas=1")
# # print data
# print >>f,data
        
        
# data = c.sector("011019002001", "2016-04-26")
# if data.ErrorCode != 0:
#     print "request sector Error, ", data.ErrorMsg
# else:
#     print "sector输出结果======分隔线======"
#     for code in data.Data:
#         print code


        

# tradedate使用范例，有用；列出起止日期内的交易日，None为默认截止日为当天；
# data = c.tradedates("2016-07-01", "2016-07-12")
# data = c.tradedates("2017-05-01", None)
# if data.ErrorCode != 0:
#     print "request tradedates Error, ", data.ErrorMsg
# else:
#     print "tradedate输出结果======分隔线======"
#     for item in data.Data:
#         print item
        
        
# os.chdir("/var/www")
# f = open ("tradedates.txt","w")
# data = c.tradedates("2017-05-01", None, "Ispandas=1")
# if data.ErrorCode != 0:
#     print "request tradedates Error, ", data.ErrorMsg
# else:
#     print "tradedate输出结果======分隔线======"
#     for item in data.Data:
#         print >>f,data



# # getdate使用范例，偏移N天的交易日函数(8月26日是周六，向前三天的日期为22号；和8月25日向前三天的值一样为22号)；
# data = c.getdate("20170825", -3, "Market=CNSESH")
# if data.ErrorCode != 0:
#     print "request getdate Error, ", data.ErrorMsg
# else:
#     print "getdate输出结果======分隔线======"
#     print data.Data

# #实时行情订阅使用范例
# data = c.csq("300059.SZ", "PRECLOSE,OPEN,HIGH", "Pushtype=1")
# if data.ErrorCode != 0:
#     print "request csq Error, ", data.ErrorMsg
# else:
#     print "csq输出结果======分隔线======"
#     text = raw_input("press any key to cancel csq \r\n")
#     #取消订阅
#     data = c.csqcancel(data.SerialID)

# #日内跳价服务使用范例
# data = c.cst('300059.SZ,600000.SH', 'TIME,OPEN,HIGH,LOW,NOW', '100000', '101000')
# if data.ErrorCode != 0:
#     print "request cst Error, ", data.ErrorMsg
# else:
#     print "cst输出结果======分割线======"
#     raw_input("press any key to quit cst \r\n")
# 
# 
#行情快照使用范例
# data = c.csqsnapshot("000005.SZ,600602.SH,600652.SH,600653.SH,600654.SH,600601.SH,600651.SH,000004.SZ,000002.SZ,000001.SZ,000009.SZ", "PRECLOSE,OPEN,HIGH,LOW,NOW,AMOUNT")
# if data.ErrorCode != 0:
#     print "request csqsnapshot Error, ", data.ErrorMsg
# else:
#     print "csqsnapshot输出结果======分割线======"
#     for key,value in data.Data.items():
#         print key, ">>> ",
#         for v in value:
#             print v,
#         print ""
    
#获取专题报表使用范例
# data = c.ctr("INDEXCOMPOSITION", "", "IndexCode=000001.SH,EndDate=2017-01-13")
# if data.ErrorCode != 0:
#     print "request ctr Error, ", data.ErrorMsg
# else:
#     print "ctr输出结果======分割线======"
#     for key,value in data.Data.items():
#         for v in value:
#             print v,
#         print ""
        
# #选股使用范例
# data = c.cps("B_001004", "s0,OPEN,2017/2/27,1;s1,NAME", "[s0]>0", "orderby=rd([s0]),top=max([s0],100)")
# if data.ErrorCode != 0:
#     print "request ctr Error, ", data.ErrorMsg
# else:
#     print u"cps输出结果======分割线======"
#     for it in data.Data:
#       print it


#退出
data = logoutResult = c.stop()
print 'ok'


