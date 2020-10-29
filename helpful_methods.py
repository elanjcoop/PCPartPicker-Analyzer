def print_max_five(some_literal):
    counter = 0
    if type(some_literal) == list:
        for i in some_literal:
            counter += 1
            if counter % 5 == 0 and not i == some_literal[-1]:
                print(i + ",")
            elif not i == some_literal[-1]:
                print((i + ", "), end = '')
            else:
                print(i)
    elif type(some_literal) == dict:
        for key in some_literal:
            counter += 1
            if counter % 5 == 0 and not key == list(some_literal.keys())[-1]:
                print((key + ": "), end = '')
                print("{:.2f}".format(some_literal[key]), end = '')
                print((","))
            elif not key == list(some_literal.keys())[-1]:
                print((key + ": "), end = '')
                print("{:.2f}".format(some_literal[key]), end = '')
                print((", "), end = '')
            else:
                print((key + ": "), end = '')
                print("{:.2f}".format(some_literal[key]))