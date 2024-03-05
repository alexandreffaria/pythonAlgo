import time, numpy as np

searchSize = 10000
haystack = np.random.randint(10000, size=searchSize)

def linearSearch(haystack, needle):
    for i in range(len(haystack)):
        print(f"Looking at: {i}:{haystack[i]}. Needle is: {needle}")
        if haystack[i] == needle:
            print(f"Needle {needle} found at index: {i}")
            return True
        # time.sleep(.1)
    print(f"No {needle} in the haystack")
    return False

linearSearch(haystack, 42)