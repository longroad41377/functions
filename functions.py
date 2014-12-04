def OutputSymbols(count, symbol):
    for i in range(count):
        print(symbol, end="")

def OutputPyramid(size):
    rows = size // 2 + 1
    for row in range(rows):
        OutputSymbols(row, " ")
        OutputSymbols(size - (2 * row), "*")
        print()

def OutputDiamond(size):
    rows = size // 2
    for row in range(rows):
        OutputSymbols(rows - (row), " ")
        OutputSymbols(row * 2 + 1, "*")
        print()

    OutputPyramid(size)

while 1:
    size = int(input("Enter size: "))
    if size % 2:
        OutputDiamond(size)
