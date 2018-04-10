def merge_sort(unsorted_list):
    if len(unsorted_list) > 1:
        midpoint = len(unsorted_list) // 2

        left = unsorted_list[:midpoint]
        right = unsorted_list[midpoint:]

        merge_sort(left)
        merge_sort(right)

        x = 0
        y = 0
        z = 0
        while x < len(left) and y < len(right):
            if left[x] < right[y]:
                unsorted_list[z] = left[x]
                x += 1
            else:
                unsorted_list[z] = right[y]
                y += 1

            z += 1

        while x < len(left):
            unsorted_list[y] = left[x]
            x += 1
            z += 1

        while y < len(right):
            unsorted_list[z] = right[y]
            y += 1
            z += 1

        return unsorted_list
    else:
        return unsorted_list
