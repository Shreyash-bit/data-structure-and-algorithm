def bubble_sort(array):
    n = len(array)

    for i in range(n):
        # Create a flag that will allow the function to
        already_sorted = True
        # Start looking at each item of the list one by one,
        for j in range(n - i - 1):
            if array[j] > array[j + 1]:
                array[j], array[j + 1] = array[j + 1], array[j]   # swapping the numbers
                already_sorted = False
        # If there were no swaps during the last iteration,
        if already_sorted:
            break

    return array
