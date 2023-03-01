# 3.6 Write a program to sort a stack in ascending order You should not make any assump-tions about how the stack is implemented The following are the only functions that should be used to write this program: push | pop | peek | isEmpty

class Node:
	def __init__(self, d, node = None):
		self.data = d
		self.next = None
		if(node != None):
			self.next = node
	def __str__(self):
		return(f"{self.data} ->  {self.next}")

class Stack:
	def __init__(self):
		self.top = None
	
	def push(self, d):
		new_top = Node(d, self.top)
		self.top = new_top
		return None
	
	def pop(self):
		if self.top == None:
			return None
		d = self.top.data
		self.top = self.top.next
		return d
	
	def __str__(self):
		return f"{self.top}"
	
	def peek(self):
		if self.top == None:
			return None
		return self.top.data
	
	def isEmpty(self):
		if self.top == None:
			return True
		else:
			return False

def sortStack(stack, asc = True):
	buffer = []
	while not stack.isEmpty():
		buffer.append(stack.pop())
	
	for k in range(len(buffer)):
		max_buff = max(buffer)
		stack.push(max_buff)
		# maybe illegal pop and index
		buffer.pop(buffer.index(max_buff)) 
	
	return stack
	
st = Stack()
st.push(3)
st.push(8)
st.push(2)
st.push(999)
print(st)
st = sortStack(st)
print(st)