import requests
import random
import configparser

cf = configparser.ConfigParser()
cf.read("config.ini")
port = cf.get('clash api', 'port')
secret = cf.get('clash api', 'secret')
selector = cf.get('clash api', 'selector')

port = port
secret = secret
url_all_proxies = 'http://localhost:{}/proxies/{}'.format(port,selector)

def change_proxy(url_all_proxies):
    headers_secret = {
        'Authorization': 'Bearer {}'.format(secret)
    }
    res_proxies = requests.get(url_all_proxies,headers=headers_secret).json()
    now_proxy = res_proxies['now']
    print('现在的代理是{}'.format(now_proxy))
    proxy_name_list = res_proxies['all'][3:-3]
    if now_proxy not in ['DIRECT','REJECT','账号邮箱看最新的地址','NETV2','自动选择','故障转移']:
        proxy_name_list.remove(now_proxy)
    random_proxy = random.choice(proxy_name_list)
    print('随机选择的代理为{}'.format(random_proxy))
    data = {
        "name": random_proxy
    }
    headers = {
        "content-type": "application/json",
        'Authorization': 'Bearer {}'.format(secret)
    }
    res = requests.put(url=url_all_proxies,json=data,headers=headers)
    print('切换代理请求的状态码为{}'.format(res.status_code))
    if res.status_code == 204:
        print('切换代理成功！现在的代理为{}'.format(random_proxy))
if __name__ == '__main__':
    change_proxy(url_all_proxies=url_all_proxies)