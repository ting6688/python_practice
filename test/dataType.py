# 数据类型
# 数字有四种类型：整数、布尔型、浮点数、复数
# 整数： int
# bool
# float
# complex(复数): 1+2j、 1.1+2.2j
# 字符串String
# 单引号和双引号使用完全相同，使用三引号''' 或 """来指定一个多行字符串
# 输出---------
# word 字符串
# sentence 这是一个句子。
# paragraph 这是一个段落，
# 可以由多行组成
if __name__== "__main__":
  word = '字符串'
  sentence="这是一个句子。"
  paragraph= """这是一个段落，
  可以由多行组成"""
  print("word",word)
  print("sentence",sentence)
  print("paragraph",paragraph)



# 标准数据类型
"""
Number(数字):有符号整型 长整型 浮点数 复数
String(字符串)
List(列表)
Tuple(元组)
Dictionary(字典)
"""


# 创建Number对象
var1=1
var2=10
# print("var1",var1)
# print("var2",var2)
# 删除对象的引用
# del var1
# del var1,var2
# print("var1",var1)
# print("var2",var2)


# 字符串的顺序 从左到右的索引默认从0开始，从右到左的索引默认从-1开始的

# 字符串截取[头下标：尾下标]
s="abcdef"
# abcdef 下标为空表示取到头或尾，我理解是获取全部
print(s[:])
# bcde 前包含，后不包含
print(s[1:5])
# cd -4-3
print(s[-4:-2])
# cdef 从第3个字符开始到结束
print(s[2:])
# 输出第一个字符 a
print(s[0])
# 字符串连接 abcdef:test
print(s+":test")
# 输出字符串两次 abcdefabcdef
print(s * 2)

# 输出字符串两次 aa
print(s[0] * 2)


# python的列表截取接收三个参数 开始位置索引，结束位置索引，步长
letters = ['a','b','c','d','e','f','h','i']
# ['b', 'd']
print(letters[1:4:2])


# 列表 python中使用最频繁的数据类型，最通用的复合数据类型，它支持字符，数字，字符串，也可以包含列表
# 列表用[]标识
list = ['big','big',789,2.23,'John',1+2j,[1,'test',5.32]]
tinylist = [222,"tracy"]


# ['big', 'big', 789, 2.23, 'John', (1+2j), [1, 'test', 5.32]]
# [222, 'tracy']
# big
# ['big', 789]
# [789, 2.23, 'John', (1+2j), [1, 'test', 5.32]]
# [222, 'tracy', 222, 'tracy', 222, 'tracy']
# ['big', 'big', 789, 2.23, 'John', (1+2j), [1, 'test', 5.32], 222, 'tracy']
# 输出完整列表
print(list)
# 输出完整列表
print(tinylist)
# 输出列表的第一个元素
print(list[0])
# 输出列表的第二个到第三个元素
print(list[1:3])
# 输出列表从第三个开始到末尾的元素
print(list[2:])
# 输出列表三次
print(tinylist*3)
# 列表连接
print(list + tinylist)
# 输出列表倒数第二个元素 (1+2j)
print(list[5])
# 输出列表最后一个元素 [1, 'test', 5.32]
print(list[6])


# python元组 类似于List(列表)
# 元组用()标识，内部元素用逗号隔开，但是元组不能二次赋值，相当于只读列表
tuple = ('my','little','Dog',2,'岁')
tinyTuple = (123,'john')


'''
('my', 'little', 'Dog', 2, '岁')
my
('little', 'Dog')
('Dog', 2, '岁')
(123, 'john', 123, 'john')
('my', 'little', 'Dog', 2, '岁', 123, 'john')
'''
#输出一个完整元组
print(tuple)
#输出元组的第一个元素
print(tuple[0])
#输出第二个到第四个(不包含)的元素
print(tuple[1:3])
#输出从第三个开始到末尾的所有元素
print(tuple[2:])
#输出元组两次
print(tinyTuple*2)
#输出拼接后的元组
print((tuple+tinyTuple))
# 元组中元素赋值非法，因为元组不可变，不允许更新，会报错
# tuple[2]=1
# 在输出更新后的元组时会提示错误
# print(tuple)


# Python字典
'''
字典是除列表以外python之中最灵活的内置数据结构类型，列表是有序的对象集合，字典是无序的对象集合。
两者的区别在于：字典当中的元素是通过键来存取的，而不是通过偏移存取
字典用"{}"标识，字典由key和它对应的value组成。
'''



'''
{'one': 'This is one', 2: 'this is two'}
this is two
{'name': 'tracy', 'code': 200, 'age': 18}
dict_keys(['name', 'code', 'age'])
dict_values(['tracy', 200, 18])
this is two
'''
dict = {}
dict['one'] = "This is one"
dict[2] = "this is two"
tinydict={'name':'tracy','code':200,'age':18}

print(dict)
print(dict[2])
print(tinydict)
print(tinydict.keys())
print(tinydict.values())
print(dict[2])



# 数据类型转换：将数据类型作为函数名即可
print(int(18.8)) # 18
print(float(19)) # 19.0
'''
23
<class 'str'>
'''
print(str(23))
print(type(str(23)))
# error!!! TypeError: 'tuple' object is not callable
# print(tuple([1231,111]))
# print(type(tuple(1)))
# 元组类型转换遇到问题 TODO
new_tuple = tuple([1231,111])

print(new_tuple)


#-------python3的数据类型---------
'''
 数字类型（Number）: 整数、布尔型、浮点数和复数
 字符串 （String）:python中单引号和双引号使用完全相同
'''