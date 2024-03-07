import time, numpy as np

searchSize = 1000000
haystack = np.random.randint(1000000, size=searchSize)
haystack = sorted(haystack)

def binarySearch(haystack, needle):
    low = 0
    high = len(haystack) - 1 

    while (low < high):
        middle = low + (high - low) // 2
        hay = haystack[middle]
        print(f"hay: {hay} | needle: {needle} | middle: {middle} | low: {low} | high {high}")
        # print(haystack)
        
        time.sleep(0.1)
    
        if needle == hay:
            print(f"Needle found at: {middle}")
            return True
        elif hay < needle:
            low = middle + 1
        elif hay > needle: 
            high = middle 

    return False


print(binarySearch(haystack, np.random.randint(searchSize)))