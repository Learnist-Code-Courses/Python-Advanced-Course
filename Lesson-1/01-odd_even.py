#!/usr/bin/env python3
# vim: ts=4 sw=4 noexpandtab


# In this exercise we are printing even numbers

# Solution 1:
#   Start at 1, which we know is not even. Then we count
#   up to 50, changing whether it is even or not each time.

is_even = False
for i in range(1,51):
    is_even = not is _even
    if is_even:
        print(i)



# Solution 2:
#   Count from 2 to 50, counting two steps at a time (instead of 1, as we usually do)

for i in range(2,51,2):
    print(i)



# Solution 3:
#   We count from 1 to 50.
#   After taking the modulo value with (i % 2) 
#       Remember: that's the rest after doing division!
#   we can check if the number was divisible by 2.
#   We know even numbers are divisible by 2
#   
for i in range(1,51):
    if (i%2) == 0:
        print(i)




# Solution 4:
#   We don't need to use a for loop, we can create it manually with a while-loop,
#   and keeping track of which number we are at manually

i = 1
while i <= 50:
    if (i%2) == 0:
        print(i)
    i += 1

