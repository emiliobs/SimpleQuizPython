# Simple Quiz In Python

name = input("Please, Enter your Full  Name:- ")
print(f'Hello "{name.upper()}" , Welcome to Python Quiz......')
print("---------------------------------------------------------")

while True:
			total_question = 5
			correct = 0

		
			print("1. Start Quiz.")
			print("2. Exit.")
			print("------------------------------------------------------")

			options = input( "Enter your option (Press 1 to 'START' or  Press any othe key to 'EXIT'):- ")
			print()
			print()

			if options == "1":


				print("Question 1. :- What is single line comment is python?")
				print("a) //     b) /**/     c) #     	d) /")
				answer = input("Enter your answer (a/b/c/d) :- ").lower()

				if answer == 'c':
					correct += 1
				print()
				print()

				print("Question 2. :- s='Python programer', the output of s[-8:-2] = ?")
				print("a) mmargo     b) programmer     c) remmgorp     d) ogramm")
				answer = input("Enter your answer (a/b/c/d) :- ").lower()

				if answer == 'd':
					correct += 1
				print()
				print()

				print("Question 3. :- Statement to do nothing ?")
				print("a) continue     b) pass	     ) stop     d) break")
				answer = input("Enter your answer (a/b/c/d) :- ").lower()

				if answer == 'b':
					correct += 1
				print()
				print()

				print(
				    "Question 4. :- x = [i**2 for i in range(1,10) if i % 2 == 0] what is output ?")
				print("a) [2, 4, 6, 8, 10]     b) [0, 4, 16, 36, 64]     c) [4, 16, 36, 64]      ) [0, 4, 16, 36]")
				answer = input("Enter your answer (a/b/c/d) :- ").lower()

				if answer == 'c':
					correct += 1

				print()
				print()

				print("Question 5. :- What is the output of the program ?")
				print("if not 0:")
				print("     print('statement - 1')")
				print("else")
				print("     prin('statement - 2')")
				print("a) statement-1     	b) statement-2     c) error     	d) none")
				answer = input("Enter your answer (a/b/c/d) :- ").lower()

				if answer == 'a':
					correct += 1
				print()
				print()

				print("<===============================>")
				print(f"{name.upper()} You score {correct} out of {total_question}")
				print("=================================")
				print()
				
			else:
					exit()
             
						 
