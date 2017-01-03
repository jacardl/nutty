#coding=utf8
__author__ = 'Jacard'

URL = 'http://tongji.d.pt.xiaomi.com/api/datas'

START = "2016-12-24"
END = "2016-12-30"

# after END + 1 day 11:30, results will come out

DUT = ["R1CM", "R1D", "R2D", "R1CL", "R3", "R3L", "Android", "iOS"]  #支持监控整机kernel的产品
DUT_SUPPORT_DAEMON = ["R1CM", "R1D", "R2D", "R3"] #支持监控daemon的产品

# type code
R1D = 241
R2D = 559
R1CM = 319
R1CL = 682
R3 = 1030
R3L = 1530
R3P = 0
CLIENT = 374
CRASH = 482
R1CM_VERSION_DIS = 338
R1D_VERSION_DIS = 337
R2D_VERSION_DIS = 583
R1CL_VERSION_DIS = 683
R3_VERSION_DIS = 1045
R3L_VERSION_DIS = 1533
CLIENT_VERSION_DIS = 375
CRASH_VERSION_DIS = 498
CRASH_VERSION_DAEMON_DIS = 833

FILE_NAME = "质量数据.xlsx".decode("utf8").encode("gbk")
SHEET1 = "overall"
SHEET2 = "spec version 1"
SHEET3 = "spec version top10"
SHEET4 = "spec version 2"
SHEET5 = "spec version 3"