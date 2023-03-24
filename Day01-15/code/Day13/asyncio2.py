"""
异步I/O操作 - async和await

Version: 0.1
Author: 骆昊
Date: 2018-03-21
"""
import asyncio
import threading


# 通过async修饰的函数不再是普通函数而是一个协程
# 注意async和await将在Python 3.7中作为关键字出现
async def hello():
    print(f'{threading.current_thread()}: hello, world!')
    await asyncio.sleep(2)
    print(f'{threading.current_thread()}: goodbye, world!')


loop = asyncio.get_event_loop()
tasks = [hello(), hello()]
# 等待两个异步I/O操作执行结束
loop.run_until_complete(asyncio.wait(tasks))
loop.close()
