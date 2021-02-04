from array import *


def create_array():
    arr = array('i', [])
    n = int(input("\nenter number of elements : "))
    for i in range(n):
        x = int(input("enter element : "))
        arr.append(x)
    return arr


def print_array(array_to_print):
    n = len(array_to_print)
    for i in range(n):
        print(array_to_print[i], end=' - ')


# shell sort
def shell_sort(arr):
    print_array(arr)
    n = len(arr)
    gap = n // 2
    pass_count = 1

    while gap > 0:
        for i in range(gap, n, gap):
            j = i - gap
            key = arr[i]
            while arr[j] > key and j >= 0:
                arr[j + gap] = arr[j]
                j -= gap
            arr[j + gap] = key
        print("pass {} and gap is {}".format(pass_count, gap))
        print_array(arr)
        print(" ")
        pass_count += 1
        gap = gap // 2


while True:

    a = create_array()
    print("which sort method you want to use :\n"
          "1] SHELL SORT\n"
          "2] EXIT\n")

    ch = int(input())
    if ch == 1:
        shell_sort(a)

    if ch == 2:
        break
