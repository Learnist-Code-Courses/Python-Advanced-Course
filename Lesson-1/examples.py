
# === EXERCISE 2 ===

# toggling back and forth
is_even = False
for i in range(1,51):
    is_even = not is _even
    if is_even:
        print(i)

# using the optional step argument
for i in range(1,51,2):
    print(i)

# using modulo and a while loop
i = 1
while i <= 50:
    if (i%2) == 0:
        print(i)
    i += 1

# === EXERCISE 3 ===

# generating a list of numbers 1..N
# until the total sum is 50

some_numbers = list()
i = 0
while sum(some_numbers) < 50:
    some_numbers.append(i)
    i += 1
print(some_numbers)


# printing 10 fibonaci numbers

fibonacci = [0,1]
while len(some_numbers) < 10:
    next_number = fibonacci[-1] + fibonacci[-2]
    some_numbers.append(next_number)

print(fibonacci)
print(fibonacci[9]) # 10th fib number
print(fibonacci[-1]) # the last fib number we have


# === EXERCISE 4 === 

for num in range(1,101):
    if num % 15 == 0:
        print("Fizzbuzz")
    elif num % 3 == 0:
        print("Fizz")
    elif num % 5 == 0:
        print("Buzz")
    else:
        print(num)


for num in range(1,101):
    if (num % 5 == 0) and (number % 3 == 0):
        print("Fizzbuzz")
    elif num % 3 == 0:
        print("Fizz")
    elif num % 5 == 0:
        print("Buzz")
    else:
        print(num)
