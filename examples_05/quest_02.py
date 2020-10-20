def print_multiplication_table():
    print("".rjust(4), end="")
    for i in range(1, 11):
        print(f"{i}".rjust(4), end="")
    print()

    for i in range(1, 11):

        print(f"{i}".rjust(4), end="")
        for j in range(1, 11):
            print(f"{i * j}".rjust(4), end="")
        print()
    pass


print_multiplication_table()
