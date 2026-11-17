integers = []
user_input = input("Enter integers separated by spaces: ")

for num in user_input.split():
    integers.append(int(num))


def find_max_min(integers):
    lowest = integers[0]
    highest = integers[0]

    for number in integers:
        if number < lowest:
            lowest = number
        elif number > highest:
            highest = number
    return lowest, highest


print(find_max_min(integers))
