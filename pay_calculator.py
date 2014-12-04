# calculate pay

def get_hours_and_rate():
    hours = float(input("Enter hours: "))
    rate = float(input("Enter rate of pay: "))
    return hours, rate

def calculate_basic_pay(hours, rate):
    pay = hours * rate
    return pay

def calculate_overtime_pay(hours, rate):
    basic_pay = rate * 40
    overtime_hours = hours - 40
    overtime_pay = overtime_hours * rate * 1.5
    total_pay = basic_pay + overtime_pay
    return total_pay

def calculate_total_pay(hours, rate):
    if hours > 40:
        pay = calculate_overtime_pay(hours, rate)
    else:
        pay = calculate_basic_pay(hours, rate)
    return pay

def display_total_pay(total_pay):
    message = "Total pay: {}".format(total_pay)
    print(message)

def calculate_pay():
    hours, rate = get_hours_and_rate()
    total_pay = calculate_total_pay(hours, rate)
    display_total_pay(total_pay)

calculate_pay()
