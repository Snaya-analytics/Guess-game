
'''
we are going to right a program that generate 
the random number and asks the user to guess it.

'''


import random
n = random.randint(1,100)
a = -1
guesses = 1
while (a != n):
    a = int(input("Guess the number :"))
    if (a>n):
        print("lower number please")
        guesses += 1
    elif(a<n):
        print("higher number please")
        guesses += 1
        
print(f"you have the guess the number{n},correctly in {guesses} attempt")