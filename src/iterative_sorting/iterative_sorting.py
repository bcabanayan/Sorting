# TO-DO: Complete the selection_sort() function below 
def selection_sort( arr ):
    # loop through n-1 elements
    for i in range(0, len(arr) - 1):
        cur_index = i
        smallest_index = cur_index
        # TO-DO: find next smallest element
        # (hint, can do in 3 loc)
        for j in range(cur_index + 1, len(arr)):
            if arr[j] < arr[smallest_index]:
                smallest_index = j
        # TO-DO: swap
        arr[i], arr[smallest_index] = arr[smallest_index], arr[i]
    return arr

# TO-DO:  implement the Bubble Sort function below
def bubble_sort( arr ):
    sorted = False
    while sorted == False:
        sorted = True
        for i in range(0, len(arr) - 1): # loop through array
            j = i + 1 # index of next element
            temp = arr[i] # set temporary value equal to current value  
            if arr[i] > arr[j]:
                arr[i] = arr[j]
                arr[j] = temp
                sorted = False
    return arr

# STRETCH: implement the Count Sort function below
def count_sort( arr, maximum=-1 ):

    return arr

