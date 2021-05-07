import requests


class RequestApi:

    def __init__(self, url, data, method, headers=None):

        self.url = url
        self.method = method
        self.headers = headers
        self.data = data

    def req(self):
        if self.method.upper() == 'GET':
            res = requests.get(url=self.url, params=self.data)
            return res.text
        else:
            res = requests.post(url=self.url, json=self.data, headers=self.headers)
            return res.text


if __name__ == '__main__':
    #地址是我本地写的一个平台化的接口测试工具
    url = 'http://127.0.0.1:8000/login_action/'
    data = {'username': 'admin', 'password': 'admin'}
    method = 'get'
    req = RequestApi(url=url, data=data, method=method).req()
    print(req)
