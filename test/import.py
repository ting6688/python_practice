# 导入相应的模块或函数
'''
# 导入整个模块
import somemodule
# 从某个模块中导入某些函数
from somemodule  import somefunction
# 从某个模块中导入多个函数
from somemodule import firstfunc,secondfunc
# 将某个模块中的全部函数导入
from somemodule import *
'''

# 导入sys模块
import sys
print('==============Python import mode===========')
print('命令行参数为：')
for i in sys.argv:
    print(i)
print('\n python 路径为',sys.path)

# 导入sys模块的argv,path成员
from sys import argv,path

print('==================python from import================')
# 因为已经导入path成员，所以此处引用时不需要加sys.path
print('path:',path)