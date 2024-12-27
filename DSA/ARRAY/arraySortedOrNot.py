arr1 = [2,3,5,6,7,9]
arr2 = [1,7,3,8,2,5,9]


def sortedChecker(arr):
    for i in range(len(arr)-1):
        if arr[i] > arr[i+1]:
            print("array is not sorted.")
            return
    print("Array is sorted")   

sortedChecker(arr2)        