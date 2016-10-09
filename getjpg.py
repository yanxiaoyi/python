#--简易爬虫小程序--#
#--author：颜筱祎--#
import urllib.request
import  urllib
import  re
page = urllib.request.urlopen("http://www.ly.com/")
html = page.read().decode("utf8")
reg=r'src="(.+?\.jpg)" pic_ext'
image=re.compile(reg)
imglist=re.findall(image,html)
x=0
for imgurl in imglist:
    urllib.request.urlretrieve(imgurl,'E:/%s.jpg' % x)
    x=x+1

print(html)
