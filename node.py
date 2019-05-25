class node:
    def __init__(self,d):
        self.data=d
        self.addrs=None
class SLL:
    def __init__(self):
        self.head=None
slo=SLL()
slo.head=node("MON")
n1=node("MON")
n2=node("FRI")
n3=node("THU")
n4=node("WED")
n5=node("SAT")
n6=node("SUN")
n7=node("TUE")
slo.head.addrs=n7
n7.addrs=n4
n4.addrs=n3
n3.addrs=n2
n2.addrs=n5
n5.addrs=n6
temp=slo.head
while temp!=None:
    print(temp.data)
    temp=temp.addrs

