# This is a python program calculating digits of the fibonacci sequence.
# Users can input an index and find the fibonacci's number attached to it.
from time import sleep

user_input = int(input('what\'s the index of the number in the fibonacci sequence you want to calculate?\n\n'))
index = [i for i in range(1, user_input+1)]
old_number = 1
new_number = 1
numfibo = int()
fibonacci = {}

for i in index:
    numfibo = old_number + new_number
    fibonacci.update({i: numfibo})
    old_number = new_number
    new_number = numfibo

fibolist = []
for value in fibonacci.values():
    fibolist.append(value)

# [-3] because it doesn't actually start at 2, 
# it starts at 1, 1, 2, 3 etc. so not [-1] but [-3]
print(fibolist[-3])