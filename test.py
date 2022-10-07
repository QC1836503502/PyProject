import requests
import random
import time
import mymodule
import merge
mymodule.zqip()
merge.hb()
a = open("export/combo.txt","r")
pd = input("是否进行不停歇工作(y/n):")
if pd == "y":
    print("开始不停歇工作")
    while True:
        for x in a:
            http_ip = [
                x
            ]
            time.sleep(3)
            for i in range(10):
                try:
                    ip_proxy = random.choice(http_ip)
                    proxy_ip = {
                        'http': ip_proxy,
                        'https': ip_proxy,
                    }
                    print('使用代理的IP:', proxy_ip)
                    response = requests.get("http://httpbin.org/ip", proxies=proxy_ip).text
                    print(response)
                    print('当前IP有效')
                    break
                except Exception as e:
                    print(e.args[0])
                    print('当前IP无效')
                    break
else:
    for x in a:
        http_ip = [
            x
        ]
        time.sleep(3)
        for i in range(10):
            try:
                ip_proxy = random.choice(http_ip)
                proxy_ip = {
                    'http': ip_proxy,
                    'https': ip_proxy,
                }
                print('使用代理的IP:', proxy_ip)
                response = requests.get("http://httpbin.org/ip", proxies=proxy_ip).text
                print(response)
                print('当前IP有效')
                break
            except Exception as e:
                print(e.args[0])
                print('当前IP无效')
                break

