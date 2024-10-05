# a set 
s = set()

# adding somethin
s.add(1)
s.add(2)
s.add(3)
s.add(4)
s.add(3) # i add 3 again

print(s)

s.remove(2)
print(s)

print(f'the set  has {len(s)} numbers of elements')