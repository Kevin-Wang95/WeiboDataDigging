import urllib.parse , urllib.request , http.cookiejar, time, json

cookie = http.cookiejar.LWPCookieJar()
opener = urllib.request.build_opener(urllib.request.HTTPCookieProcessor(cookie),urllib.request.HTTPHandler)
urllib.request.install_opener(opener)

cookiestr = '_T_WM=4a59373a7fdee76828ffb802d51ce077; gsid_CTandWM=4umjCpOz5EK63ILxrxZRfoglp2Q; SUB=_2A256S66GDeTxGeNJ41ES-SvLyTuIHXVZtzLOrDV6PUJbkdBeLRn3kW1FMDvb4NtDHSq05yansKQFdMznyw..; SUHB=0TPFvnaV0r0HNb; SSOLoginState=1464852182; M_WEIBOCN_PARAMS=featurecode%3D20000181%26luicode%3D10000011%26lfid%3D1005052480140482%26uicode%3D20000174'

f = open('2016-05-27_16-47-31_user_id.txt', 'r')
data = f.read()
data = data.split()
i=1
for k in range(2446 ,4975):
    #43
    uid = data[k]
    fp = open('E:\\Users_Followers\\'+uid+'.txt' , 'w' , encoding = 'utf-8')
    j=1
    num=100
    print('\n')
    print(i)
    print('\n')
    while (j<=num):
        #text = getData('http://weibo.com/p/103505'+uid+'/follow?pids=Pl_Official_HisRelation__62&page='+str(j)+'&ajaxpagelet=1&ajaxpagelet_v6=1&__ref=%2Fp%2F1035051771140437%2Ffollow%3Fpage%3D3%23Pl_Official_HisRelation__62&_t=FM_146468472447524')
        request = urllib.request.Request('http://m.weibo.cn/page/json?containerid=100505' + uid + '_-_FOLLOWERS&page='+ str(j))
        request.add_header('Cookie',cookiestr)
        request.add_header('Connection','keep-alive')
        request.add_header('Host','m.weibo.cn')
        request.add_header('Accept','application/json, text/javascript, */*; q=0.01')
        request.add_header('User-Agent','Mozilla/5.0 (iPhone; CPU iPhone OS 9_1 like Mac OS X) AppleWebKit/601.1.46 (KHTML, like Gecko) Version/9.0 Mobile/13B143 Safari/601.1')
        response = urllib.request.urlopen(request)
        text = response.read().decode('utf-8')
        if j==1:
            decodejson = json.loads(text)
            decodejson = decodejson['cards'][0]
            num = decodejson['maxPage']
            print(num)
        fp.write(text)
        fp.write('\n')
        print(j)
        j=j+1
    i=i+1
    fp.close()
