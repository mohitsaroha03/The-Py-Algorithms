# isGFG: , Link: 
# IsDone: 0
import math
class Stack(object):
	def __init__(self, limit=10):
		self.stk = []
		self.limit = limit	
	def isEmpty(self):
		return len(self.stk) <= 0

	def push(self, item):
		if len(self.stk) >= self.limit:
			print 'Stack Overflow!'
		else:
			self.stk.append(item)
		print 'Stack after Push', self.stk

	def pop(self):
		if len(self.stk) <= 0:
			print 'Stack Underflow!'
			return 0
		else:
			return self.stk.pop()
			
	def peek(self):
		if len(self.stk) <= 0:
			print 'Stack Underflow!'
			return 0
		else:
			return self.stk[-1]
			
	def size(self):
		return len(self.stk)

# Node of a Singly Linked List
class Node:
	# constructor
	def __init__(self, data=None, next=None):
		self.data = data
		self.last = None
		self.next = next
	# method for setting the data field of the node    
	def set_data(self, data):
		self.data = data
	# method for getting the data field of the node   
	def get_data(self):
		return self.data
	# method for setting the next field of the node
	def set_next(self, next):
		self.next = next
	# method for getting the next field of the node    
	def get_next(self):
		return self.next
	# method for setting the last field of the node
	def setLast(self, last):
		self.last = last
	# method for getting the last field of the node    
	def getLast(self):
		return self.last	
	# returns true if the node points to another node
	def has_next(self):
		return self.next != None


class Queue(object):
	def __init__(self, data=None):
		self.front = None
		self.rear = None
		self.size = 0

	def enQueue(self, data):
		self.lastNode = self.front
		self.front = Node(data, self.front)
		if self.lastNode:
			self.lastNode.setLast(self.front)
		if self.rear is None:
			self.rear = self.front
		self.size += 1

	def queueRear(self):
		if self.rear is None:
			print "Sorry, the queue is empty!"
			raise IndexError
		return self.rear.get_data()

	def queueFront(self):
		if self.front is None:
			print "Sorry, the queue is empty!"
			raise IndexError
		return self.front.get_data()

	def deQueue(self):
		if self.rear is None:
			print "Sorry, the queue is empty!"
			raise IndexError
		result = self.rear.get_data()
		self.rear = self.rear.last
		self.size -= 1
		return result

	def size(self):
		return self.size
		
	def isEmpty(self):
		return self.size == 0	
		
def checkStackPairwiseOrder(stk):
	que = Queue()
	pairwiseOrdered = 1
	# Reverse Stack elements
	while not stk.isEmpty():
		que.enQueue(stk.pop())
	while not que.isEmpty():
		stk.push(que.deQueue())

	while not stk.isEmpty():
		n = stk.pop()
		que.enQueue(n)
		if not stk.isEmpty():
			m = stk.pop()
			que.enQueue(m)
			if (abs(n - m) != 1):
				pairwiseOrdered = 0
				break
	while not que.isEmpty():
		stk.push(que.deQueue())
	return pairwiseOrdered

stk = Stack()
stk.push(-2)
stk.push(-3)
stk.push(11)
stk.push(10)
stk.push(5)
stk.push(6)
stk.push(20)
stk.push(21)
print checkStackPairwiseOrder(stk)
