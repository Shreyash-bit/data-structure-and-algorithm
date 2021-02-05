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


def sort(list_to_check):
    n = len(list_to_check)

    for i in range(0, n):
        for j in range(i, n):
            if list_to_check[j] < list_to_check[i]:
                temp = list_to_check[i]
                list_to_check[i] = list_to_check[j]
                list_to_check[j] = temp

    return list_to_check


def binary_search(list_to_check, x1):        # function for searching by binary method

    n = len(list_to_check)              # (the input list must be sorted for binary search)

    lowest = 0                            # initializing lowest as 0
    highest = n                           # initializing highest as n(that is length of the list)
    iterations = 1                        # initializing index as 0
    while True:
        if iterations > n / 2:  # we are counting iterations to break out of the loop (else while will an infinite loop)
            print("{} is not in the list!!!!".format(x1))
            break
        iterations += 1

        mid = int((lowest + highest) / 2)

        if list_to_check[0] == x1:
            print("number {} is present ".format(x1))
            break
        if list_to_check[mid] == x1:
            print("number {} is present ".format(x1))
            break
        if x1 < list_to_check[mid]:         # if x is less than current mid value then make highest = mid-1
            highest = mid - 1
        if x1 > list_to_check[mid]:         # if x is greater than current mid value then make lowest = mid+1
            lowest = mid + 1

        if iterations > n / 2:  # we are counting iterations to break out of the loop (else while will an infinite loop)
            print("{} is not in the list!!!!".format(x1))
            break
        iterations += 1

list1 = create_list()
binary_search(sort(list1), x)