#coding=utf8
__author__ = 'Jac'
import requests
import collections

import var as v


def getApi(url=v.URL, **kwargs):
    s = requests.session()
    # my_headers = {'User-Agent' : 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/53.0.2785.116 Safari/537.36',
    #               "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8",
    #               "Accept-Encoding": "gzip, deflate, br",
    #             }
    option = {
                "type": "",
                "subtype": "",
                "start": "",
                "end": "",
            }
    option.update(kwargs)
    res = s.get(url=v.URL, params=option, timeout=10)
    # resJson = json.dumps(res.content)
    return eval(res.content)


def getAveCount1ForSpecName(data, name):
    countList = []
    if data.get("status") is 1:
        for r in data.get("result"):
            if r.get("name") == name:
                count = r.get("count1")
                if count.isdigit():
                    countList.append(int(count))
        if len(countList) is not 0:
            countAve = reduce(lambda x, y: x + y, countList)/float(len(countList))
            return int(round(countAve))
        return 0


def getDailyActive(type, **kwargs):
    """
    :param name: rom/android/pc/mac/ios
    :param type: v.R1CM/v.R1D/v.R2D...
    :return:
    'result': [{'name': 'rom', 'subtype': '\xe6\x97\xa5\xe6\xb4\xbb\xe8\xb7\x83', 'date': '2016-09-27 00:00:00.0',
    'count1': '27291', 'count2': '0', 'type': 241},
    """

    option = {
        "type": type,
        "subtype": "日活跃",
        "start": v.END,
        "end": v.END,
    }
    option.update(kwargs)
    res = getApi(**option)
    if res.get("status") is 1:
        for r in res.get("result"):
            if r.get("name") == "rom":
                return int(r.get("count1"))
            return 0


def getAveDailyActive(dut, **kwargs):
    """
     'result': [{'name': 'android', 'subtype': '\xe6\x97\xa5\xe6\xb4\xbb\xe8\xb7\x83', 'date': '2016-09-27 00:00:00.0',
     'count1': '27291', 'count2': '0', 'type': 241},
    """
    command = {
        "R1CM" : "v.R1CM",
        "R1D" : "v.R1D",
        "R2D" : "v.R2D",
        "R1CL" : "v.R1CL",
        "R3" : "v.R3",
        "R3L" : "v.R3L",
    }
    type = eval(command.get(dut))
    option = {
        "type": type,
        "subtype": "日活跃",
        "start": v.START,
        "end": v.END,
    }
    option.update(kwargs)
    res = getApi(**option)
    return getAveCount1ForSpecName(res, "rom")


def getClientAPPAveDailyActive(name, **kwargs):
    """
    name: android/ios/mac/pc
    {"status":1,"result":[{"count1":"1295724","count2":"0","date":"2016-09-21 00:00:00.0","name":"android","subtype":"月活跃用户","type":374},
    """
    option = {
        "type": v.CLIENT,
        "subtype": "活跃用户",
        "start": v.START,
        "end": v.END,
    }
    option.update(kwargs)
    res = getApi(**option)
    name = name.lower()
    return getAveCount1ForSpecName(res, name)


def getKernelCrashAveDaily(dut, subtype, **kwargs):
    """
    name: R1CM/R1D... or app/ios
    subtype: CrashLog次数/CrashLog用户数
    {"status":1,"result":[{"count1":"758","count2":"0","date":"2016-09-21 00:00:00.0","name":"app-kernel","subtype":"CrashLog次数","type":482}
    """
    option = {
        "type": v.CRASH,
        "subtype": subtype,
        "start": v.START,
        "end": v.END,
    }
    option.update(kwargs)
    res = getApi(**option)
    if dut.lower() == "android":
        dut = "app"
    elif dut.lower() == "ios":
        dut = "ios"
    return getAveCount1ForSpecName(res, dut+'-kernel')


def getDaemonCrashAveDaily(dut, subtype, **kwargs):
    """
    name: R1CM/R1D...
    subtype: CrashLog次数/CrashLog用户数
    {"status":1,"result":[{"count1":"758","count2":"0","date":"2016-09-21 00:00:00.0","name":"app-kernel","subtype":"CrashLog次数","type":482}
    """
    option = {
        "type": v.CRASH,
        "subtype": subtype,
        "start": v.START,
        "end": v.END,
    }
    option.update(kwargs)
    res = getApi(**option)
    return getAveCount1ForSpecName(res, dut+'-app')


def getVersionDistribDaily(type, subtype):
    """
    {"status":1,"result":[{"count1":"2","count2":"0","date":"2016-09-21 00:00:00.0","name":"2.15.3","subtype":"活跃用户版本分布","type":338}
    subtype: 全部活跃用户版本分布(R1D/R2D/R1CM)/全部活跃用户版本统计(R1CL/R3/R3L)/版本分布/android版本分布/ios版本分布
    type: v.R1CM_VERSION_DIS/v.R1D_VERSION_DIS...
    """
    option = {
        "type": type,
        "subtype": subtype,
        "start": v.END,
        "end": v.END
    }
    res = getApi(**option)
    versionDict = {}
    if res.get("status") is 1:
        for r in res.get("result"):
            versionDict.update({r.get("name"): int(r.get("count1"))})
        versionDict = sorted(versionDict.iteritems(), key=lambda x: x[1], reverse=True)
        return versionDict


def getVersionDistribAveDaily(type, subtype, **kwargs):
    """
    {"status":1,"result":[{"count1":"2","count2":"0","date":"2016-09-21 00:00:00.0","name":"2.15.3","subtype":"活跃用户版本分布","type":338}
    subtype: 全部活跃用户版本分布(R1D/R2D/R1CM)/全部活跃用户版本统计(R1CL/R3/R3L)/版本分布/android版本分布/ios版本分布
    type: v.R1CM_VERSION_DIS/v.R1D_VERSION_DIS...
    """
    option = {
        "type": type,
        "subtype": subtype,
        "start": v.START,
        "end": v.END
    }
    option.update(kwargs)
    res = getApi(**option)
    versionDict = {}
    if res.get("status") is 1:
        for r in res.get("result"):
            ver = r.get("name")
            count = int(r.get("count1"))
            if versionDict.get(ver) is not None:
                versionDict.get(ver).append(count)
            else:
                versionDict.update({ver: [count]})
        for x, y in versionDict.items():
            countAve = reduce(lambda a, b: a + b, y)/float(len(y))
            versionDict[x] = int(round(countAve))
        versionDict = sorted(versionDict.iteritems(), key=lambda x: x[1], reverse=True)
        return versionDict


def getVersionMostUsedDailyActive(dut):
    """
    :param type: v.R1CM_VERSION_DIS/v.R1D_VERSION_DIS/v.R2d_VERSION_DIS...
    """
    command = {
        "R1CM": "getVersionDistribDaily(v.R1CM_VERSION_DIS, '全部活跃用户版本分布')",
        "R1D": "getVersionDistribDaily(v.R1D_VERSION_DIS, '全部活跃用户版本分布')",
        "R2D": "getVersionDistribDaily(v.R2D_VERSION_DIS, '全部活跃用户版本分布')",
        "R1CL": "getVersionDistribDaily(v.R1CL_VERSION_DIS, '全部活跃用户版本统计')",
        "R3": "getVersionDistribDaily(v.R3_VERSION_DIS, '全部活跃用户版本统计')",
        "R3L": "getVersionDistribDaily(v.R3L_VERSION_DIS, '全部活跃用户版本统计')",
    }
    res = eval(command.get(dut))
    version = res[0][0]
    count = res[0][1]
    return version, count


def getClientAPPVersionMostUsedDaily(dut):
    """
    :param subtype: android版本分布/ios版本分布
    """
    subtype = dut.lower() + "版本分布"
    res = getVersionDistribDaily(v.CLIENT_VERSION_DIS, subtype)
    version = res[0][0]
    count = res[0][1]
    return version, count


def getSpecVersionKernelCrashAveDaily(dut, version, subtype, **kwargs):
    """
    :param name: "R1CM-0.5.8"/"app-2.2.2/ios-2.2.2"
    :param subtype: "CrashLog用户数"

    :param name: "R1CM-kernel-0.5.8"/"app-2.2.2/ios-2.2.2"
    :param subtype: "CrashLog次数"
    """
    option = {
        "type": v.CRASH_VERSION_DIS,
        "subtype": subtype,
        "start": v.START,
        "end": v.END
    }
    if dut.lower() == "android":
        dut = "app"
    elif dut.lower() == "ios":
        dut = "ios"
    if subtype == "CrashLog用户数":
        name = dut + "-" + version
    elif subtype == "CrashLog次数":
        name = dut + "-kernel-" + version
    option.update(kwargs)
    res = getApi(**option)
    return getAveCount1ForSpecName(res, name)


def getSpecVersionDaemonCrashDaily(dut, version, **kwargs):
    """
    :param subtype: R1D/R2D/R3/R1CM
    :param version: 重点关注版本
    :param kwargs:
    :return:
    """
    option = {
        "type": v.CRASH_VERSION_DAEMON_DIS,
        "subtype": dut,
        "start": v.END,
        "end": v.END
    }
    option.update(kwargs)
    res = getApi(**option)
    daemonVersionCount1Dict = {}
    daemonVersionCount2Dict = {}
    if res.get('status') is 1:
        for r in res.get('result'):
            if r.get('name').find(version) is not -1:
                daemonVersionCount1Dict.update({r.get('name'): int(r.get('count1'))})
                crashUser = sorted(daemonVersionCount1Dict.iteritems(), key=lambda x: x[1], reverse=True)
                daemonVersionCount2Dict.update({r.get('name'): int(r.get('count2'))})
                crashCount = sorted(daemonVersionCount2Dict.iteritems(), key=lambda x: x[1], reverse=True)
        return crashUser, crashCount


def getSpecVersionDailyActive(dut, version):
    command = {
        "R1CM": "getVersionDistribDaily(v.R1CM_VERSION_DIS, '全部活跃用户版本分布')",
        "R1D": "getVersionDistribDaily(v.R1D_VERSION_DIS, '全部活跃用户版本分布')",
        "R2D": "getVersionDistribDaily(v.R2D_VERSION_DIS, '全部活跃用户版本分布')",
        "R1CL": "getVersionDistribDaily(v.R1CL_VERSION_DIS, '全部活跃用户版本统计')",
        "R3": "getVersionDistribDaily(v.R3_VERSION_DIS, '全部活跃用户版本统计')",
        "R3L": "getVersionDistribDaily(v.R3L_VERSION_DIS, '全部活跃用户版本统计')",
    }
    res = eval(command.get(dut))
    # version = version.split('.')
    # number = int(version[0]) * 1000 * 1000 + int(version[1]) * 1000 + int(version[2])
    if len(res) is not 0:
        for r in res:
            if r[0].find(version) is not -1:
                return int(r[1])
        return 0


def getSpecVersionAveDailyActive(dut, version):
    command = {
        "R1CM": "getVersionDistribAveDaily(v.R1CM_VERSION_DIS, '全部活跃用户版本分布')",
        "R1D": "getVersionDistribAveDaily(v.R1D_VERSION_DIS, '全部活跃用户版本分布')",
        "R2D": "getVersionDistribAveDaily(v.R2D_VERSION_DIS, '全部活跃用户版本分布')",
        "R1CL": "getVersionDistribAveDaily(v.R1CL_VERSION_DIS, '全部活跃用户版本统计')",
        "R3": "getVersionDistribAveDaily(v.R3_VERSION_DIS, '全部活跃用户版本统计')",
        "R3L": "getVersionDistribAveDaily(v.R3L_VERSION_DIS, '全部活跃用户版本统计')",
    }
    res = eval(command.get(dut))
    if len(res) is not 0:
        for r in res:
            if r[0].find(version) is not -1:
                return int(r[1])
        return 0


def getSpecVersionDaemonCrashUserCountTop10Daily(dut, version):
    user, _ = getSpecVersionDaemonCrashDaily(dut, version)
    return user[0:10]

if __name__ == '__main__':
    # print getAveDailyActive("R1CM")
    # print getAveDailyActive("R1D")
    # print getAveDailyActive("R2D")
    # print getAveDailyActive("R1CL")
    # print getAveDailyActive("R3")
    # print getAveDailyActive("R3L")
    # print getClientAPPAveDailyActive("android")
    # print getClientAPPAveDailyActive("ios")
    # print getClientAPPAveDailyActive("mac")

    # print getKernelCrashAveDaily("R1CM", "CrashLog次数")
    # print getKernelCrashAveDaily("R1D", "CrashLog次数")
    # print getKernelCrashAveDaily("R2D", "CrashLog次数")
    # print getKernelCrashAveDaily("R1CL", "CrashLog次数")
    # print getKernelCrashAveDaily("R3", "CrashLog次数")
    # print getKernelCrashAveDaily("R3L", "CrashLog次数")
    # print getKernelCrashAveDaily("app", "CrashLog次数")
    # print getKernelCrashAveDaily("ios", "CrashLog次数")
    # print getKernelCrashAveDaily("R1CM", "CrashLog用户数")
    # print getKernelCrashAveDaily("R1D", "CrashLog用户数")
    # print getKernelCrashAveDaily("R2D", "CrashLog用户数")
    # print getKernelCrashAveDaily("R1CL", "CrashLog用户数")
    # print getKernelCrashAveDaily("R3", "CrashLog用户数")
    # print getKernelCrashAveDaily("R3L", "CrashLog用户数")
    # print getKernelCrashAveDaily("app", "CrashLog用户数")
    # print getKernelCrashAveDaily("ios", "CrashLog用户数")

    # print getDaemonCrashAveDaily("R1CM", "CrashLog次数")
    # print getDaemonCrashAveDaily("R1D", "CrashLog次数")
    # print getDaemonCrashAveDaily("R2D", "CrashLog次数")
    # print getDaemonCrashAveDaily("R3", "CrashLog次数")
    # print getDaemonCrashAveDaily("R1CM", "CrashLog用户数")
    # print getDaemonCrashAveDaily("R1D", "CrashLog用户数")
    # print getDaemonCrashAveDaily("R2D", "CrashLog用户数")
    # print getDaemonCrashAveDaily("R3", "CrashLog用户数")

    # version, count = getVersionMostUsedDaily("R1CM")
    # print version, count
    # print getSpecVersionKernelCrashAveDaily(dut="R1CM", version=version, subtype="CrashLog次数")
    # print getSpecVersionKernelCrashAveDaily(dut="R1CM", version=version, subtype="CrashLog用户数")

    # print getVersionMostUsedDailyActive("R1D")
    # print getVersionMostUsedDailyActive("R2D")
    # print getVersionMostUsedDailyActive("R1CM")
    # print getVersionMostUsedDailyActive("R1CL")
    # print getVersionMostUsedDailyActive("R3")
    # print getVersionMostUsedDailyActive("R3L")

    version, count = getClientAPPVersionMostUsedDaily("Android")
    version2, count2 = getClientAPPVersionMostUsedDaily("iOS")
    print version, count
    print version2, count2
    # print getSpecVersionKernelCrashAveDaily(dut="app", version=version, subtype="CrashLog次数")
    # print getSpecVersionKernelCrashAveDaily(dut="app", version=version, subtype="CrashLog用户数")
    # print getSpecVersionKernelCrashAveDaily(dut="ios", version=version2, subtype="CrashLog次数")
    # print getSpecVersionKernelCrashAveDaily(dut="ios", version=version2, subtype="CrashLog用户数")
    # user, count = getSpecVersionDaemonCrashDaily("R1CM", "2.12.3")
    # print  user , "\n", count

    # print getSpecVersionDailyActive("R1CM", "2.12.3")
    # print getSpecVersionAveDailyActive("R1CM", "2.12.3")
    # print getSpecVersionDaemonCrashUserCountTop10Daily("R1CM", "2.12.3")

