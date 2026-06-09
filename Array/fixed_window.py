arr = [2,1,5,1,3,2]
k = 3
window_sum = 0
best_sum = float("-inf")

for right in range(len(arr)):
    window_sum += arr[right]

    # right >= k: window_sum - arr[right-k]
    if right >= k:
        window_sum -= arr[right-k]

    #  start calculating best after right >= K-1 
    if right >= k-1:
        best_sum = max(best_sum, window_sum)
print(best_sum)

