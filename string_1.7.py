# 1.8 Assume you have a method isSubstring which checks if one word is a substring of another Given two strings, s1 and s2, write code to check if s2 is a rotation of s1 using only one call to isSubstring (i e , “waterbottle” is a rotation of “erbottlewat”) 

s1 = "waterbottle"
s2 = "erbottlewat"

def isSubstring(s1, s2):
	pass

def isRotation(s1, s2):
	if length(s1) != length(s2):
		return(False)
	s1s1 = s1 + s1
	return(isSubstring(s2, s1s1))