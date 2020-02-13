class Node:
    def __init__(self,data):
        self.value=data
        self.l=None
        self.r=None
class btree:
    def __init__(self,data=None):
        self.root=Node(data)
        self.s=[]
    def preoder(self):
        self.s1=[]
        if self.root is None:
            return "Empty"
        self.s.append(self.root)
        while self.s:
            self.head=self.s.pop()
            self.s1.append(self.head.value)
            if self.head.r is not None:
                 self.s.append(self.head.r)
            if self.head.l is not None:
                self.s.append(self.head.l)
        print(self.s1)
    def postorder(self):
        self.s1=[]
        if self.root is None:
            return "Empty"
        self.s1.append(self.root)
        while self.s1:
            self.head=self.s1.pop()
            self.s.append(self.head.value)
            if self.head.l:
                self.s1.append(self.head.l)
            if self.head.r:
                self.s1.append(self.head.r)
        print(self.s)

    def inorder(self):
        self.s=[]
        self.s1=[]
        if self.root is None:
            return
        while(True):
            if self.root is not None:
                self.s.append(self.root)
                self.root=self.root.l
            else:
                if self.s:
                    self.root=self.s.pop()
                    self.s1.append(self.root.value)
                    self.root=self.root.r
                else:
                    break
        print(self.s1)




a = btree(10)
a.root.l=Node(0)
a.root.r=Node(-10)
a.root.r.r=Node(11)
a.root.l.l= Node(5)
a.root.l.r = Node(6)
a.inorder()
