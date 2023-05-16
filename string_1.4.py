# 1 4 Write a method to decide if two strings are anagrams or not  

def is_anagram(s, t):
	print(sorted(s))
	return(sorted(s)==sorted(t))

print(is_anagram("aabbd", "adbba"))