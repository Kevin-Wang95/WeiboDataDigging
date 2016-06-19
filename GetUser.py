import re , urllib.parse , urllib.request , http.cookiejar, base64 , binascii, rsa, time

cookie = http.cookiejar.LWPCookieJar()
opener = urllib.request.build_opener(urllib.request.HTTPCookieProcessor(cookie),urllib.request.HTTPHandler)
urllib.request.install_opener(opener);
#opener.open('https://passport.weibo.cn/signin/login?entry=mweibo&res=wel&wm=3349&r=http%3A%2F%2Fm.weibo.cn%2F')
def getData(url) :
    request = urllib.request.Request(url)
    response = urllib.request.urlopen(request)
    text = response.read().decode('utf-8')
    return text

def postData(url , data) :
    headers = {'User-Agent' : 'Mozilla/5.0 (iPhone; CPU iPhone OS 9_1 like Mac OS X) AppleWebKit/601.1.46 (KHTML, like Gecko) Version/9.0 Mobile/13B143 Safari/601.1'}
    data = urllib.parse.urlencode(data).encode('utf-8')
    request = urllib.request.Request(url , data , headers)
    response = urllib.request.urlopen(request)
    text = response.read().decode('gbk')
    return text

def login_weibo(nick , pwd):
	prelogin_url = 'http://login.sina.com.cn/sso/prelogin.php?entry=weibo&callback=sinaSSOController.preloginCallBack&su=%s&rsakt=mod&checkpin=1&client=ssologin.js(v1.4.15)&_=1400822309846' % nick
	preLogin = getData(prelogin_url)
	servertime = re.findall('"servertime":(.*?),' , preLogin)[0]
	pubkey = re.findall('"pubkey":"(.*?)",' , preLogin)[0]
	rsakv = re.findall('"rsakv":"(.*?)",' , preLogin)[0]
	nonce = re.findall('"nonce":"(.*?)",' , preLogin)[0]
	su = base64.b64encode(bytes(urllib.request.quote(nick) , encoding = 'utf-8'))
	rsaPublickey = int(pubkey , 16)
	key = rsa.PublicKey(rsaPublickey , 65537)
	message = bytes(str(servertime) + '\t' + str(nonce) + '\n' + str(pwd) , encoding = 'utf-8')
	sp = binascii.b2a_hex(rsa.encrypt(message , key))
	param = {'entry' : 'weibo' , 'gateway' : 1 , 'from' : '' , 'savestate' : 7 , 'useticket' : 1 , 'pagerefer' : 'http://login.sina.com.cn/sso/logout.php?entry=miniblog&r=http%3A%2F%2Fweibo.com%2Flogout.php%3Fbackurl%3D' , 'vsnf' : 1 , 'su' : su , 'service' : 'miniblog' , 'servertime' : servertime , 'nonce' : nonce , 'pwencode' : 'rsa2' , 'rsakv' : rsakv , 'sp' : sp , 'sr' : '1680*1050' ,
             'encoding' : 'UTF-8' , 'prelt' : 961 , 'url' : 'http://weibo.com/ajaxlogin.php?framelogin=1&callback=parent.sinaSSOController.feedBackUrlCallBack'}
	s = postData('http://login.sina.com.cn/sso/login.php?client=ssologin.js(v1.4.15)' , param)
	urll = re.findall("location.replace\(\'(.*?)\'\);" , s)[0]
	getData(urll)





login_weibo('18813119733' , '95102200')
f = open('2016-05-27_16-47-31_user_id.txt', 'r')
#f2 = open('Follower_info2.txt','wb')
data = f.read()
data = data.split()
i=1
for j in range(1,4936):
	uid = data[j]
	text = getData('http://weibo.com/p/100505'+uid+'/info?mod=pedit_more')
	fp = open('E:\\UserInfo\\'+uid+'.txt' , 'w' , encoding = 'utf-8')
	fp.write(text)
	fp.close()
	print(i)
	i=i+1
	time.sleep(0.5)
#	url = 'http://m.weibo.cn/users/%s' % uid
#	req = urllib.request.Request(url)
#	req.add_header('Accept','text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8')
#	req.add_header('Accept-Encoding','gzip, deflate, sdch')
#	req.add_header('Accept-Language','zh-CN,zh;q=0.8')
#	req.add_header('Cache-Control','max-age=0')
#	req.add_header('Upgrade-Insecure-Requests','1')
#	req.add_header('User-Agent','Mozilla/5.0 (iPhone; CPU iPhone OS 9_1 like Mac OS X) AppleWebKit/601.1.46 (KHTML, like Gecko) Version/9.0 Mobile/13B143 Safari/601.1')
#	response = urllib.request.urlopen(req)
#	data = response.read()
#	f2.write(bytes.decode(data) + '\n')
#	print(i)
#	i=i+1
#	time.pause(0.5)
#f2.close()
#f.close()

