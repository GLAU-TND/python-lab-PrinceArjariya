class MyException(Exception):
    def __init__(self ,v):
        self.v=v


def xyz(a,b):
    c = a+b
    if c<150:
        raise TypeError('Custom Exception occurred')
    else:
        return c


a = int(input())
b = int(input())
print(xyz(a,b))
