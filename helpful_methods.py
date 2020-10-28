def print_max_five(array):
    counter = 0
    for i in array:
        counter += 1
        if counter % 5 == 0 and not i == array[-1]:
            print(i + ",")
        elif not i == array[-1]:
            print((i + ", "), end = '')
        else:
            print(i)