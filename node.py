class Node:
    def __init__(self , value = None):
        self.value  = value
        self.next = None

    def isempty(self):
        if self.value == None:
            return True
        else:
            return False

    def append(self, v):
        if self.isempty():
            self.value = v
        elif self.next == None:
            self.next = Node(v)

        else:
            self.next.append(v)
            return

    def insert(self , v):
        if self.isempty():
            self.value = v
        else:
            newnode = Node(v)
            self.value , newnode.value = newnode.value , self.value
            self.next , newnode.next = newnode.next , self.next
            return

    def delete(self , v):
        if self.isempty():
            return

        if self.value == v:
            self.value = None
            if self.next != None:
                self.value = self.next.value
                self.next = self.next.next
                return

        else:
            if self.next != None:
                self.next.delete(v)
                if self.next.value == None:
                    self.next = None
                return

node = Node()
node.append(4)
node.append(6)
node.append(9)
node.insert(3)
node.delete(6)
node.append(2)
print(node.value)




        
