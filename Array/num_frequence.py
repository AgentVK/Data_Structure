# def num_freq(arr):
#     window = {}
#     for val in arr:
#         window[val] = window.get(val,0) + 1
#     return window

# print(num_freq([2,2,2,3,3,5,5,5,5,7,7,7,9,2])[5])
# # get the freq of 5


#-----------------------

from collections import Counter

arr = [2,2,2,3,3,5,5,5,5,7,7,7,9,2]

freq = Counter(arr)
print(freq[9])