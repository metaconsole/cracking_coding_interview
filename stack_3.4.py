# -*- coding: utf-8 -*-
"""
Created on Mon Jan  9 22:04:28 2023

@author: Nero

3 4 In the classic problem of the Towers of Hanoi, you have 3 rods and N disks 
of dif f erent sizes which can slide onto any tower The puzzle starts with 
disks sorted in ascending order of size from top to bottom (e g , each disk 
sits on top of an even larger one) You have the following constraints: 
(A) Only one disk can be moved at a time 
(B) A disk is slid of f the top of one rod onto the next rod 
(C) A disk can only be placed on top of a larger disk 

Write a program to move the disks from the first rod to the last using Stacks
"""

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
		if self.top.data > d:
			raise Exception("In Hanoi larger disk can only be at bottom.")
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
		if self.top == None:
			return "None"
		return f"top of stack {self.top.data} \nlinked list below top\n{self.top.next}"
	
if __name__ == "__main__":
	# game setup
	tower_1 = Stack()
	tower_2 = Stack()
	tower_3 = Stack()
	tower_3.push(3)
	tower_3.push(2)
	tower_3.push(1)
	print(tower_1, tower_2, tower_3)
	
	# game moves
	tower_2.push(tower_3.pop())
	tower_1.push(tower_2.pop())
	tower_2.push(tower_3.pop())
	tower_2.push(tower_1.pop())
	
	print(tower_1, tower_2, tower_3)
	

