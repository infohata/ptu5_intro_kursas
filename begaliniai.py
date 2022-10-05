def poriniai():
    number = 2
    while True:
        yield number
        number += 2

def fibonacci():
    a, b = 0, 1
    while True:
        yield a
        a, b = b, a+b

lyginiai = poriniai()
fibai = fibonacci()

counter = 0
while True:
    print(counter, next(fibai))
    c = input("ENTER for next number, 'x/q' to quit:")
    if c.casefold() == "x" or c.casefold() == "q":
        break
    counter += 1
