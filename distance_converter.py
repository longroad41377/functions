# functions
# stretch and challenge exercise
# 1

def ImperialToMetric(feet, inches):
    centimetres = inches * 2.54
    centimetres += feet * 30.48
    return centimetres

def MetricToImperial(centimetres, metres):
    inches = centimetres * 0.397
    inches += metres * 39.37
    feet = inches * 0.0833333
    return inches, feet
    

mode = input("What measurement system do you want to convert to? ")

if mode == "metric":
    feet = float(input("Enter number of feet: "))
    inches = float(input("Enter number of inches: "))
    centimetres = ImperialToMetric(feet, inches)
    print("{0:.2} cm".format(centimetres))
elif mode == "imperial":
    metres = float(input("Enter number of metres: "))
    centimetres = float(input("Enter number of centimetres: "))
    inches, feet = MetricToImperial(centimetres, metres)
    
    print("{0:.2f} inches".format(inches))
    print("{0:.2f} feet".format(feet))
