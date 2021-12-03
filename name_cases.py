famous_person = " albert einstein "
quote = " A person who never made a mistake never tried anything new "
message = f"{famous_person.strip().title()} once said,\t\n{quote.strip()}"
print(message)

#Both the famous_person and quote variables are surrounded by whitespace. The
#message variable formats both strings with f, and uses the .strip() 
#method to remove the whitespace. The famous_person variable becomes
#capitalized like an actual name would, by the use of the .title() method.

#Then, it prints the message variable. When you're inserting variables into
#a string (such as a formatted one in the message variable), you encase them
#with {}. At least, you would with strings.