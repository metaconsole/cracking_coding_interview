# 1.5 Write a method to replace all spaces in a string with ‘%20’  

def str_replace(s, pattern, x):
	r = s
	addon = 0
	for i in range(len(s)):
		if(s[i] == pattern):
			r = r[:i + addon] + x + r[i + addon+1:]
			addon += len(x) - len(pattern)
	return(r)		
print("fr aha aj a")
print(str_replace("fr ahagggg ggg", " ", "%20"))
print(str_replace("fr aha aj a", "a", "7a20"))
print(str_replace("fr aha aj a", "", "%20"))			