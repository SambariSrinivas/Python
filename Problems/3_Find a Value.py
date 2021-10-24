"""Find a Value present in a given list or not
This program expects a user input, if any exception occurs an error message will be displayed.

"""
numbers = [2, 3, 54, 89, 35, 76, -9]
try:
    search_num = int(input("Enter a Value to search : "))
except:
    print("Invalid Number!")
else:
    found = False
    for num in numbers:
        if num == search_num:
            print(f"Your number {search_num} has found in the list")
            found = True
            break
        else:
            found = False
    if not found:
        print(f"Your number {search_num} has not found in the list")
finally:
    print("Bye Bye ==== Task has completed")
