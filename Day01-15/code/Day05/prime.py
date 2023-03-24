"""
输出2~99之间的素数

Version: 0.1
Author: 骆昊
Date: 2018-03-02
"""


import math

for num in range(2, 100):
    is_prime = all(
        num % factor != 0 for factor in range(2, int(math.sqrt(num)) + 1)
    )
    if is_prime:
        print(num, end=' ')
