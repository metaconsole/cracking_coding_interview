# -*- coding: utf-8 -*-
"""
Created on Sun Jan  8 23:07:45 2023

@author: Nero

3 3 Imagine a (literal) stack of plates If the stack gets too high, it might 
topple There-fore, in real life, we would likely start a new stack when the 
previous stack exceeds some threshold Implement a data structure SetOfStacks 
that mimics this SetOf-Stacks should be composed of several stacks, and should 
create a new stack once the previous one exceeds capacity SetOfStacks push() 
and SetOfStacks pop() should behave identically to a single stack (that is, 
pop() should return the same values as it would if there were just a single 
stack) 
FOLLOW UP Implement a function popAt(int index) which performs a pop 
operation on a specif i c sub-stack  
"""

# Node is essentially a linked list implementation
class Node:
	def __init__(self, d, node = None):
		self.data = d
		self.next = None
		if node != None :
			self.next = node
	def __str__(self):
		return f"{self.data} ->  {self.next}"

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
		data = self.top.data
		self.top = self.top.next
		return data
	
	def __str__(self):
		return f"top of stack {self.top.data} \nlinked list below top\n{self.top.next}"

class SetOfStacks:
	def __init__(self, max_height):
		# using a list to store stacks might be cheating, since pop and append
		# are already implemented, should probably also be a stack
		self._stack_list = [Stack()]
		self._max_height = max_height
		self._height = 0
	
	def push(self, data):
		if self._height < self._max_height:
			self._stack_list[-1].push(data)
			self._height += 1
		else:
			self._stack_list.append(Stack())
			self._stack_list[-1].push(data)
			self._height = 1
		return None
	
	def pop(self):
		self._stack_list[-1].pop()
		self._height -= 1
		if len(self._stack_list) > 1 and self._height == 0:
			self._stack_list.pop()
			self._height = self._max_height
		return None
	
	def __str__(self):
		return f"list of stacks\n{[print(i) for i in self._stack_list]}"
		

if __name__ == "__main__":	
	s = SetOfStacks(3)
	[s.push(i) for i in range(10)]
	print(s)
	print("##################")
	[s.pop() for i in range(8)]
	print(s)
	print("##################")
	[s.push(i) for i in range(44, 48)]
	print(s)
	
	