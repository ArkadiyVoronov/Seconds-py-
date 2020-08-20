def f(n):
    try:
        x = 10 / n
        print("x is " + str(x))
        f(n-1)
        print("survived!")
    finally:
        print("Bye from f where n = " + str(n))

f(4)
