arr_1 = [1,3,5,7,9]
arr_2 = [2,4,6,8,10]

i = 0
j = 0
result = []

while i < len(arr_1) and j < len(arr_2):
    if arr_1[i] < arr_2[j]:
        result.append(arr_1[i])
        i += 1
    else:
        result.append(arr_2[j])
        j += 1
while i < len(arr_1):
    result.append(arr_1[i])
    i += 1

while j < len(arr_2):
    result.append(arr_2[j])
    j+=1

print(result)