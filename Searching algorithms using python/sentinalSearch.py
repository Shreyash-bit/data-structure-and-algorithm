def create_list():                    # function to create new list
    m = 1
    new_list = []
    while True:

        elem = int(input("enter {}th element : ".format(m)))
        new_list.append(elem)                                # appending the entered element to the new_list
        m += 1

        do_again = input("want to stop appending, enter n : ")  # ask user to do the appending process again
        if do_again == 'n':
            break

    return new_list

def sentinel_search(list_to_check, x1):        # function for searching by sentinel method

    n = len(list_to_check)                 # here we are not initializing index = 0 (like in linear search)

    index = -1
    while index != n:
        index += 1

        if list_to_check[index] == x1:        # compare x with each element in the list
            print("number {} is present at {} index".format(x, index))
            break
    else:
        print("not present!!!!")


list1 = create_list()
sentinel_search(list1, x)