message = 'One of Python's strengths is its diverse community.'
print(message)
#This doesn't work because the message variable is assigned with single
#quotes, which re-appear within the data. The interpreter reads this and
#thinks the data ends there, and then tries to process the rest of it as
#code, even though it's not code at all. It might as well be, to the 
#interpreter's eyes, nonsense. To fix this, you would need to, at the 
#most basic level, change the outer quotes to double ones. 