"""
套接字 - 基于TCP协议创建时间客户端

Version: 0.1
Author: 骆昊
Date: 2018-03-22
"""


from socket import *

client = socket(AF_INET, SOCK_STREAM)
client.connect(('localhost', 6789))
while True:
    if data := client.recv(1024):
        print(data.decode('utf-8'))
    else:
        break
client.close()
