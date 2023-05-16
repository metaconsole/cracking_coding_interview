# 1.3 Design an algorithm and write code to remove the duplicate characters in a string without using any additional buf f er NOTE: One or two additional variables are fi ne An extra copy of the array is not FOLLOW UP Write the test cases for this method  

def unique_string(s):
	#flag = [False for x in range(len(s))]
	flag = []
	for i in range(len(s)):
		for k in range(i+1, len(s)):
			if(s[i] == s[k]):
				flag.append(k)
	return(flag)
	
print("aaabbbdsejsbaaa")
print(unique_string("aaabbbdsejsbaaa"))