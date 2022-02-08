number1 = '127' #Weird, looks like strings can still function like numbers. Also, I have no idea what the fuck I just did to make this type twice.
number2 = '3389' #Weird, looks like strings can still function like numbers. Also, I have no idea what the fuck I just did to make this type twice.

print(f"Is {number1} greater than {number2}? I predict false")
print(number1 > number2) #It will print the result of this statement, which is false. 

word = 'shrew'
print(f"Is the word '{word}' capitalized? I predict false")
print(word == word.upper()) #Compares "shrew" contained in 'word' to "Shrew", Outputting the result (false)