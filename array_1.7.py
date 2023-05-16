# 1.7 Write an algorithm such that if an element in an MxN matrix is 0, its entire row and column is set to 0

class Matrix:
	def __init__(self, matrix):
		self.data = matrix
	
	def __str__(self):
		# ugly solution, should create str
		for row in self.data:
			print(row)
		return("")

class Node:
	def __init__(self, d, node = None):
		self.data = d
		self.next = None
		if(node != None):
			self.next = node
	def __str__(self):
		return(f"{self.data} ->  {self.next}")

def linked_index(start, end):
	i = start
	node = Node(i)
	while(i < end -1):
		if( i == 0):
			head = node
		next = Node(i + 1)
		node.next = next
		node = next
		i += 1
	return(head)

def set_col_row(matrix, value):
	row_n = len(matrix)
	col_n = len(matrix[0])
	row_link = linked_index(0, row_n)
	col_link = linked_index(0, col_n)
	while(row_link is not None):
		while(col_link is not None):
			if(matrix[row_link.data][col_link.data] == value):
				print("col row set to ", value)
				if(row_link.next is None):
					
				row_link.data = row_link.next.data
				row_link.next = row_link.next.next
				col_link.data = col_link.next.data
				col_link.next = col_link.next.next
			col_link = col_link.next
			row_link = row_link.next
	print(row_link, col_link)
	pass
	
matrix = [[i + k for i in range(0, 4)] for k in (2, 0, 1)]

for row in Matrix(matrix).data:
	print(row)
print(Matrix(matrix))

set_col_row(matrix, 0)
