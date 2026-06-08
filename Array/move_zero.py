nums = [0, 1, 0, 3, 12]

slow = 0

for fast in range(len(nums)):
    if nums[fast] != 0:
        nums[slow], nums[fast] = nums[fast], nums[slow]
        slow +=1
# for i in range(slow+1, len(nums)):
#     nums[i] = 0

print(nums)