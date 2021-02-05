

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


def sort(list_to_check):
    n = len(list_to_check)

    for i in range(0, n):
        for j in range(i, n):
            if list_to_check[j] < list_to_check[i]:
                temp = list_to_check[i]
                list_to_check[i] = list_to_check[j]
                list_to_check[j] = temp

    return list_to_check


def fibonacci_generate(n):
    if n < 1:
        return 0
    elif n == 1:
        return 1
    else:
        return fibonacci_generate(n - 1) + fibonacci_generate(n - 2)
    
# return the index at which x exists inside arr
# return -1 otherwise


def fibonacci_search(list_to_check, x1):
    # find the smallest Fibonacci number greater than or equal
    # to the length of arr
    if x1 > list_to_check[len(list_to_check) - 1]:
        print("number not found")
        return -1
    m = 0
    while fibonacci_generate(m) <= len(list_to_check):
        m = m + 1

    offset = -1

    # make sure you fibonacci index is valid
    while fibonacci_generate(m) > 1:

        i = min(offset + fibonacci_generate(m - 2), len(list_to_check) - 1)

        if x1 > list_to_check[i]:

            m = m - 1
            offset = i

        elif x1 < list_to_check[i]:

            m = m - 2

        else:
            print("number {} is present ".format(x1))
            return i + 1

    # this will run if there is one last element left
    # if fibonacci_generate(m - 1) and list_to_check[offset + 1] == x1:
    #    return offset + 1

    # return -1 if the element doesn't exist in the array
    print("Element {} Not in the list".format(x1))
    return -1

# the search array
# arr = [10, 22, 30, 44, 56, 58, 60, 70, 100, 110, 130]
# x = 130
# print(FibonacciSearch(arr, x)


do = True
while do:

    list1 = create_list()
    # x = int(input("enter number to be searched : "))

    while True:

        x = int(input("\nenter number to be searched : "))
        
        print("\n 1] LINEAR \n 2] SENTINEL \n 3] BINARY \n 4] FIBONACCI \n 5] Exit")
        choice = input("enter choice : ")

        if choice == '1':
            linear_search(list1, x)
        if choice == '2':
            sentinel_search(list1, x)
        if choice == '3':
            binary_search(sort(list1), x)
        if choice == '4':
            print(fibonacci_search(sort(list1), x))

        if choice == '5':
            break

    ans = input("do you want to do the operations again (y/n) : ")
    if ans != 'y':
        break
