		# Simple Quiz In Python

name = input("Please, Enter your Full  Name:- ")
print(f'Hello "{name.upper()}" , Welcome to Python Quiz......')
print("---------------------------------------------------------")

while True:
	total_question = 5
	correct = 0


print("---------------------------------------------------------")
print("1. Start Quiz.")
print("2. Exit.")
print("---------------------------------------------------------")

options  = int(input("Enter your option (Press 1 to 'START' or  Press any othe key to 'EXIT'):- "))
print()
print()

if options == 1:

	print("Question 1. :- What is single line comment is python?")
	print("a) //					b) /**/					c) #					d) /")
	answer = input("Enter your answer (a/b/c/d) :- ").lower()

	if answer  == 'c':
		correct += 1
		print()
		print()


	print("Question 2. :- s='Python programer', the output of s[-8:-2] = ?")
	print("a) mmargo					b) programmer					c) remmgorp					d) ogramm")
	answer = input("Enter your answer (a/b/c/d) :- ").lower()

	if answer  == 'd'
		correct += 1
		print()
		print()


