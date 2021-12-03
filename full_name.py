first_name = " ada"
last_name = "lovelace "
full_name = f"{first_name} {last_name}"
message = f"\tHello, {full_name.strip().title()}!"
print(message)

#You assign the values of the first_name and last_name variables to full_name
#by formatting it as a string with f"{first_name} {last_name}". Then, you 
#assign the full_name variable to message, but you format it as a string
#with f again, and also add in a \t for good measure. You also use the 
#.strip().title() methods in {full_name} because they're stored as 
#lowercase words with whitespaces, but you want them to have proper spacing
#and capitalization, which .strip() and .title() do respectively.

#The \t makes it indent like a tab. Also, this whole curly braces thing will
#be how variables are inserted into strings like this from here on.