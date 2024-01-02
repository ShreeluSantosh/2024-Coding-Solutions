def compressTheString(head):
	unique = ""   #create final string
	i = 0         #create initial index at 0
	while i != len(head):      #traverse the input string
		c = 1                    #count variable for each substring
		while (i < len(head)-1) and (head[i] == head[i+1]):  #checking condition
			i += 1
			c += 1
		if c == 1:       #if the substring is a single character
			unique += head[i]
		else:
			unique += head[i] + str(c)
		i += 1
	return unique     #returns the compressed string
