cubes = [cubed**3 for cubed in range(1, 100)]
print(cubes)

#So as far as I can tell, this creates a list "cubes", then defines it by 
#assigning a variable "cubed" to every number from 1 to 100. The for loop here
#then somehow knows how to use the cubed**3 (such to say, that, it will cube
#every number from 1-100). This is as opposed to writing the following code,
#which will take up more lines

	#cubes = []
	#for cubed in range(1,100):
		#cubed = cubed**3
		#cubes.append(cubed)
	#print(cubes)

#This is five lines of code as opposed to two, which isn't favorable. Although 
#they produce the same result, the first option is smaller and therefore more
#efficient. The top is known as a list comprehension

