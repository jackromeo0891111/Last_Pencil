import random

users = ["John",  "Jack"]
print("How many pencils would you like to use:")
check_num_input = True
check_name_input = True
#check pencil number input integrity
while check_num_input:
    num_of_pencils_input = input()
    if num_of_pencils_input.isdigit() and num_of_pencils_input != "0":
        num_of_pencils = int(num_of_pencils_input)
        check_num_input = False
    elif num_of_pencils_input == "0":
        print("The number of pencils should be positive")
    else:
        print("The number of pencils should be numeric")
print(f"Who will be the first ({users[0]}, {users[1]}):")
#check player name input integrity
while check_name_input:
    current_user_input = input()
    if current_user_input not in users:
        print(f"Choose between {users[0]} and {users[1]}")
    else:
        current_user = current_user_input
        check_name_input = False
print("|" * num_of_pencils)
while num_of_pencils != 0:
    # user[0] is human
    if current_user == users[0]:
        print(f"{current_user}'s turn:")
        check_pencil_taken = True
        while check_pencil_taken:
            take_pencil_input = input()
            if take_pencil_input not in ["1", "2", "3"]:
                print("Possible values: '1', '2' or '3'")
            elif int(take_pencil_input) > num_of_pencils:
                print("Too many pencils were taken")
            else:
                take_pencil = int(take_pencil_input)
                check_pencil_taken = False
        num_of_pencils -= take_pencil
        print("|" * num_of_pencils)
        current_user = users[1]
    #user[1] is bot
    elif current_user == users[1]:
        print(f"{current_user}'s turn:")
        if num_of_pencils == 1:
            take_pencil = 1
        elif num_of_pencils % 4 == 2:
            take_pencil = 1
        elif num_of_pencils % 4 == 3:
            take_pencil = 2
        elif num_of_pencils % 4 == 0:
            take_pencil = 3
        elif num_of_pencils % 4 == 1:
            take_pencil = random.randint(1,3)
        num_of_pencils -= take_pencil
        print(take_pencil)
        print("|" * num_of_pencils)
        current_user = users[0]
print(f"{current_user} won!")