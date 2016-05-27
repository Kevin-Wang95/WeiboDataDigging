from urllib import request
import math
import time

t = time.strftime("%Y-%m-%d_%H-%M-%S", time.localtime())

# Getting fans list
url = 'http://m.weibo.cn/page/pageJson?containerid=&containerid=230403_-_10080894a92ca39febc7c72d0d29606cddf0f0&title=%E7%B2%89%E4%B8%9D&uid=5412999676&from=feed&luicode=10000011&lfid=10730394a92ca39febc7c72d0d29606cddf0f0_-_ext_intro&v_p=11&ext=&fid=230403_-_10080894a92ca39febc7c72d0d29606cddf0f0&uicode=10000011&next_cursor=&page='
f = open('Fans_Data_' + t + '.json' ,'w')
for i in range(1,501):
	url1 = url + str(i)
	print(i)
	req = request.Request(url1)
	req.add_header('Accept','application/json, text/javascript, */*; q=0.01')
	req.add_header('Accept-Language','zh-CN,zh;q=0.8')
	req.add_header('Host','m.weibo.cn')
	req.add_header('Cookie','_T_WM=ac89bd37885b03c26730c73afa448a1f; SUB=_2A256QqmUDeRxGeNK6lAY-SfKzDqIHXVZzDfcrDV6PUJbrdBeLWLikW1LHeubAfMH57LpHvd8nofkUoTd2HccKw..; SUHB=0WGchh-nGfb4uf; gsid_CTandWM=4urXCpOz5w5ZwCxb0idJ9mIaraU; H5_INDEX=2; H5_INDEX_TITLE=%E6%B5%81%E4%BC%BC%E9%A3%8E%E8%8B%A5%E6%B0%B5%E5%BD%B1; browser=d2VpYm9mYXhpYW4%3D; h5_deviceID=0f335b4c4acbc61c4eb49deaa2342427; M_WEIBOCN_PARAMS=from%3Dfeed%26luicode%3D10000011%26lfid%3D10730394a92ca39febc7c72d0d29606cddf0f0_-_ext_intro%26fid%3D230403_-_10080894a92ca39febc7c72d0d29606cddf0f0%26uicode%3D10000011')
	req.add_header('X-Requested-With','With:XMLHttpRequest')
	req.add_header('Referer','http://m.weibo.cn/p/index?containerid=230403_-_10080894a92ca39febc7c72d0d29606cddf0f0&containerid=230403_-_10080894a92ca39febc7c72d0d29606cddf0f0&title=%E7%B2%89%E4%B8%9D&uid=5412999676')
	req.add_header('User-Agent','Mozilla/5.0 (iPhone; CPU iPhone OS 9_1 like Mac OS X) AppleWebKit/601.1.46 (KHTML, like Gecko) Version/9.0 Mobile/13B143 Safari/601.1')
	response = request.urlopen(req)
	data = response.read()
	f.write(bytes.decode(data) + '\n')
	time.sleep(0.5)

f.close();

#Getting discussion list
url_ = 'http://m.weibo.cn/page/pageJson?containerid=10080894a92ca39febc7c72d0d29606cddf0f0&from=feed&containerid=100808topic&extparam=%E5%A4%A7%E5%AD%A6%E6%98%AF%E6%89%80%E6%95%B4%E5%AE%B9%E9%99%A2&v_p=11&ext=&fid=10080894a92ca39febc7c72d0d29606cddf0f0&uicode=10000011&next_cursor=&page='
f = open('Discussion_Data_' + t + '.json','w')
for i in range(1,101):
	url2 = url_ + str(i)
	print(i)
	req = request.Request(url2)
	req.add_header('Accept','application/json, text/javascript, */*; q=0.01')
	req.add_header('Accept-Language','zh-CN,zh;q=0.8')
	req.add_header('Host','m.weibo.cn')
	req.add_header('Cookie','_T_WM=ac89bd37885b03c26730c73afa448a1f; SUB=_2A256QqmUDeRxGeNK6lAY-SfKzDqIHXVZzDfcrDV6PUJbrdBeLWLikW1LHeubAfMH57LpHvd8nofkUoTd2HccKw..; SUHB=0WGchh-nGfb4uf; gsid_CTandWM=4urXCpOz5w5ZwCxb0idJ9mIaraU; H5_INDEX=2; H5_INDEX_TITLE=%E6%B5%81%E4%BC%BC%E9%A3%8E%E8%8B%A5%E6%B0%B5%E5%BD%B1; browser=d2VpYm9mYXhpYW4%3D; h5_deviceID=0f335b4c4acbc61c4eb49deaa2342427; M_WEIBOCN_PARAMS=from%3Dfeed%26fid%3D10080894a92ca39febc7c72d0d29606cddf0f0%26uicode%3D10000011')
	req.add_header('X-Requested-With','With:XMLHttpRequest')
	req.add_header('Referer','http://m.weibo.cn/k/%E5%A4%A7%E5%AD%A6%E6%98%AF%E6%89%80%E6%95%B4%E5%AE%B9%E9%99%A2?from=feed')
	req.add_header('User-Agent','Mozilla/5.0 (iPhone; CPU iPhone OS 9_1 like Mac OS X) AppleWebKit/601.1.46 (KHTML, like Gecko) Version/9.0 Mobile/13B143 Safari/601.1')
	response = request.urlopen(req)
	data = response.read()
	f.write(bytes.decode(data) + '\n')

f.close();
