class node:
    def __init__(self,data):
        self.data=data
        self.nextt=None
class SLL:
    def __init__(self):
        self.head=None
    def insertatbeg(self,data):
        temp=node(data)
        temp.nextt=self.head
        self.head=temp
    def delatbeg(self):
        temp=self.head
        if temp!=None:
            self.head=self.head.nextt
            temp.nextt=None
        else:
            print("error")
    def printlist(self):
        temp=self.head
        while temp!=None:
            print(temp.data,"  ",end='')
            temp=temp.nextt
    pri nt("None")
obj=SLL()
ch=0
while ch!=4:
    print("linked list implementation\n","1.insertion at beginning 2.deletion at beginning 3. print list 4.exit ")
    ch=int(input())
    if ch==1:
        print("enter value of the node")
        data=input()
        obj.insertatbeg(data)
        obj.printlist()
    elif ch==2:
        obj.delatbeg()
        obj.printlist()
    elif ch==3:
        obj.printlist()
        
