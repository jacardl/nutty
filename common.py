__author__ = 'Jac'

def checkContainChinese(string):
    checkstr = unicode(string, 'utf8')
    for ch in checkstr:
        if u'\u4e00' <= ch <= u'\u9ffff':
            return True
    return False
