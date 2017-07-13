# 时间:2017年7月13日17:39:57
# silei
# http://www.zjito.com/
# 爬取妹子图片
# 存储文件地址为 '../photo/photo_1'

import requests
from bs4 import BeautifulSoup
import urllib

if __name__ == '__main__':
	photo_number = 0
	# 下载图片计数器，最大50
	index_number = 530273
	# 页面计数器，最小530273，最大544527
	file = '../photo/'
	# 图片的保存地址
	while index_number < 544527 :
		url = 'http://www.zjito.com/dqfl/zgnd/'+str(index_number)+'.shtml?idx=1'
		# 爬虫目标网站地址
		headers = {'user-agent': 'my-app/0.0.1'}
		r = requests.get(url, headers=headers)
		# 获得目标页面返回信息
		soup = BeautifulSoup(r.text, 'html.parser')
		# 返回的信息放入soup中
		# 获取页面全部标签信息
		# print(soup.prettify())
		# 测试显示的是否是页面的标签
		print(url)
		for link in soup.find_all(class_="div-num"):
			print(link.get('data-src'))
			# 输出图片地址
			urllib.request.urlretrieve(link.get('data-src'), file+'/'+str(photo_number)+'.jpg')
			# 下载图片
			photo_number = photo_number + 1
		index_number + index_number + 1