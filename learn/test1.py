import sys
print(sys.platform)

import math
print(math.e)
print(math.pi)

import random
print(random.random ())#0-1之间随机浮点数
print(random.uniform(10,15))#a-b之间的随机浮点数
print(random.randint(20,25))#a-b之间的随机整数

from decimal import Decimal
from decimal import getcontext
getcontext().prec = 5
print(Decimal("1.0")/Decimal("3.0"))

name = input("请输入姓名：")
print(name)