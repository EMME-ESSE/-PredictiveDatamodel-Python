# The algorithm repeatedly divides the list in half depending on the mid value until it finds the element x.
# lista is the list of numbers that I want to search within.
# low is the lowest index of the current range being searched, and it changes as the list is updated.
# high is the highest index of the current range being searched, and it changes as the list is updated.
# x is the value that I'm searching for.


def binary_search(lista, low, high, x):

    if low <= high:
        mid = (high + low) // 2
        if lista[x] == mid:
            return mid
        elif arr[mid] > x:
            return binary_search(arr, low, mid - 1, x)

        else:
            return binary_search(arr, mid + 1, high, x)
 
    else:

        print("SOMETHING HAPPENDS...")

arr = [ 2, 3, 4, 10, 40 ]
x = 10
 

result = binary_search(arr, 0, len(arr)-1, x)
 
if result != -1:
    print("Element is present at index", str(result))
else:
    print("Element is not present in array")