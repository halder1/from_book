magicians = ['alice', 'david', 'carolina']
for magician in magicians:
	print(f"{magician.title()}, that was a great trick!")
	print(f"I can't wait to see the next trick, {magician.title()}. \n")
	#Python assigns a variable "magician" for each value in the list "magicians"
	#Then, it executes the code stored within the loop for every value that it 
	#just assigned, repeating and therefore switching values when the code is
	#done. That's why this program in particular will repeat the below output
	#three times, because there are three magicians in the list created at
	#the beginning of the program. 

	#This is the basic functioning of a for loop.
print("Thank you everyone, that was a great magic show!  ")