
def second_largest(arr):
    largest = float("-inf")
    second_largest = float("-inf")

    for value in arr:
        if value > largest:
            second_largest = largest
            largest = value
        elif value > second_largest and value != largest:
            second_largest =  value
        
    if second_largest == float("-inf"):
        return None
    return second_largest

val = second_largest([2,3,5,8,12,1,7])

print(val)