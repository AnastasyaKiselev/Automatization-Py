def fizz_buzz(n):
    for x in range(0, n):
        if (x % 3 == 0) and (x % 5 == 0):
            print("FizzBuzz")
        elif x % 3 == 0:
            print("fizz")
        elif x % 5 == 0:
            print("buzz")
        else:    print(x)


fizz_buzz(18)