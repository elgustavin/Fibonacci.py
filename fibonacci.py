print("Welcome to Fibonacci!")

question = input("Let's start? [Y/N]: ")
if question.upper() == "Y":
    print("Ok, let's do it")
    
    number_count = int(input("How many numbers do you want in the sequence? "))
    fibonacci_sequence = [0, 1]

    for i in range(2, number_count):
        next_number = fibonacci_sequence[-1] + fibonacci_sequence[-2]
        fibonacci_sequence.append(next_number)

    print("The Fibonacci sequence is:", fibonacci_sequence)

else:
    print("Ok, Bye!")
