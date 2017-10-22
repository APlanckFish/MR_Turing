import requests
import itchat
def Turing_response(msg):
	apiUrl="http://www.tuling123.com/openapi/api"
	data = {
	    'key'    : '7f5b71d6ecc548fc861ce5de63df85eb', # 我申请的图灵key
	    'info'   : msg, # 这是我们发出去的消息
	    'userid' : 'APlanckFish', # 我的名字
	}
	try:
		r=requests.post(apiUrl,data=data).json()
		return r.get('text')
	except:
		return None
# 这是与图灵服务器交互的程序

@itchat.msg_register(itchat.content.TEXT)
def turing_reply(msg):
	defaultReply="我收到了:"+msg['Text']
	#设置默认回复，防止服务器无响应
	reply=Turing_response(msg['Text'])
	#调用图灵服务器回复
	return reply or defaultReply
	#a or b 意思是如果a不为None，则返回a，否则返回b
itchat.auto_login(hotReload=True)
itchat.run()