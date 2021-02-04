from array import *   # import everything from array library


def create_array():   # function to create array
    arr = array('i', [])
    n = int(input("\nenter number of elements : "))
    for i in range(n):   # accept input using for loop
        x = int(input("enter element : "))
        arr.append(x)
    return arr


def print_array(array_to_print):  # function to to print array elements in a format
    n = len(array_to_print)
    for i in range(n):
        print(array_to_print[i], end=' - ')


def ins_sort(arr):   # insertion sort method
    print_array(arr)
    n = len(arr)    # set n = length of array

    for i in range(1, n):  # for i in range of length of array
        j = i - 1
        key = arr[i]
        while j >= 0 and arr[j] > key:
            arr[j + 1] = arr[j]
            j = j - 1
        arr[j + 1] = key

    print_array(arr)


while True:        # menu driven approach

    a = create_array()
    print("which sort method you want to use :\n"
          "1] INSERTION SORT\n"
          "2] EXIT\n")
    ch = int(input())
    if ch == 1:
        ins_sort(a)
    if ch == 2:
        break
