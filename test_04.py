from contextlib import contextmanager


@contextmanager
def my_context_manager(filename, operation):
    print("Open...")
    file = open(filename, operation)
    yield file
    print("Close...")
    file.close()


with my_context_manager("textFile.txt", "r") as f:
    text = f.read()

print("Print...")
print(text)
