def get_lines(file_name):
    file = open("account_activities.txt", "r", encoding="utf8")

    lines = [line.strip() for line in file.readlines()[1:]]

    file.close()

    return lines


def get_total_amounts(lines):
    total_amounts = {}

    for line in lines:
        columns = line.split(",")
        account_number = columns[0].strip()
        operation = float(columns[1].strip())

        total_amounts[account_number] = total_amounts.get(account_number, 0) + operation

    return total_amounts


lines = get_lines("account_activities.txt")

total_amounts = get_total_amounts(lines)

for key, value in total_amounts.items():
    print("Account number:", key)
    print("Total amount:", value)
    print()
