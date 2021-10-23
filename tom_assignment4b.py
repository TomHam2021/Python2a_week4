from os import truncate
import sys
from contextlib import contextmanager
import time

from tom_assignment4 import FILENAME


# • Create a simple context manager class as we did in the lectures (the simplest version with just __enter__,
#   __exit__ and __init__ methods where you open the file in either __init__ or __enter__). Replace the current
#   try format with your context manager and make sure the code runs properly.
# • In the context manager where you open the file, implement a try-except section to catch the exception
#   FileNotFoundError. If the exception is caught the program should print “File not found” and then call exit()
#   which stops the code from executing further. Try it by changing to a filename that doesn’t exist in your
#   current folder ("dogcat.txt" is an excellent choice if you have trouble deciding what the non-existing file
#   should be called).
class MyFileContextManager:

    def __init__(self, filename, operation):
        # om filen inte finns så blir det fel här!
        #self._file = open(filename, operation)
        try:
            self._file = open(filename, operation)
        except FileNotFoundError:
            print("Please check the filename again.. ")
            # och sen då? Vad göra nu?
            self._file.__exit__  # fungera inte, hoppar aldrig till exit
            # self._file.close()   # fast det finns ju ingen öppen fil?!

    def __enter__(self):
        # print("File is opened and fetched")
        return self._file

    def __exit__(self, type, value, traceback):
        # print("Closing File")
        self._file.close()  # Alternative: self._file.__exit__()


def time_rec_decorator(function):
    start = time.time()   # starta tiden här...
    result = function()
    end = time.time()     # stanna tiden
    return end-start      # räkna och returnera tiden det tog


#FILENAME = "simple.txt"
FILENAME = "eng_vocab.txt"


@time_rec_decorator
def read_list():
    with MyFileContextManager(FILENAME, "r") as f:
        text = f.read()
        print(sys.getsizeof(text), "Bytes are used by read_list")
        # när man går ut "with" så anropas __exit__


# • Create a generator function called my_generator that yields each line in the text document
# • Create a function called read_generator that uses a for-loop to iterate through the generator.
#   Decorate it with the timer function and print the size of the generator (how many bytes of
#   memory it consumes).
# • Run the code and compare the performance of the generator vs the list. You should see a
#   large difference in memory usage and a difference in the speed of the two different functions
#   akin to something like below. Good to know is that the performance varies heavily depending
#   on what type of computer you use, you may for instance see similar execution time for both functions.

@time_rec_decorator
def my_generator():
    with MyFileContextManager(FILENAME, "r") as f:
        for row in f:
            # yield row          # <--- fungerar inte ????
            txt_row = row     # <--- fungerar
            # yield row         # <--- fungerar inte ???
        print(sys.getsizeof(txt_row), "Bytes are used by my_decorator")


def main():
    print(f"Time consumed (read_list): {read_list}")
    print(f"Time consumed (my_generator): {my_generator}")


if __name__ == "__main__":
    main()
