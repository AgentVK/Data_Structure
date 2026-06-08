def find_max_consecutive_one(arr):
    max_count = 0
    count = 0
    for num in arr:
        if num == 1:
            count+=1
            max_count = max(max_count, count)
        else:
            count = 0
    return max_count

print(find_max_consecutive_one([1,1,1,0,0,1,1,1,1,1,1,1,0,0,1]))