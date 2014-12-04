import random

def DoGame():
    counters = GetInitailCounters()
    player = True
    while counters > 0:
        take_counters = TakeCounters(player, counters)
        player = not player

        counters -= take_counters
        print("Counters: {}".format(counters))

    if player:
        print("You win")
    else:
        print("You lose")

def TakeCounters(player, counters):
    if player:
        take_counters = 0
        while take_counters < 1 or take_counters > 3:
            take_counters = int(input("Enter counters to take: "))
            if take_counters < 1 or take_counters > 3:
                print("You can only take 1, 2 or 3 counters")
            else:
                return take_counters
    else:
        return random.randint(1, 3)

def GetInitailCounters():
    while 1:
        counters = int(input("Enter number of counters: "))
        if counters < 10 or counters > 50:
            print("counters must be between 10 and 50")
        else:
            return counters

DoGame()
