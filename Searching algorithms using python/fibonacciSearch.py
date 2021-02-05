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

list1 = create_list()# x = int(input("enter number to be searched : "))
print(fibonacci_search(sort(list1), x))