# 1.2 Write code to reverse a C-Style String (C-String means that “abcd” is represented as five characters, including the null character )  
# In computer programming, a null-terminated string is a character string stored as an array containing the characters and terminated with a null character (a character with a value of zero, called NUL in this article). either '\0' or 0
# assumption last element index is not known at start so list[-1] does not work
# arrays are assumed to be fixed size i.e. last memory slot not necessarly last char.

def to_c_str(s):
	[*result] = s
	result.append('\0')
	return(result)

def reverse_c_str(c_str):
	len_s = 0
	char = c_str[len_s]
	while(char != '\0' and char != 0):
		len_s += 1
		char = c_str[len_s]
		
	len_half = int(len_s//2)
	for i in range(len_half):
		c_str[i], c_str[len_s - i -1] = c_str[len_s -i -1], c_str[i]
	return(c_str)
	
c_str = to_c_str("abcdef")
print(c_str)
print(reverse_c_str(c_str))