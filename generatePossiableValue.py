from tabulate import tabulate
import itertools
from itertools import combinations_with_replacement
b = input("Enter your tagrets : ")
# print(bsss)
arr = list(b.strip())
# print(arr)
x = len(arr)
count = 0
for i in range(1, x+1):
    l = list(itertools.product(arr, repeat=i))
    print("level" + str(i),
          " / number of possiable values in this level : " + str(len(l)))
    count += len(l)
    print(tabulate(l, tablefmt="fancy_grid"))
print("number of all values : ", str(count))
# l = [('a', 'a'), ('a', 's'), ('a', 'd'), ('s', 'a'), ('s', 's'),
#      ('s', 'd'), ('d', 'a'), ('d', 's'), ('d', 'd'),('a','s','r')]
# print(tabulate(l))
# #2
# import string
# print(("ID").ljust(15), ("Name").ljust(15), ("Age").ljust(15),("CGPA").ljust(15))
# data=[[1,"ahmed",21,3.7],[2,"Ola","20","3.9"]]
# "plain" ,# "simple",# "github",# "grid",# "fancy_grid",# "pipe"
# "orgtbl",# "jira",# "presto",# "psql",# "rst",# "mediawiki",# "moinmoin"
# "youtrack",# "html",# "latex",# "latex_raw",# "latex_booktabs",# "textile"
