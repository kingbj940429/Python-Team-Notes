from collections import Counter

counter = Counter(['red', 'blue', 'red', 'blue', 'green', 'red'])

print(counter['blue'])
print(counter['red'])
print(dict(counter))
