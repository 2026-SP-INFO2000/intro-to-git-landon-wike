def bubble_sort(arr):
    n = len(arr)
    for i in range(n):
        print(i)
        # Assume the list is already sorted
        sorted_flag = True

        for j in range(0, n - i - 1):
            if arr[j] > arr[j + 1]:
                # Swap the elements
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
                sorted_flag = False  # Found unsorted pair
        
        # If no swaps happened, list is sorted
        if sorted_flag:
            print(f"Pass {i+1}: No swaps → already sorted ✅")
            break
        else:
            print(f"Pass {i+1}: Swaps happened → continue 🔁")

    return arr


nums = [2, 3, 4, 5, 6]
print("Original:", nums)
sorted_nums = bubble_sort(nums)
print("Sorted:", sorted_nums)