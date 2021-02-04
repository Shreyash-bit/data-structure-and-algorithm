from array import *


def create_array():
    arr = array('f', [])
    n = int(input("\nenter number of elements : "))
    for i in range(n):
        new = int(input("enter element : "))
        arr.append(new)
    return arr


def print_array(array_to_print):
    n = len(array_to_print)
    for i in range(n):
        print(array_to_print[i], end=' - ')


def part(a, low, high):
    i = low - 1
    p = a[high]         # p=pivot
    for j in range(low, high):
        if a[j] <= p:
            i = i + 1
            a[i], a[j] = a[j], a[i]
    a[i+1], a[high] = a[high], a[i+1]
    return i+1


def quick_sort(a, low, high):
    if len(a) == 1:
        return a
    if low < high:
        pi = part(a, low, high)
        quick_sort(a, low, pi-1)
        quick_sort(a, pi+1, high)


x = create_array()
m = len(x)
quick_sort(x, 0, m-1)
print("Sorted array is:")
print_array(x)

print("Top 5 scores are:")
for k in range(-1, -6, -1):
    print(x[k])
