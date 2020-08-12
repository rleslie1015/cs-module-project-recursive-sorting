# TO-DO: complete the helper function below to merge 2 sorted arrays
def  merge ( arrA , arrB ):
    elements  =  len(arrA) + len(arrB)
    merged_arr = [0] * elements

    # Your code here

    # need to assign pointers at the start of both lists
    a_pointer, b_pointer = 0, 0

    for item in range(len(merged_arr)):
        # if counter becomes of of range the next in the list should be the only element left in the other list
        if  a_pointer  >=  len(arrA): 
            merged_arr[item] = arrB[b_pointer]
            # pointer for list B moves
            b_pointer += 1 
        # if counter becomes of of range the next in the list should be the only element left in the other list
        elif b_pointer >= len(arrB):
            merged_arr[item] = arrA[a_pointer]
            # pointer for list A moves
            a_pointer += 1
        elif arrA[a_pointer] < arrB[b_pointer]: # compare the first of each list
            merged_arr[item] = arrA[a_pointer]
            # pointer for list A moves
            a_pointer += 1
        else: 
            merged_arr[item] = arrB[b_pointer]
            # pointer for list B moves
            b_pointer += 1
    return merged_arr

# TO-DO: implement the Merge Sort function below recursively
def merge_sort(arr):
    # Your code here
    if len(arr) > 1: 
        half = len(arr)//2 
        # divde in half until you have subarrays of length 1
        arr1 = arr[:half]
        arr2 = arr[half:]


        arr1 = merge_sort(arr1)
        arr2 = merge_sort(arr2)

        #merge sorted lists togehter
        arr = merge(arr1, arr2)

    return arr
example = [5, 3, 1]
merge_sort(example)

# STRETCH: implement the recursive logic for merge sort in a way that doesn't 
# utilize any extra memory
# In other words, your implementation should not allocate any additional lists 
# or data structures; it can only re-use the memory it was given as input
# def merge_in_place(arr, start, mid, end):
#     # Your code here
#     pass

# def merge_sort_in_place(arr, l, r):
#     # Your code here
#     pass
