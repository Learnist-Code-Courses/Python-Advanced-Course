#!/usr/bin/env python3
# vim: ts=4 sw=4 noexpandtab

# The goal of this exercise is to do the Fizzbuzz! challenge
#
# The rules of the game are as follow:
#   - You have to count from 1 to 100
#   - If a number is divisible by 3, you will say Fizz instead of the number
#   - If a number is divisible by 5, you will say Buzz instead of the number
#   - If the number is disible by BOTH 3 and 5, you will say Fizzbuzz! instead
#


# Step 1: We start by counting
for num in range(1,101):
    print(num)


# Step 2: We check for divisibility
for num in range(1,101):
	if num % 15 == 0:
		print("Fizzbuzz")
	elif num % 3 == 0:
		print("Fizz")


# Step 3: We combine all the rules!
#   Notice how we use the "and" keyword to check for multiple conditions
for num in range(1,101):
	if (num % 5 == 0) and (number % 3 == 0):
		print("Fizzbuzz")
	elif num % 3 == 0:
		print("Fizz")
	elif num % 5 == 0:
		print("Buzz")
	else:
		print(num)


# Step 3: We combine all the rules!
#   Any number divisible by both 3 and 5 must also be divisible by 15. Maths!
for num in range(1,101):
	if num % 15 == 0:
		print("Fizzbuzz")
	elif num % 3 == 0:
		print("Fizz")
	elif num % 5 == 0:
		print("Buzz")
	else:
		print(num)



