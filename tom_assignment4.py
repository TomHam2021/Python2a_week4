import sys
'''
Your job here is to implement a context manager class, a generator for traversing the data in the 
text file and a decorator for tracking the time it takes for yours and Bad Code Inc’s function to 
run (this is to compare their performance). Remember that even though the difference might not seem 
huge, when handling a lot of files of large sizes, the differences can be big!

Setup
• Create a folder week4 for the assignment
• Download the text file eng_vocab.txt and put it in the folder
• Download the python code file provided by Bad Code Inc. (bad_code_inc.py) and rename it to 
  “firstname_assignment4.py”. For example: Emil_assignment4.py
• Run the code and make sure it works

Note: Their code has some flaws. They are not closing the file after use and they employ a try 
catch instead of a proper context manager.

Tasks
Tip: Following these steps in order will help in creating a good workflow.
• Start by creating a decorator to track the time it takes to run the function read_list. Your decorator 
  should print how long it takes for the function to run (Hint: Since timeit doesn’t give you the return 
  value of the timed function, you can instead use the time module to measure the time before and after 
  calling the decorated function. The time taken is then after - before.)
• Decorate read_list with your timer decorator and run the function to get an estimation of the runtime
  (for me it takes a little less than 0.1 seconds but can vary a lot between computers and other factors).
'''

from contextlib import contextmanager
import time

FILENAME = "eng_vocab.txt"
'''
def read_list():
    file = open(FILENAME, "r")
    return file.read().splitlines()


def main():
    try:
        text_list = read_list()
        print(sys.getsizeof(text_list), "Bytes are used by the list")
    except Exception:
        print("something is wrong")
'''

# Start by creating a decorator to track the time it takes to run the function read_list. Your decorator
# should print how long it takes for the function to run (Hint: Since timeit doesn’t give you the return
# value of the timed function, you can instead use the time module to measure the time before and after
# calling the decorated function. The time taken is then after - before.)
# Time consumed: 0.07654237747192383
# Time consumed: 0.11983561515808105
# Time consumed: 0.07588982582092285

# • Create a simple context manager class as we did in the lectures (the simplest version with just __enter__,
#   __exit__ and __init__ methods where you open the file in either __init__ or __enter__). Replace the current
#   try format with your context manager and make sure the code runs properly.
# • In the context manager where you open the file, implement a try-except section to catch the exception
#   FileNotFoundError. If the exception is caught the program should print “File not found” and then call exit()
#   which stops the code from executing further. Try it by changing to a filename that doesn’t exist in your
#   current folder ("dogcat.txt" is an excellent choice if you have trouble deciding what the non-existing file
#   should be called).
'''
@contextmanager
def my_context_manager(filename, operation):
    print("Open...")
    file = open(filename, operation)
    yield file
    print("Close...")
    file.close()
'''


def time_rec_decorator(function):
    start = time.time()   # starta tiden här...
    result = function()
    end = time.time()     # stanna tiden
    return end-start      # räkna och returnera tiden det tog
    # print(f"Time consumed: {end-start}")  # räkna och skriv ut tiden det tog


@time_rec_decorator
def read_list():
    file = open(FILENAME, "r")
    return file.read().splitlines()


FILENAME = "eng_vocab.txt"


def main():
    print(f"Time consumed: {read_list}")


if __name__ == "__main__":
    main()
