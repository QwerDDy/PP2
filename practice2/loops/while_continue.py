arr = [5,2,3,4,5]
first = 0
second = len(arr)-1
while first<=second:
    if arr[first] == arr[second]:
        first += 1
        second -= 1
        continue
    arr[first],arr[second] = arr[second],arr[first]
    first += 1
    second -= 1
for i in arr:
    print(i)
