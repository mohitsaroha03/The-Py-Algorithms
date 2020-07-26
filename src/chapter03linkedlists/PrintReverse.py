#

class ListNode:
    def __init__(self, value):
        self.data = value
        self.next = None

    def get_data(self):
        return self.data

    def get_next(self):
        return self.next

    def set_data(self, value):
        self.data = value

    def set_next(self, newnext):
        self.next = newnext
	
def ListLength(self):
    current = self.head
    count = 0
    while current != None:
        count = count + 1
        current = current.get_next()

    return count	
    
    def insert(self, position, value):
        sentinel = self.sentinel
        newNode = ListNode(value)
        size = len(self)
        if size == 0:
            self.insert_between(newNode, sentinel, sentinel)
        elif position >= 0 and position < size:
            node = self.get_node(position)   
            self.insert_between(newNode, node.prev, node)
        elif position == size:
            self.insert_between(newNode, sentinel.prev, sentinel)
        else:
            raise positionError
        self.size += 1
                
    def insert_between(self, node, leftNode, rightNode):
        if node and leftNode and rightNode:
            node.prev = leftNode
            node.next = rightNode
            leftNode.next = node
            rightNode.prev = node
        else:
            raise positionError
