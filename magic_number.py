import random 

def ask_user_and_check_number():
    user_number = int(input("Enter a number between 0 and 9: "))
    if user_number in magic_number:
        print('You got it right')
    if user_number not in magic_number:
        print('You did not quite get it')

magic_number = [random.randint(0, 9), random.randint(0, 9)]

def run_programme_x_time(chances):
    for i in range(chances): # range chances is [0, 1, 2]
        print("This is {} attempt". format(i + 1))
        ask_user_and_check_number()

chances = int(input("Enter the number of chances: "))
run_programme_x_time(chances)
