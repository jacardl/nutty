#coding=utf8
__author__ = 'Jacard'

URL = 'http://tongji.d.pt.xiaomi.com/api/datas'

START = "2017-08-28"
END = "2017-09-03"

# after END + 1 day 11:30, results will come out

DUT = ["R1CM", "R1D", "R2D", "R1CL", "R3", "R3L", "R3D", "R3P", "R3G","R3A", "Android", "iOS"]  #支持监控整机kernel的产品
DUT_SUPPORT_DAEMON = ["R1CM", "R1D", "R2D", "R3", "R3D", "R3P", "R3G"] #支持监控daemon的产品

# type code
# 新增设备时，取其日活跃任务的type编号
# v_R3D-概况数据-日活跃,查看 stderr 中 Sending HTTP POST to http://tongji.d.pt.xiaomi.com/api/put?type=2091&sub_type=%E6%97%A5%E6%B4%BB%E8%B7%83&key=FB7F640D5314E015A533B55DFEED719B&date=2017-03-19
R1D = 241
R2D = 559
R1CM = 319
R1CL = 682
R3 = 1030
R3L = 1530
R3P = 2088
R3D = 2091
R3G = 2386
R3A = 2392
CLIENT = 374
CRASH = 482

# 新增设备时，取其活跃版本分布任务的type编号
# v_R3D_概况-版本分布-全部活跃版本分布，查看 stderr 中 http://tongji.d.pt.xiaomi.com/api/put?type=2093&sub_type=%E5%85%A8%E9%83%A8%E6%B4%BB%E8%B7%83%E7%94%A8%E6%88%B7%E7%89%88%E6%9C%AC%E7%BB%9F%E8%AE%A1&key=565D13DBB0E2419AF3A39210C248A51E&date=2017-03-19
R1CM_VERSION_DIS = 338
R1D_VERSION_DIS = 337
R2D_VERSION_DIS = 583
R1CL_VERSION_DIS = 683
R3_VERSION_DIS = 1045
R3L_VERSION_DIS = 1533
R3D_VERSION_DIS = 2093
R3P_VERSION_DIS = 2090
R3G_VERSION_DIS = 2388
R3A_VERSION_DIS = 2394

#v-客户端-客户端概况-版本分布-android、v-客户端-客户端概况-版本分布-ios
CLIENT_VERSION_DIS = 375
# v-路由器-crash-app用户数-版本分布 、	v-路由器-crash-app次数-版本分布、v-路由器-crash用户数-版本分布、v-路由器-crash次数-版本分布
CRASH_VERSION_DIS = 498
# 进程crash统计分布
# v_R3D_crash_app_分布
CRASH_VERSION_DAEMON_DIS = 833

FILE_NAME = "质量数据.xlsx".decode("utf8").encode("gbk")
SHEET1 = "overall"
SHEET2 = "most version"
SHEET3 = "most version top10"
SHEET4 = "second most version"
SHEET5 = "third most version"
SHEET6 = "latest stable version"
SHEET7 = "latest stable version top10"