motorcycles = ['honda', 'yamaha', 'suzuki']
print(motorcycles)

motorcycles[0] = 'ducati'
print(motorcycles)

motorcycles.insert(0, 'harley davidson')
print(motorcycles)

motorcycles.append('ford')
print(motorcycles)

del motorcycles[0]
print(motorcycles)

popped_motorcycles = motorcycles.pop()
print(popped_motorcycles)

last_owned = motorcycles.pop(1)
message = f"The last motorcycle that I owned was a {last_owned.title()}"
print(message)

motorcycles.remove('ducati')
print(motorcycles)
too_expensive = 'ducati'
message = f"\nA {too_expensive.title()} is too expensive for me."
print(message)