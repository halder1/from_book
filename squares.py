squares = [] #creating an empty list
for value in range(1, 11): #creates a for loop given every value in the range defined
	squares.append(value ** 2) #puts the value to the power of 2 and appends it
print(squares)#results
print(min(squares))
print(max(squares))
print(sum(squares))