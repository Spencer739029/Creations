def bubble_sort(arr):
    """
    Sorts a list in ascending order using the Bubble Sort algorithm.

    Args:
        arr: The list of numbers to sort. The list is sorted in-place.
    """
    n = len(arr)
    # Traverse through all array elements
    for i in range(n):
        # Last i elements are already in place
        for j in range(0, n - i - 1):
            # Traverse the array from 0 to n-i-1
            # Swap if the element found is greater than the next element
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]

# Example usage:
if __name__ == "__main__":
    my_list = input("Enter numbers separated by spaces: ")
    my_list = list(map(int, my_list.split()))
    print("\nOriginal list:", my_list)

    bubble_sort(my_list)

    print("\nSorted list:", my_list)


    again = input("\nDo you want to sort another list? (yes/no): ").strip().lower()
    while again == 'yes':
        my_list = input("\nEnter numbers separated by spaces: ")
        my_list = list(map(int, my_list.split()))
        print("\nOriginal list:", my_list)

        bubble_sort(my_list)

        print("\nSorted list:", my_list)
        again = input("\nDo you want to sort another list? (yes/no): ").strip().lower()