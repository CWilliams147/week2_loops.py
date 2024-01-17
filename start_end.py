starting_number = int(input("Please Enter Starting Number: "))
ending_number = int(input("Please Enter Ending Number: "))

max_value = 1000

while starting_number <= ending_number and ending_number <= max_value:
    print(starting_number)
    starting_number += 7
else:
    ending_number > max_value
    print("Please Enter Valid End Number!")