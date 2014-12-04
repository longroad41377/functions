# functions
# development exerises
# 1

def CalculateSeconds(hours, minutes, seconds):
    return (hours * 3600) + (minutes * 60) + seconds

hours = int(input("Enter hours: "))
minutes = int(input("Enter minutes: "))
seconds = int(input("Enter seconds: "))

print("Seconds: {}".format(CalculateSeconds(hours, minutes, seconds)))
