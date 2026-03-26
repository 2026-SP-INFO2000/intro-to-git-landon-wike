def binary_search(arr, target):
    low, high = 0, len(arr) - 1
    
    while low <= high:
        mid = (low + high) // 2
        print(f"Checking index {mid}, value {arr[mid]}")  # optional for tracing
        
        if arr[mid] == target:
            return mid   # found
        elif arr[mid] < target:
            low = mid + 1  # search right half
        else:
            high = mid - 1 # search left half
    return -1  # not found


arr = [1, 3, 4, 5, 7, 9, 11]
target = 7
result = binary_search(arr, target)

if result != -1:
    print(f"Found {target} at index {result}")
else:
    print("Not found")