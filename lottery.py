def get_player_numbers():
    number_csv = input("PLease enter any 6 numbers between 0 and 20 sepetated by commas: ")
    # Now create a set of integers from this number_csv
 #   integer_set = {int(i) for i in numbers_csv.split(",")} #  {1, 2, 3, ...}
    # OR
    number_list = number_csv.split(",") # ['1', '2', '3',...]
    integer_set = {int(number) for number in number_list}
    return integer_set

print(get_player_numbers())
