def foo():
    str="function"
    print(str);


def foo1(num):
    print('num',num);

def foo2(name,age):
    print('name',name);
    print('age',age);

if __name__== "__main__":
    print("main")
    foo2('zhangting',25)
    foo1(6)
    foo()