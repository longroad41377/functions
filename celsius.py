def celsius(fahrenheit):
    return (fahrenheit - 32) * (5/9)

fahrenheit = int(input("enter temperature in fahrenheit: "))
print(celsius(fahrenheit))
