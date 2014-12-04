# functions improvement exercise
# times-table tester
import random

def correct_message():
    print('Well done, you got the correct answer!')

def incorrect_message(answer):
    print('Sorry, you got the answer wrong. The correct answer is',answer)

def get_answer(question):
    answer = input(question)
    return answer

def ask_question(question, answer):
    user_answer = get_answer(question)
    if answer == user_answer:
        correct_message()
    else:
        incorrect_message(answer)

# main program
print("Times-table tester")
print()
testTable = input("Which times-table do you want to be tested on? ")
testTable = int(testTable)
for questions in range(1,6):
    Num1 = testTable
    Num2 = random.randrange(2,13)
    Ans = Num1 * Num2
    ask_question(str(Num1) + ' x ' + str(Num2) + ' = ? ',str( Ans))

