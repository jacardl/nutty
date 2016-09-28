#coding=utf8
__author__ = 'Jac'
import requests

import var as v


def getApi(url=v.URL, **kwargs):
    s = requests.session()
    # my_headers = {'User-Agent' : 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/53.0.2785.116 Safari/537.36',
    #               "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8",
    #               "Accept-Encoding": "gzip, deflate, br",
    #             }
    option = {
                "type": "482",
                "subtype": "CrashLog次数",
                "start": "2016-09-27",
                "end": "2016-09-27",
            }
    option.update(kwargs)
    res = s.get(url=v.URL, params=option, timeout=10)
    # resJson = json.dumps(res.content)
    return eval(res.content)


def getDailyActive(name, **kwargs):
    """
     'result': [{'name': 'android', 'subtype': '\xe6\x97\xa5\xe6\xb4\xbb\xe8\xb7\x83', 'date': '2016-09-27 00:00:00.0',
     'count1': '27291', 'count2': '0', 'type': 241},
    """
    option = {
        "type": type,
        "subtype": "日活跃",
        "start": "",
        "end": "",
    }
    option.update(kwargs)
    res = getApi(**option)
    if res.get("status") is 1:
        for r in res.get("result"):
            if r.get("name") == name:
                return r.get("count1")
    else:
        return False

def getAveDailyActive(name, **kwargs):
    """
     'result': [{'name': 'android', 'subtype': '\xe6\x97\xa5\xe6\xb4\xbb\xe8\xb7\x83', 'date': '2016-09-27 00:00:00.0',
     'count1': '27291', 'count2': '0', 'type': 241},
    """
    option = {
        "type": type,
        "subtype": "日活跃",
        "start": v.START,
        "end": v.END,
    }
    option.update(kwargs)
    res = getApi(**option)
    countList = []
    if res.get("status") is 1:
        for r in res.get("result"):
            if r.get("name") == name:
                count = r.get("count1")
                if count.isdigit():
                    countList.append(int(count))
    countAve = reduce(lambda x, y: x + y, countList)/float(len(countList))
    return int(round(countAve))


def getAveClientAPPDailyActive(name, **kwargs):
    """
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
    countList = []
    if res.get("status") is 1:
        for r in res.get("result"):
            if r.get("name") == name:
                count = r.get("count1")
                if count.isdigit():
                    countList.append(int(count))
    countAve = reduce(lambda x, y: x + y, countList)/float(len(countList))
    return int(round(countAve))


def getAveCrashDaily(name, subtype, **kwargs):
    """
    {"status":1,"result":[{"count1":"758","count2":"0","date":"2016-09-21 00:00:00.0","name":"app-kernel","subtype":"CrashLog次数","type":482}
    """
    option = {
        "type": v.CRASH_KERNEL,
        "subtype": subtype,
        "start": v.START,
        "end": v.END,
    }
    option.update(kwargs)
    res = getApi(**option)
    countList = []
    if res.get("status") is 1:
        for r in res.get("result"):
            if r.get("name") == name:
                count = r.get("count1")
                if count.isdigit():
                    countList.append(int(count))
    countAve = reduce(lambda x, y: x + y, countList)/float(len(countList))
    return int(round(countAve))


def getVersionMostUsed():


if __name__ == '__main__':
    # print getAveDailyActive("rom", **{"type": v.R1CM})
    # print getAveDailyActive("rom", **{"type": v.R1D})
    # print getAveDailyActive("rom", **{"type": v.R2D})
    # print getAveDailyActive("rom", **{"type": v.R1CL})
    # print getAveDailyActive("rom", **{"type": v.R3})
    # print getAveDailyActive("rom", **{"type": v.R3L})
    # print getAveClientAPPDailyActive("android")
    # print getAveClientAPPDailyActive("ios")
    # print getAveClientAPPDailyActive("mac")

    # print getAveCrashDaily("R1CM-kernel", "CrashLog次数")
    # print getAveCrashDaily("R1D-kernel", "CrashLog次数")
    # print getAveCrashDaily("R2D-kernel", "CrashLog次数")
    # print getAveCrashDaily("R1CL-kernel", "CrashLog次数")
    # print getAveCrashDaily("R3-kernel", "CrashLog次数")
    # print getAveCrashDaily("R3L-kernel", "CrashLog次数")
    # print getAveCrashDaily("app-kernel", "CrashLog次数")
    # print getAveCrashDaily("ios-kernel", "CrashLog次数")
    # print getAveCrashDaily("R1CM-kernel", "CrashLog用户数")
    # print getAveCrashDaily("R1D-kernel", "CrashLog用户数")
    # print getAveCrashDaily("R2D-kernel", "CrashLog用户数")
    # print getAveCrashDaily("R1CL-kernel", "CrashLog用户数")
    # print getAveCrashDaily("R3-kernel", "CrashLog用户数")
    # print getAveCrashDaily("R3L-kernel", "CrashLog用户数")
    # print getAveCrashDaily("app-kernel", "CrashLog用户数")
    # print getAveCrashDaily("ios-kernel", "CrashLog用户数")

    print getAveCrashDaily("R1CM-app", "CrashLog次数")
    print getAveCrashDaily("R1D-app", "CrashLog次数")
    print getAveCrashDaily("R2D-app", "CrashLog次数")
    print getAveCrashDaily("R3-app", "CrashLog次数")
    print getAveCrashDaily("R1CM-app", "CrashLog用户数")
    print getAveCrashDaily("R1D-app", "CrashLog用户数")
    print getAveCrashDaily("R2D-app", "CrashLog用户数")
    print getAveCrashDaily("R3-app", "CrashLog用户数")