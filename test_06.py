def print_number(s: str) -> bool:
    print(s)
    if s == "q":
        print("Exiting..")
        return False
    else:
        return True


looping = bool

while looping:
    s = input("add a number, q to quit, p to print: ")
    looping = print_number(s)
