class number:
    def __init__ (self,n):
        self.num=n
        self.abc=None
class slist:
    def __init__(self):
        self.head=None
obj=slist()
obj.head=number("1")
a7=number("5")
a2=number("3")
a3=number("4")
a4=number("2")
a5=number("7")
a6=number("6")
obj.head.abc=a4
a4.abc=a2
a2.abc=a3
a3.abc=a7
a7.abc=a6
a6.abc=a5
temp=obj.head
while temp!=None:
    print(temp.num)
    temp=temp.abc
        
        
