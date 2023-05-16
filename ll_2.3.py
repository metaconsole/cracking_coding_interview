# Implement an algorithm to delete a node in the middle of a single linked list, given only access to that node 
# EXAMPLE Input: the node ‘c’ from the linked list a->b->c->d->e Result: nothing is returned, but the new linked list looks like a->b->d->e
# NOTE! head is first element, tail is last element pointing to none.

class Node:
	def __init__(self, d, node = None):
		self.data = d
		self.next = None
		if(node != None):
			self.next = node
	def __str__(self):
		return(f"{self.data} ->  {self.next}")

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

def get_k_element(head, k):
	n = 0
	while(n < k):
		head = head.next
		n += 1
	return(head)

def get_k_element_back(head, k):
	return(get_k_element(head, length_linkedlist(head) - k))	

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
print("linked list")
print(d_node)
del_node(a_node)
print(d_node)
print(a_node)
del(c_node)
print(d_node)
#print(c_node)
#a = [5 , 6, 3]
#b = 0
#while(b < len(a)):
#	print(b, a[b])
#	b += 1


