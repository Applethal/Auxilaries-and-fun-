horizontal = int(input("Input the number of rows"))
vertical = int(input("Input the number of collumns"))


def matrix(horizontal, vertical):
    matrix = []
    counter_r = 0
    counter_c = 0
    for row in range(vertical):
        row = []
        matrix.append(row)
        counter_r += 1
        for column in range(horizontal):
            if counter_c == horizontal:
                counter_c = 0
            counter_c += 1
            number = int(input(f"Input the number in column{counter_c}, row {counter_r} "))
            row.append(number)

    return matrix


matrix = matrix(horizontal, vertical)

for row in matrix:
    print(row)
