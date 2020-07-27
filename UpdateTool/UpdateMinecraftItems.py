from bs4 import BeautifulSoup,element
import urllib.request
import urllib.parse
import gzip
import io

'''
这是一个用从BukkitAPI文档获取最新物品列表的工具。
'''

def getCode(url, UserAgent='Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:59.0) Gecko/20100101 Firefox/59.0', Cookie=''):
    """
    获取http内容
    :param url: URL
    :param UserAgent: 浏览器UserAgent
    :param Cookie: Cookie
    :return: 内容
    """
    try:
        host = url.split('//')[1].split('/')[0].split('?')[0]
    except IndexError:
        raise TypeError("请输入一个带协议头的链接，如：“https://www.bilibili.com”")
    cookieDict = {}
    if bool(Cookie):
        cookieDict = {'Cookie': Cookie}
    response = urllib.request.urlopen(urllib.request.Request(url, headers=dict({
        'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8',
        'Accept-Encoding': 'gzip, deflate', 'Connection': 'keep-alive',
        'Accept-Language': 'zh-CN,zh;q=0.8,zh-TW;q=0.7,zh-HK;q=0.5,en-US;q=0.3,en;q=0.2', 'Cache-Control': 'max-age=0',
        'Content-Type': 'application/x-www-form-urlencoded', 'Host': host, 'Referer': url,
        'User-Agent': UserAgent}, **cookieDict)))
    raw = response.read()
    if response.getheader('Content-Encoding') == 'gzip':
        return gzip.GzipFile(fileobj=io.BytesIO(raw)).read().decode("utf-8")
    else:
        return raw


def getEnums(page):
    """
    获取BukkitAPI文档中枚举类的枚举。
    https://hub.spigotmc.org/javadocs/bukkit/index.html
    :param page:
    :return:
    """
    print("\n本次运行数据来源于：\n%s" % page)
    enums = []
    soup = BeautifulSoup(getCode(page), "html.parser")
    print("\n页面标题：\n%s\n" % soup.find("title").text)
    for item in soup.find("section", "constantsSummary").table.tbody:
        if type(item) != element.NavigableString:
            enums.append(item.th.code.span.a.text.lower())
    return enums


print("\n数据来源于BukkitAPI：\nhttps://hub.spigotmc.org/javadocs/bukkit/index.html")

if __name__ == '__main__':
    print(getEnums("https://hub.spigotmc.org/javadocs/bukkit/org/bukkit/Material.html"))
