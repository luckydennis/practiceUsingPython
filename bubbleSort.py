


def bubble_sort(arr):
    
    swapping = True
    length_arr = len(arr)

    while swapping:
        
        swapping = False
        for i in range(length_arr -1):
            if arr[i] > arr[i +1]:
                temp = arr[i]
                arr[i] = arr[i+1]
                arr[i+1] = temp
                swapping = True
        
        length_arr -=1
    
    return arr
            


