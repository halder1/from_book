players = ['charles', 'martina', 'michael', 'florence', 'eli']
print(f"{players}\n")
print(players[0:3])
print(players[1:4])
print(players[:4])
print(players[2:])
print(players[-2:])

print("These are the first three players on my team")
for player in players[:3]:
	print(player.title())
