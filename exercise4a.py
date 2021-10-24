''' 
The task is to implement the only_numbers decorator. It should check if the user input can 
be converted to an int and if so call the decorated function, otherwise print a message 
that only numbers, q and p are allowed.
'''

numbers = []


def only_numbers(funcion):   # outer function
    def inner_function(s):   # inner function

        if s == "q":
            print("Exiting")
            return False
        elif s == "p":
            print(numbers)  # skriv ut alla tillagda nummer
            return True
        else:
            try:
                number = int(s)
                funcion(number)   # här läggs nummer in i listan
                return True
            except ValueError:
                print(f"'{s}' is not a valid number, try again...")
                return True

    return inner_function


@only_numbers
def add_number(s: str) -> bool:  # deta känns konstigt.. returnerar funktionen rätt?
    print("Add number: ", s)
    numbers.append(s)


looping = bool
while looping:
    s = input("add a number, q to quit, p to print: ")
    looping = add_number(s)
