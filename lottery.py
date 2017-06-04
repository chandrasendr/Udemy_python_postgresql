import random

# Step:3 Then we match the user numbers to the lottery numbers
def menu():
    # Ask player for numbers
    player_number = get_player_numbers()
    
    # Calculate lottery numbers
    lottery_number = create_lottery_numbers()
    
    # Print out the winnings
    winnings = player_number.intersection(lottery_number)
    print("You won ${}!".format(100 ** len(winnings)))

# Step:1 User can pick 6 numbers
def get_player_numbers():
    number_csv = input("PLease enter any 6 numbers between 0 and 20 sepetated by commas: ")
    # Now create a set of integers from this number_csv
 #   integer_set = {int(i) for i in numbers_csv.split(",")} #  {1, 2, 3, ...}
    # OR
    number_list = number_csv.split(",") # ['1', '2', '3',...]
    integer_set = {int(number) for number in number_list}
    return integer_set

# Step:2 Lottery calculates 6 random numbes (between 1 and 20)
def create_lottery_numbers():
    values = set() # We cannot initialize an empty set like so: {}
    while len(values) < 6: # Range in [0, 1, 2, 3, 4, 5]
        values.add(random.randint(1, 20))
    return values

    
menu()

