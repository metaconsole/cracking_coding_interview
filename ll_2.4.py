# 2.4 You have two numbers represented by a linked list, where each node contains a sin-gle digit.
# The digits are stored in reverse order, such that the 1’s digit is at the head of the list 
# Write a function that adds the two numbers and returns the sum as a linked list 
# EXAMPLE Input: (3 -> 1 -> 5) + (5 -> 9 -> 2) Output: 8 -> 0 -> 8
# 513 + 295 = 808
# NOTE! head is first element, tail is last element pointing to none.
# head is "einser stelle"

class Node:
	def __init__(self, d, node = None):
		self.data = d
		self.next = None
		if(node != None):
			self.next = node
	def __str__(self):
		return(f"{self.data} ->  {self.next}")

def add_linked_int(a, b):
	if(length_linkedlist(a)>= length_linkedlist(b)):
		result = a
	else:
		result = b
	head = result
	carry = 0
	while(result != None):
		if(a == None):
			a_digit = 0
		else:
			a_digit = a.data
		if(b == None):
			b_digit = 0
		else:
			b_digit = b.data
		c = a_digit + b_digit + carry
		carry = 0
		if(c < 10):
			result.data = c
		elif(result.next == None):
			result.next = Node(99)
			result.data = c - 10
			carry = 1
		else:
			result.data = c - 10
			carry = 1
		if(a != None):
			a = a.next
		if(b != None):
			b= b.next
		result = result.next
	return(head)

def rmv_dpl_ll(head):
	data_found = []
	if(head.next == None):
		data_found.append(head.data)
		return(head) # nothing to do
	cur_nd = head
	last_nd = None
	while(True):
		if(cur_nd.next == None):
			if(cur_nd.data in data_found):
				last_nd.next = None
			else:
				data_found.append(cur_nd.data)	
		elif(cur_nd.next.data in data_found):
			cur_nd.next = cur_nd.next.next
		else:
			data_found.append(cur_nd.data)
		last_nd = cur_nd
		cur_nd = cur_nd.next
		if(cur_nd == None):
			return(data_found)

def length_linkedlist(head):
	n = 0
	while(True):
		head = head.next
		n += 1
		if(head == None):
			return(n)

def del_node(node):
	if(node.next == None):
		return('error node not in middle')
	elif(node.next.next == None):
		node.data = node.next.data
		node.next = None
	else:
		node.data = node.next.data
		node.next = node.next.next
	# print(node.next)
	# del node.next
	return(None)

e_node = Node(777)
c_node = Node(66, e_node)
a_node = Node(55, c_node)
b_node = Node(6336, a_node)
d_node = Node(577, b_node)

a = Node(2)
b = Node(4, a)
c = Node(1, b)

aa = Node(3)
bb = Node(5, aa)
cc = Node (9, bb)
print(c)
print(cc)
print(add_linked_int(a, cc))

#print("linked list")
#print(d_node)
#del_node(a_node)
#print(d_node)
#print(a_node)
#del(c_node)
#print(d_node)
#print(c_node)
#a = [5 , 6, 3]
#b = 0
#while(b < len(a)):
#	print(b, a[b])
#	b += 1


