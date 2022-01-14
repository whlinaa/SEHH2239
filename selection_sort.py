# 2022-01-14 07:20:59

def selection_sort(a):
    """early termination version of in-place selection sort. 
    this version finds the max element in each iteration.

    Args:
        a (sequence): sequence of numbers to be sorted in-placed. 
    """    
    n = len(a) # number of elements in the input sequence
    sorted = False
    i = n-1 # start from the last element, which has index n-1. 
    
    while i>0 and not sorted:
        max_index = 0 # find the max index, starting from the first element
        sorted = True
        for j in range(1, i+1): 
            if a[max_index] < a[j]: # find a number larger than the current max
                max_index = j
            else:
                sorted = False
        a[i], a[max_index] = a[max_index], a[i] # swap elements
        i-=1

# sanity check
a = [1,2,3,1,10,2,-1]
selection_sort(a)
print(a)



