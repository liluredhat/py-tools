# coding=utf-8
'''
Created on Jul 3, 2017

@author: lilu
'''
import re
import urllib

def getHtml(url): 
    try: 
        page = urllib.urlopen(url)  
        html = page.read()  
        return html
    except Exception, e:
        print Exception, ":", e   

def process(ourl, url):
    # print ourl + "||||||||||" + url
    if (url.startswith("http://")):
        return url
    else:
        pos = ourl.rfind("/")
        # print ourl[0:pos]
        return ourl[0:pos] + url

# 此方法只能爬取网页链接性的url，不能爬取js动态生成的url  
def getUrl(index, ourl, html):
    try:
        # print index  
        reg = r'href="(.+?)"'  
        urlpattern = re.compile(reg)  
        urllist = re.findall(urlpattern, html)
        # 输出目标文件 
        x = 0
        filename = ("output.txt")
        #print filename  
        fobj = open(filename, 'a')
        # print urllist
        for url in urllist:
            # print x
            if (url == "#" or url.startswith("javascript") or url.endswith("css")):
              continue
            else:
              print >> fobj, process(ourl, url)
              # print url  
              # urllib.urlretrieve(url,'%s.jpg' % x)  
              x += 1
        fobj.close()
    except Exception, e:
        print Exception, ":", e 
        
if __name__ == '__main__':
    file = open("input.txt")
    lines = file.readlines()
    # print lines
    index = 0
    for line in lines:
        line = line.strip('\n')
        if len(line) == 0:
           continue
        else:
           index += 1
           print line + "......"
           getUrl(index, line, getHtml(line))
    # webaddress = "http://wsbs.gz.gov.cn/gz/index.jsp"  
    # webaddress = raw_input("Input the Website Address(without \"http:\")>")  
    # html = getHtml(webaddress)
    # print html
    # getUrl(html)
    file.close()  
    print "success."  # 代码执行完毕之后打印此提示信息 
