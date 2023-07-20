def fibonacci(range):
    if range<=1:
        return range
    else:
        return fibonacci(range-1)+fibonacci(range-2)

range=int(input("Enter the range : "))
print(fibonacci(range))