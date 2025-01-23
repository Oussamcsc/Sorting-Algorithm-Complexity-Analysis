import random

def selection_sort(arr):
    """Sorts the array elements from least to greatest and returns the operation count."""
    n = len(arr)
    op_count = 0
    for i in range(n - 1):
        least = i
        for j in range(i + 1, n):
            op_count += 1  # Count comparisons
            if arr[least] > arr[j]:
                least = j
        arr[i], arr[least] = arr[least], arr[i]
        op_count += 1  # Count swaps
    return op_count

def insertion_sort(arr):
    """Sorts the array elements from least to greatest and returns the operation count."""
    n = len(arr)
    op_count = 0
    for i in range(1, n):
        val = arr[i]
        j = i - 1
        while j >= 0 and val < arr[j]:
            arr[j + 1] = arr[j]
            j -= 1
            op_count += 2  # Count assignments and comparisons
        arr[j + 1] = val
        op_count += 1  # Count assignments
    return op_count

def bubble_sort(arr):
    """Sorts the array elements from least to greatest and returns the operation count."""
    n = len(arr)
    op_count = 0
    for i in range(n - 1):
        made_swaps = False
        for j in range(0, n - i - 1):
            op_count += 1  # Count comparisons
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
                made_swaps = True
                op_count += 1  # Count swaps
        if not made_swaps:
            break
    return op_count

if __name__ == "__main__":
    n = 30
    arr1 = [random.randint(0, n) for _ in range(n)]
    arr2 = list(arr1)
    arr3 = list(arr1)
    print("List =", arr1)
    selection_sort(arr1)
    insertion_sort(arr2)
    bubble_sort(arr3)
    print("Selection Sort:", arr1)
    print("Insertion Sort:", arr2)
    print("Bubble Sort:", arr3)
