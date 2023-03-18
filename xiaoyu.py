import requests
class lianz():
	def __init__(self):
		self.headers={
			'POSThttps':'//v2-api.jsdama.com/uploadHTTP/1.1',
			'Host':'v2-api.jsdama.com',
			'Connection':'keep-alive',
			'Content-Length':'298',
			'Accept':'application/json,text/javascript,*/*;q=0.01',
			'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36 Edg/91.0.864.67',
			'Content-Type':'text/json'}
	def login(self,username,password):
		'''联众点数->
		账号,密码
		成功返回点数,其余false
		'''
		#data['softwareSecret']   开发者token
		data={
			'softwareId':'24472',
			'softwareSecret':'MoVVI1sOIbzlIIzNYPoQaomLZlZ5wYu75yxjgy1h',
			'username':username
			,'password':password}
		if(username and password):
			result=requests.post('https://v2-api.lz25.com/check-points',json=data,headers=self.headers,timeout=5).json()
			return result['data']['availablePoints'] if(result['code']==0) else False
		else:
			return False
	def upload(self,username,password,pic_base,captchaType=1038):
		'''识别验证码->
		账号,密码,图片base64,类型(默认英数混合->1038,纯数字->1043)
		成功返回code'''
		if(username and password and captchaType and pic_base):
			data={
				'softwareId':'24472',
				'softwareSecret':'MoVVI1sOIbzlIIzNYPoQaomLZlZ5wYu75yxjgy1h',
				'username':username,
				'password':password,
				'captchaData':pic_base,
				'captchaType':captchaType
				}
			result=requests.post('https://v2-api.jsdama.com/upload',json=data,headers=self.headers,timeout=5).json()
			return result['data']['recognition'] if result['code']==0 else False
		else:
			return False
class miyun():
	def login(self,username,password):
		"""登录->
		账号,密码必传
		正确返回token,其余false"""
		if(username and password):
			result=requests.get('http://api.miyun.pro/api/login?apiName={}&password={}'.format(username,password),timeout=5).json()
			return result['token'] if(result['message']=='ok') else False
		else:
			return False
	def get_info(self,token):
		"""用户信息->token必传
		正确返回余额,其余false"""
		if(token):
			result=requests.get('http://api.miyun.pro/api/get_myinfo?token={}'.format(token),timeout=5).json()
			return result['money'] if(result['message']=='ok') else False
		else:
			return False
	def get_phone(self,token,project_id,operator=4,scope='',scope_black=''):
		"""取号->token,id必传,operator默认实卡(随机0,实卡4,虚卡5),指定-排除号段(176,178)
		返回手机号,其余message"""
		if(token and project_id):
			result=requests.get('http://api.miyun.pro/api/get_mobile?token={}&project_id={}&operator={}&scope={}&scope_black={}&api_id=xiaoyu_'.format(token,project_id,operator,scope,scope_black),timeout=5).json()
			return result['mobile'] if(result['message']=='ok') else False
		else:
			return False
	def get_message(self,token,project_id,phone):
		"""取码->token,项目id,手机号
		返回code,其余false"""
		if(token and project_id and phone):
			result=requests.get('http://api.miyun.pro/api/get_message?token={}&project_id={}&phone_num={}'.format(token,project_id,phone),timeout=5).json()
			return result['code'] if(result['message']=='ok') else False
		else:
			False
	def add_blacklist(self,token,project_id,phone):
		"""加黑->token,项目id,手机号
		返回true,其余false"""
		if(token and project_id and phone):
			result=requests.get('http://api.miyun.pro/api/add_blacklist?token={}&project_id={}&phone_num={}'.format(token,project_id,phone),timeout=5).json()
			return True if(result['message']=='ok') else False
		else:
			False
	def free_mobile(self,token,project_id,phone):
		"""释放->token,项目id,手机号
		返回true,其余false"""
		if(token and project_id and phone):
			result=requests.get('http://api.miyun.pro/api/free_mobile?token={}&project_id={}&phone_num={}'.format(token,project_id,phone),timeout=5).json()
			return True if(result['message']=='ok') else False
		else:
			False
class ip():
	def __white_list(self):
		result=requests.get('http://op.xiequ.cn/IpWhiteList.aspx?uid=63206&ukey=2FFEA09A36E0ADC23B61800C117B24D1&act=get').text
		return result.split(',')
	def __add_white(self,IP):
		result=requests.get('http://op.xiequ.cn/IpWhiteList.aspx?uid=63206&ukey=2FFEA09A36E0ADC23B61800C117B24D1&act=add&ip={}'.format(IP)).text
		return True if result=='success' else False
	def __del_white(self,IP):
		result=requests.get('http://op.xiequ.cn/IpWhiteList.aspx?uid=63206&ukey=2FFEA09A36E0ADC23B61800C117B24D1&act=del&ip={}'.format(IP)).text
		return True if result=='success' else False
	def get_ip(self,num=1):
		'''返回ip,其余清空false'''
		if num:
			result=requests.get('http://api.xiequ.cn/VAD/GetIp.aspx?act=get&uid=63206&vkey=CD019F4E615E9CF8A0C12B1xxxxxx&num={}&time=30&plat=1&re=0&type=0&so=1&ow=1&spl=3&addr=&db=1'.format(num)).text
			return result.split('\n') if(result[0]!='D') else (self.get_ip(num) if(self.__add_white(result[12:])) else False) if(len(self.__white_list())!=5) else ((self.get_ip(num) if(self.__add_white(result[12:])) else False) if(self.__del_white(self.__white_list()[4])) else False)
		else:
			return False
if __name__ == '__main__':
	print(ip().get_ip(2))