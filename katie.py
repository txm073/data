"""
#INPUT/OUTPUT
x = int(input("enter a number "))
attempts = 1
while x < 100:
    x = int(input("try again (>=100) "))
    attempts = attempts + 1
print("Thanks")
print("took", attempts, "attempts to enter a number >= 100")

#WHILE LOOP
y = int(input("how often should tom shower?"))
attempts=1
while y < 7:
    y = int(input("shower more (>=7)"))
    attempts = attempts + 1
print("acceptable ig")
print("took", attempts, "attempts to enter a number >=7")


#FOR LOOP
for i in range(10):
    print(i)

#LISTS:
fruits = ["apple", "pear", "banana", 9, -3.5, "hihihi"]
fruits.append("orange")
length = len(fruits)

for i in range(length):
    print(fruits[i])
"""

'''
colours = []
for i in range(6):
    colours.append(int(input("enter a number")))
print(colours)

#PRIMES
n = int(input("primes up to a number"))
primes = []
for i in range(2, n):
    prime = True
    for j in range(2, i):
        if i % j == 0:
            prime = False
            break
    if prime == True:
        primes.append(i)
print(primes)
'''
"""
#input 2 numbers and store in variables
#input an operation either '+', '-', '*', '/'
#do the operation on those 2 numbers
while True:
    x = int(input("enter a number if you please"))
    y = int(input("enter another govenor"))

    op = input("enter an operation either '+', '-', '*', '/': ")

    if op == "+":
        print(x+y)
    elif op == "-":
        print (x-y)
    elif op == "*":
        print (x*y)
    elif op == "/":
        print (x/y)

    else: print("invalid operation dummy")
"""

# Generate a random number
# Repeatedly ask the user for a number and give hints if it's too high or low
# Count the number of guesses it takes
