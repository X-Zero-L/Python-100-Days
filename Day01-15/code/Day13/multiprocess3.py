"""
创建进程调用其他程序

Version: 0.1
Author: 骆昊
Date: 2018-03-20
"""

import subprocess
import sys

def main():
    # 通过sys.argv获取命令行参数
    if len(sys.argv) > 1:
        # 第一个命令行参数是程序本身所以从第二个开始取
        for index in range(1, len(sys.argv)):
            try:
                # 通过subprocess模块的call函数启动子进程
                status = subprocess.call(sys.argv[index])
            except FileNotFoundError:
                print(f'不能执行{sys.argv[index]}命令')
    else:
        print('请使用命令行参数指定要执行的进程')


if __name__ == '__main__':
    main()
