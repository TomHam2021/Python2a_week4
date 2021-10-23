#a = []
# help(a)
# print(dir(a))

# ----------------------------- ITERABLES -------------------------
'''
class Enthusiastic:
    def __init__(self, *words):
        self._words = [word + "!" for word in words]

    def __iter__(self):
        return iter(self._words)


enthusiastic = Enthusiastic("Oh", "my", "Volvo")
print(" ".join(enthusiastic))
'''
# ----------------------------- ITERABLES -------------------------
'''
class Enthusiastic:
    def __init__(self, *words):
        self._words = [word + "!" for word in words]

    def __getitem__(self, index):
        return self._words[index]


enthusiastic = Enthusiastic("Oh", "my", "Volvo")
print(" ".join(enthusiastic))
print(enthusiastic[0])      # man kan idexera när man använder __getitem__
'''
# ----------------------------- ITERATOR -------------------------
# An iterator can be created using iter and stepped through in a for loop or using next, but only once
# Objects with a __next__ method are usually iterators
# An iterator should contain both __next__ and __iter__
'''
import sys
class MultiplyByThree:
    def __init__(self, start_number):
        self._current = start_number

#    def __iter__(self):    # det funkar ändå om man tar bort __iter__
#        return self

    def __next__(self):
        self._current = self._current * 3
        return self._current


myMult = MultiplyByThree(2)
print(next(myMult), next(myMult), next(myMult))
print(sys.getsizeof(next(myMult)))
'''
# ----------------------------- ITERATOR -------------------------
'''
class CountToTen:
    def __init__(self, start_number):
        self._current = start_number

    def __iter__(self):             # här antopas __iter__ !
        return self                 # felkod om den itne finns med

    def __next__(self):
        if self._current < 10:
            self._current += 1
            return self._current
        raise StopIteration


for i in CountToTen(8):
    print(i)
'''
# ----------------------------- GENERATOR -------------------------
'''
# detta är en generator, pga den innehåller "yield"
def multiply_by_three(list1):
    for item in list1:
        yield item * 3  # yield kommer ihåg var den var sist!


myMult = multiply_by_three([1, 3, 5, 7, 9])
print(myMult)
print(next(myMult))     # denna skriver ut första = 1x3
print(next(myMult))     # denna skriver ut andra  = 3x3
print(list(myMult))     # denna skriver ut resten
'''
# detta gör samma som ovan men kallas "<genexpr>"
myMult = (item*3 for item in [1, 3, 5, 7, 9])
print(myMult)
print(next(myMult))
print(next(myMult))
print(list(myMult))

# Three must know concepts
# • Iterable: has __iter__ or __getitem__
# • Iterator: has __iter__ and __next__
# • Generator: produces an iterator

# ----------------------------- GENERATOR -------------------------
