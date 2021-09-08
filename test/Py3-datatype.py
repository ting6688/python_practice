#-------python3的数据类型---------
'''
 数字类型（Number）: 整数、布尔型、浮点数和复数
 字符串 （String）:python中单引号和双引号使用完全相同
'''

# a,b,c,d = 20,5.5,True,4+3j
# # <class 'int'>
# # <class 'float'>
# # <class 'bool'>
# # <class 'complex'>
# print(type(a))
# print(type(b))
# print(type(c))
# print(type(d))
#
# a = 111
# flag = isinstance(a,int)
# # True
# print(flag)
#
#
#
# # isinstance 和 type的区别
# '''
# type()不会认为子类是一种父类类型
# isinstance()会认为子类是一种父类类型
# '''
#
# class A:
#     pass
#
# class B(A):
#     pass
#
#
# '''
# True
# True
# True
# True
# False
# '''
# print(isinstance(A(),A))
#
# print(type(A()) == A)
#
# # True isinstance认为子类是一种父类类型
# print(isinstance(B(),A))
#
# print(type(B()) == A)



# python3中 bool是int的子类，true和false可以和数字相加
print(issubclass(bool,int)) # True

print(True==1) # True


print(False==0) # True


print(True+1) # 2


print(False-1) # -1


print(1 is True) # False


print(0 is False) # False


print(False is False) # True

# todo is 的作用？
print(False is 0) # False








