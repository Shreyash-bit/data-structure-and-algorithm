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


def linear_search(list_to_check, x1):        # function for searching linearly

    n = len(list_to_check)
    index = 0                            # initializing index as 0

    for i in range(0, n):

        if index < n:
            if list_to_check[index] == x1:        # compare x with each element in the list
                print("number {} is present at {} index".format(x1, index))
                break
            index += 1                  # increase index by 1
    else:
        print("not present!!!!")

list1 = create_list()
linear_search(list1, x)