"""
You are a robber. Given an array of house values, you cannot rob two adjacent houses.
Find the maximum amount you can rob.
```
[2,7,9,3,1]  →  12  (rob houses 0,2,4 → 2+9+1)
[2,1,1,2]    →   4  (rob houses 0,3 → 2+2)
```
"""

house = [2,7,9,3,1] 

house_count = len(house)

dp = [0] * house_count

dp[0] = house[0]
dp[1] = max(house[0], house[1])

for i in range(2, house_count):
    skip_house = dp[i-1]
    rob_house = house[i] + dp[i-2]
    dp[i] = max(skip_house, rob_house)

print(dp[house_count-1])