from math import dist

target = [3,4]
k = 5
df = [[2,4],[3,4],[1,3],[2,3],[1,6],[6,3]]
label = [1,1,1,2,2,2]

arr = [[a,b] for a,b in zip(df, label)]

for i in arr:
    distance = dist(target,i[0])
    i[0] = distance
    
arr = sorted(arr, key=lambda i:i[0])

case_one = 0
case_two = 0

for i in range(k):
    if arr[i][1] == 1:
        case_one += 1
    
    else:
        case_two += 1
        
if case_one > case_two:
    print("Choose Case 1")
else:
    print("Choose Case Two")
    