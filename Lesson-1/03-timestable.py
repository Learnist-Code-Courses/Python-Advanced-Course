#!/usr/bin/env python3
# vim: ts=4 sw=4 noexpandtab

# The goal of this exercise is to print the times table


# We start showing up the times table for the number 7

for i in range(11):  # the numbers 0 to 10, inclusive
    product = 7 * i
    print(7, "times", i, "=", product)




# Then we can do it for all the tables
for a in range(1,11):
	for b in range(11):  # the numbers 0 to 10, inclusive
		product = a * b
		print(a, "times", b, "=", product)
		



# Here's a fancy way of formatting the output
#	It is difficult, so don't expect to understand everything here
for a in range(1,11):
	for b in range(11):  # the numbers 0 to 10, inclusive
		output = f"{a}×{b}={a*b}"
		print(f"{output:10}", end="")
	print()


