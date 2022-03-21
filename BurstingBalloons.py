points = [[1,2],[2,3],[3,4],[4,5]]
count = 0

for a in range(len(points)):
    flag = False
    for b in range(a+1, len(points)):
        if((points[a][0] >= points[b][0] and points[a][0] <= points[b][1])
            or (points[a][1] >= points[b][0] and points[a][1] <= points[b][1])):
            flag = True
    if(flag == False):
        count += 1
print(count)