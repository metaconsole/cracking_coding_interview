# 1.1 Implement an algorithm to determine if a string has all unique characters. What if you can not use additional data structures?

for c in [3,5,6]:
	print(c)

def unique_char(s):
	for c in s:
		count = 0
		for d in s:
			if(c == d):
				count += 1
			if(count > 1):
				return(False)
	return(True)

print(unique_char('halloo'))
print(unique_char("abcdefg"))

