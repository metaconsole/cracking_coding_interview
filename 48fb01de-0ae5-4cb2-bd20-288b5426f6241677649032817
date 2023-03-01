# Write code to remove duplicates from an unsorted linked list FOLLOW UP How would you solve this problem if a temporary buf f er is not allowed?

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

def get_linklist_data(head):
	data_found = []
	if(head.next == None):
		data_found.append(head.data)
		return(head.data) # nothing to do
	cur_nd = head
	while(True):
		data_found.append(cur_nd.data)
		cur_nd = cur_nd.next
		if(cur_nd == None):
			return(data_found)		
	
c_node = Node(66)
a_node = Node(55, c_node)
b_node = Node(66, a_node)
d_node = Node(55, b_node)
print("data of linked list")
print(get_linklist_data(d_node))
print("after duplicate removal")
print(rmv_dpl_ll(d_node))
#a = [5 , 6, 3]
#b = 0
#while(b < len(a)):
#	print(b, a[b])
#	b += 1


