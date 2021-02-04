# using iterative method
def merge(left, right):
    if len(left) == 0:
        return right

    if len(right) == 0:
        return left

    result = []
    index_left = index_right = 0

    while len(result) < len(left) + len(right):
        # The elements need to be sorted to add them to the
        if left[index_left] <= right[index_right]:
            result.append(left[index_left])
            index_left += 1
        else:
            result.append(right[index_right])
            index_right += 1

        # the result and break the loop
        if index_right == len(right):
            result += left[index_left:]
            break

        if index_left == len(left):
            result += right[index_right:]
            break
###############################################################
# using recursive method

    def merge_sort(array):
        # If the input array contains fewer than two elements,
        # then return it as the result of the function
        if len(array) < 2:
            return array

        midpoint = len(array) // 2

        # Sort the array by recursively splitting the input
        # into two equal halves, sorting each half and merging them
        # together into the final result
        return merge(
            left=merge_sort(array[:midpoint]),
            right=merge_sort(array[midpoint:]))

    return result
