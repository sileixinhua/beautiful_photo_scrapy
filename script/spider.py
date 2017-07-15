# 时间:2017年7月13日17:39:57
# silei
# http://www.zjito.com/
# 爬取妹子图片 bs4 + re + gevent 多线程爬虫
# 存储文件地址为 '../photo'

import requests
from bs4 import BeautifulSoup
import urllib
import gevent
from gevent import Greenlet
import socket
import random

def cbk(a,b,c):  
    '''''回调函数 
    @a:已经下载的数据块 
    @b:数据块的大小 
    @c:远程文件的大小 
    '''  
    per=100.0*a*b/c  
    if per>100:  
        per=100  
    print('%.2f%%' % per)

def photo_download(photo_thread, index_number, photo_number, number):
	while number < 3564 :
		try:
			i = 0
			number = number + 1
			url = 'http://www.zjito.com/dqfl/'+dict[i]+'/'+str(index_number)+'.shtml?idx=1'
			# 爬虫目标网站地址
			headers = {'user-agent': 'my-app/0.0.1'}
			r = requests.get(url, headers=headers)
			# 获得目标页面返回信息
			print(r.status_code)
			print(url)
			while r.status_code == 404:
			# 判断响应状态码			
				i = i + 1
				url = 'http://www.zjito.com/dqfl/'+dict[i]+'/'+str(index_number)+'.shtml?idx=1'
				print(url)
			else :
				soup = BeautifulSoup(r.text, 'html.parser')
				# 返回的信息放入soup中
				# 获取页面全部标签信息
				# print(soup.prettify())
				# 测试显示的是否是页面的标签		
				for link in soup.find_all(class_="div-num"):
					print(link.get('data-src'))
					# 输出图片地址
					socket.setdefaulttimeout(3.0)
					# 设置超时
					photo_number = photo_number + 1
					urllib.request.urlretrieve(link.get('data-src'), file+'/'+str(photo_thread)+'_'+str(photo_number)+'.jpg', cbk)
					# 下载图片并显示下载进度
					gevent.sleep(random.randint(0,2)*0.001)
		except Exception as e:			
			index_number = index_number + 1
		index_number = index_number + 1
		
if __name__ == '__main__':
	dict = ['zgnd', 'tw', 'xg', 'rb', 'hg', 'mlxy', 'tg', 'om', 'hx',]
	# 照片分类
	photo_thread = [1, 2]
	# 线程计数器
	photo_number = -1
	# 下载图片计数器，最大50
	# index_number = 530273
	# 页面计数器，最小530273，最大544527
	file = '../photo/'
	# 图片的保存地址
	thread1 = Greenlet.spawn(photo_download, photo_thread[0], 530273, photo_number, 0)
	# 从命名中创建，并运行新的Greenlet的包装器
	# 函数photo_download，带有传递的参数
	thread2 = gevent.spawn(photo_download, photo_thread[1], 533836, photo_number, 0)
	# 两个thread运行，一个从530273页面开始爬取，另一个从537400页面开始爬取
	# 537400 - 530273 = 7127
	# 7127 / 2 = 3564
	# 3564 + 530273 = 533836
	threads = [thread1, thread2]
	# 阻止所有线程完成
	gevent.joinall(threads)