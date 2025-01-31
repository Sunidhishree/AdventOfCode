import re
LocationIDS=[]
ID1=[]
ID2=[]
distance=[]
sum=0

LocationIDS = []
while True:
    line = input()
    if not line:
        break
    LocationIDS.append(line)

for j in range(0,len(LocationIDS)):
    n=LocationIDS[j].split()
    ID1.append(int(n[0]))
    ID2.append(int(n[1]))
    ID1.sort()
    ID2.sort()
for k in range(0,len(LocationIDS)):
    diff=ID1[k]-ID2[k]
    distance.append(abs(diff))
for i in range(0,len(distance)):
    sum=sum+distance[i]
print(distance)
print(sum)
