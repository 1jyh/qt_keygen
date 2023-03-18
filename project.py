from hashlib import md5
import time
import requests
import json
import random
from utils import aes

class main():
    def __init__(self):
        self.key='l8N2iooyp07M9IWa'
        self.url='http://apichlove.com'

    def x_t(self,url):
        a = []
        b = []
        # url = 'app/api/auth/login/device'
        v1 = str(int(time.time()))
        v2 = md5(v1.encode()).hexdigest()[:8]
        a.append('md5')
        a.append(self.key)
        a.append(v1)
        a.append(v2)
        a.append(url)
        v3 = '|'.join(a)
        v3 = md5(v3.encode()).hexdigest()
        b.append('md5')
        b.append(v1)
        b.append(v2)
        b.append(v3)
        return '|'.join(b)

    def getRandom(self,randomlength=16):
        digits = '0123456789'
        ascii_letters = 'abcdefghigklmnopqrstuvwxyz'
        str_list = [random.choice(digits + ascii_letters) for i in range(randomlength)]
        random_str = ''.join(str_list)
        return random_str

    def token(self):
        device_id = 'b2ad30fc-0301-3d50-a97f-' + self.getRandom(12)
        data = json.dumps({"channel": "", "code": "", "device_no": device_id, "device_type": "A", "version": "1.0.0"})
        data = {'data': aes.encrypt(data, self.key), 'handshake': 'v20200429'}
        header = {'X-JSL-API-AUTH': self.x_t('/app/api/auth/login/device')}
        result = requests.post(self.url + '/app/api/auth/login/device', json=data, headers=header).text
        print(result)
        if not result:
            print('result==null',result)
            return '',''
        try:
            result = json.loads(result)
            msg = aes.decrypt(result['data'], self.key)
        except Exception as e:
            print(result)
            return '',''
        return json.loads(msg)['auth']['token'], device_id

    def x_token(self, device_id, token):
        Json = json.dumps({"device_no": device_id, "device_type": "A", "token": token, "version": "1.0.0"})
        return aes.encrypt(Json, self.key)

    def parent(self, code,x):
        token, device_id = self.token()
        if not ( token or device_id):
            self._signal.emit('----'.join(map(str, ['','', 'error', x])))
            return
        data = {'data': aes.encrypt(json.dumps({'code': code}), self.key), 'handshake': 'v20200429'}
        header = {'X-JSL-API-AUTH': self.x_t('/app/api/user/bindcode'),
                  'X-TOKEN': self.x_token(device_id=device_id, token=token)}
        result = requests.post(self.url + '/app/api/user/bindcode', json=data, headers=header).text
        try:
            result = json.loads(result)
        except Exception as e:
            self._signal.emit([device_id,'','','error', x])
            return
        self._signal.emit([device_id, '', '', 'succes', x]) if result['code'] == 200 else self._signal.emit([device_id, '', '', 'error', x])
        # print(result)
        # self._signal.emit([device_id, '', '', 'error', x])
        # print(self.decrypt(result['data'], self.key))
        # header['X-JSL-API-AUTH'] = self.x_t('/app/api/user/info')
        # 你的X-TOKEN
        # header['X-TOKEN']='4LJnAngoza8TZIz2otKTe52PhqbrW8GULUYVUu87AjDKzXQWPzNCDiHTohcbTWRcJ5V+mdgxrLVskUbLae90njTJJk4bG8tqYcgDX/fhwwG0VkkB11CY0wLhlxPfSkfMSlqmArvVTbrJ7UiydzotGh9nUHVrBqxMbDy9+iuhq9pFmucuV1SRKd/1pGxDNI0UX9nA5mpYMfYih0N/vR3A6+AdHQASRqBpeXSfMj3M7fHY/5W4fj0esNHkw93KjsnWM2FJWdNCYrkZC3tHWipUqKTk7zvbx20zaWo/c78VuePh8OeiCV2Htt9ah8+MNvAu+o6TERNF13aavGJkxeptaZs/+PFbBa397NVD4zQ28QDhkuOthPwHbpvOL/cWm9rjoL7TH7BdKGqjbYzHTvUnpWHQtJhGTPXRdNdSklDv4UDW/nsKTVVcv1LQAU1Oo5EnMwfZF2wmTtIRMRTPIi9zYFVhTYlJeFroe2fWrl8H9afzxz+fP+tm5aGSa7Ll0RBitPmN364On3xaWrRIiYGvfYsqckb6+BRQyDMXI+nHUMOAR2EcT6U3BMUCN5VJnkX8atWL76jdqPlFZzS9zyo5yaeiNLnQzVYm9wxNPuzb9ZMgvRQ4TnXfBGE5t8BiE4jAPJczvQhvWseHNy3M3wCd5b7CavKAVznoovCoLaqJpRX+bOWnttUWMLqdYxBnweL3'
        # result=requests.post(url+'/app/api/user/info',data='{"handshake":"v20200429"}',headers=header).json()
        # print(json.loads(decrypt(result['data'],key))['vip_expired'])

# from concurrent.futures import ThreadPoolExecutor
# # 邀请码
# m=main()
# # for i in range(1):
# #     m.parent('RWK6IF',1)
# with ThreadPoolExecutor(max_workers=1) as t:
#     for x in range(5):
#         t.submit(m.parent, ('RWK6IF', x))

    # https: // d.ajwool5.com?code = RWK6IF & channel = share
    # https: // d.ajtk88.com?code = RWK6IF & channel = share
#     https://d.ajgg52.com?code=RWK6IF&channel=share
