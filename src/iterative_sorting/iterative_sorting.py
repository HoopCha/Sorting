# TO-DO: Complete the selection_sort() function below 

def selection_sort( arr ):
    # loop through n-1 elements
    for i in range(0, len(arr) - 1):
        cur_index = i
        smallest_index = cur_index
        # TO-DO: find next smallest element
        # (hint, can do in 3 loc) 
        for j in range(cur_index, len(arr)):
            if arr[j] < arr[smallest_index]:
                smallest_index = j

        # TO-DO: swap
        temp = arr[smallest_index]
        arr[smallest_index] = arr[cur_index]
        arr[cur_index] = temp

    return arr


# TO-DO:  implement the Bubble Sort function below
def bubble_sort( arr ):
    for i in range(len(arr)-1):
        for unsorted in range(len(arr)-1):
            if arr[unsorted] > arr[unsorted + 1]:
                temp = arr[unsorted + 1]
                arr[unsorted + 1] = arr[unsorted]
                arr[unsorted] = temp
    return arr


# STRETCH: implement the Count Sort function below
#assuming max is known beforehand 
def count_sort( arr ):
    m = max(arr) + 1
    print (m)
    count = [0] * m                
    for a in arr:
    # counts how often each number shows up
        count[a] += 1     
        print(count)       
    i = 0
    for a in range(m):         
        for c in range(count[a]):  
            arr[i] = a
            i += 1

    return arr


print(count_sort( [1, 2, 7, 3, 2, 1, 12, 12, 4, 2, 3, 2, 1, 5]))