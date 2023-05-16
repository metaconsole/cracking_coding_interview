# 2.5 Given a circular linked list, implement an algorithm which returns node at the begin-ning of the loop 
# DEFINITION Circular linked list: A (corrupt) linked list in which a node’s next pointer points to an earlier node, so as to make a loop in the linked list 
# EXAMPLE input: A -> B -> C -> D -> E -> C [the same C as earlier] 
# output: C
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

def make_cycle(head, node):
	while(head.next != None):
		head = head.next
	head.next = node
	return(None)

def get_cycle(head):
	i = 0
	id_node = []
	while(i < 20):
		i += 1
		print(id(head))
		if(id(head) in id_node):
			return(head)
		id_node.append(id(head))
		head = head.next
		if(head == None):
			return("no cycle found")
	return("end")

e_node = Node(777)
c_node = Node(66, e_node)
a_node = Node(55, c_node)
b_node = Node(6336, a_node)
d_node = Node(577, b_node)
print(d_node)
make_cycle(d_node, a_node)
c = get_cycle(d_node)
print(id(c))
print(id(a_node))