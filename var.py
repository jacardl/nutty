#coding=utf8
__author__ = 'Jacard'

URL = 'http://tongji.d.pt.xiaomi.com/api/datas'

START = "2017-12-11"
END = "2017-12-17"
# START = "2017-09-11"
# END = "2017-09-11"

# after END + 1 day 11:30, results will come up
# DUT_SUPPORT_KERNEL = ["R1CM", "R1D", "R2D", "R1CL", "R3", "R3L", "R3D", "R3P", "R3G","R3A", "P01","Android", "iOS"]  #支持监控整机kernel crash的产品
DUT = ["R1CM", "R1D", "R2D", "R1CL", "R3", "R3L", "R3D", "R3P", "R3G","R3A", "P01", "R01", "R02", "R03", "Android", "iOS"]
DUT_SUPPORT_DAEMON = ["R1CM", "R1D", "R2D", "R3", "R3D", "R3P", "R3G"] #支持监控daemon crash的产品

# type code
# 新增设备时，取其日活跃任务的type编号
# v_R3D-概况数据-日活跃,查看 stderr 中 Sending HTTP POST to http://tongji.d.pt.xiaomi.com/api/put?type=2091&sub_type=%E6%97%A5%E6%B4%BB%E8%B7%83&key=FB7F640D5314E015A533B55DFEED719B&date=2017-03-19
# sub_type = 日活跃
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
#不支持统计日活，支持kernel crash统计，不支持daemon crash统计
P01 = 0

# v_路由器_放大器_概况_日活跃，查看R01/R02/R03的总体日活跃
# http://tongji.d.pt.xiaomi.com/api/put?type=681&sub_type=%E6%97%A5%E6%B4%BB%E8%B7%83&key=73BCBEE35971B5E24C9F61A2E26296C7&date=2017-11-04
# ============================== data =============================
# [["name","count1"],["R01","721479"],["R02","592822"],["R03","79027"]]
# =================================================================
# sub_type = 日活跃
#支持统计日活，不支持kernel crash统计，不支持daemon crash统计
R01 = R02 = R03 = 681

# 新增设备时，取其活跃版本分布任务的type编号
# v_R3D_概况-版本分布-全部活跃版本分布，查看 stderr 中 http://tongji.d.pt.xiaomi.com/api/put?type=2093&sub_type=%E5%85%A8%E9%83%A8%E6%B4%BB%E8%B7%83%E7%94%A8%E6%88%B7%E7%89%88%E6%9C%AC%E7%BB%9F%E8%AE%A1&key=565D13DBB0E2419AF3A39210C248A51E&date=2017-03-19
# sub_type = 全部活跃用户版本统计 | 全部活跃用户版本分布（R1D/R2D/R1CM）
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
P01_VERSION_DIS = 0

# v_放大器_概况-日活版本分布，查看R01/R02/R03各个版本的日活跃
# http://tongji.d.pt.xiaomi.com/api/put?type=919&sub_type=%E6%97%A5%E6%B4%BB%E7%89%88%E6%9C%AC%E5%88%86%E5%B8%83&key=E04E19990F4562755B8C46B33E518729&date=2017-11-04
# ============================== data =============================
# [["name","count1"],["R01--0.2.10","1"],["R01--0.2.31","2"],["R01--0.2.5","1"],["R01-release-0.2.10","12547"],["R01-release-0.2.31","67439"],["R01-release-0.2.5","2018"],["R01-release-1.4.12","9"],["R01-release-1.4.14","639370"],["R01-release-2.0.10","1"],["R01-stable-0.3.2","2"],["R01-stable-1.5.21","7"],["R01-stable-1.5.22","85"],["R02-release-2.0.10","51255"],["R02-release-2.0.28","531930"],["R02-release-2.0.6","10"],["R02-release-2.2.13","1"],["R02-release-2.2.14","9625"],["R02-release-2.2.2","2"],["R03-release-3.0.10","41374"],["R03-release-3.0.11","2"],["R03-release-3.0.9","37651"]]
# =================================================================
# sub_type = 日活版本分布
R01_VERSION_DIS = R02_VERSION_DIS = R03_VERSION_DIS = 919

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