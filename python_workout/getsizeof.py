# show the number of bytes
import sys

mylist = []
for i in range(25):
    l = len(mylist)
    s = sys.getsizeof(mylist)
    print(f'len = {1}, size = {s}')
    mylist.append(i)
