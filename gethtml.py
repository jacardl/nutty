#coding=utf8
__author__ = 'Jac'
import requests
import json

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
        "start": "",
        "end": "",
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
    countAve = reduce(lambda x, y: x + y, countList)/len(countList)
    return countAve

if __name__ == '__main__':
    params = {
        "type": "241",
        "subtype": "总用户",
        "start": "2016-09-21",
        "end": "2016-09-21",
    }
    res = getAveDailyActive("rom", **params)
    print res, type(res)

