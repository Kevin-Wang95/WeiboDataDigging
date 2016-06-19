from urllib import request
import time


f = open('2016-05-27_16-47-31_dis_id','r')
f2 = open('Disscusser_Weibo.txt','w')
data = f.read()
data = data.split()
for uid in data:
	url = 'http://m.weibo.cn/page/json?containerid=100505%s_-_WEIBO_SECOND_PROFILE_WEIBO&page=%s' % (uid,1)
	req = request.Request(url)
	req.add_header('User-Agent','Mozilla/5.0 (iPhone; CPU iPhone OS 9_1 like Mac OS X) AppleWebKit/601.1.46 (KHTML, like Gecko) Version/9.0 Mobile/13B143 Safari/601.1')
	response = request.urlopen(req)
	data = response.read()
	f2.write(bytes.decode(data) + '\n')
	time.sleep(0.5)
f2.close()
f.close()
