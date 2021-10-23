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
            self._file.close()   # fast det finns ju ingen öppen fil?!

    def __enter__(self):
        print("File is opened and fetched")
        return self._file

    def __exit__(self, type, value, traceback):
        print("Closing File")
        self._file.close()  # Alternative: self._file.__exit__()

        if type == ValueError:
            print("ValueError detected, ignore and proceed")
            return True
        # detta funkar inte! borde finnas i construktorn.
        if type == FileNotFoundError:
            print("Please check the filename again.. ")


#  textFile2.txt finns inte och då kommer valueError att köras! ... eller?
with MyFileContextManager("textFile2.txt", "r") as f:
    text = f.read()
    print("Final operation before close")
    # när man går ut "with" så anropas __exit__

print(text)
