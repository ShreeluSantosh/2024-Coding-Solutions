def compressTheString(head):
	unique = ""      #create empty final string
	i = 0            #create index, initially at 0
	while i != len(head):      #traverse the input string
		c = 1                  #initializing count variable
		while (i < len(head)-1) and (head[i] == head[i+1]):       #conditions
			i += 1                    #incrementing index and count
			c += 1
		if c == 1:                    #appending the letter and its count to final string
			unique += head[i]
		else:
			unique += head[i] + str(c)
		i += 1              #increment index, otherwise it will result in infinite loop
	return unique               #return compressed string