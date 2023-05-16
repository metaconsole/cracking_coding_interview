class Node:
	def __init__(self, d, node = None):
		self.data = d
		self.next = None
		if(node != None):
			self.next = node
			
head_node = Node(787)
a_node = Node(55, head_node)
print(head_node.next)
print(a_node.next)
print(a_node.data)