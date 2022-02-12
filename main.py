from name_functions import get_formatted_name

print("Enter 'q' at anytime to quit")
while True:
    first = input("\nPlease enter first name :")
    if first == 'q':
        break
    last = input("\nPlease enter last name :")
    if last == 'q':
        break

    formatted_name = get_formatted_name(first, last)
    print("\nNeatly formatted name : ", formatted_name)
