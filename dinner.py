guests = ['mike hunt', 'jack hoff', 'vlanman']
guest1 = guests.pop(0)
guest2 = guests.pop(0)
guest3 = guests.pop(0)
#Because the pop() method *removes* the first item in the list, the item 
#next to it will become the first, and therefore you do not need to 
#actually count the positions in the list should you just want to pop
#it in the order in which it was written. This is reflected in the fact
#that the message printed below will be in order, despite all the pop
#methods popping from the same position

message = f"I hereby invite {guest1.title()}, {guest2.title()}, and {guest3.title()} to my dinner party."

print(message)

guests = ['mike hunt', 'jack hoff', 'vlanman']
#I don't know how else I could have gone about doing this. I didn't want to 
#change the message every time I had different guests (like I even used this
#program more than once) and wanted to actually use the list function.

absent_guest = guests[-1]
print(f'Unfortunately, our guest {absent_guest.title()} cannot make it.')
guests.remove('vlanman')
guests.append('captain traceroute')
new_guest = guests[-1]
print(f"Therefore, we will instead have {new_guest.title()}!")

#First program here that I feel is greatly inefficient.