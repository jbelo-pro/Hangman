# place `import` statement at top of the program
from random import randint, seed

# don't modify this code or variable `n` may not be available
n = int(input())

# put your code here
seed(n)
print(randint(-100, 100))
