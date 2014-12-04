# functions
# development exercises
# 3

values = [1, 0.814, 0.625]
symbols = ["£", "€", "$"]

def ConvertCurrency(convert_from, convert_to, ammount):
    scaler = values[convert_from] / values[convert_to]
    return ammount * scaler

convert_from = input("Enter currency to convert from: ")
convert_to = input("Enter currency to convert to: ")
ammount = float(input("Enter ammount: "))

convert_from = symbols.index(convert_from)
convert_to = symbols.index(convert_to)

converted = ConvertCurrency(convert_from, convert_to, ammount)
print("{0}{1}".format(symbols[convert_to], converted))
