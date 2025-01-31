import re
LocationIDS=[]
ID1=[]
ID2=[]
similarity=[]
sum=0


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
     num=ID2.count(ID1[k])
     similarity.append(ID1[k]*num)
for i in range(0,len(similarity)):
    sum=sum+similarity[i]
print(similarity)
print(sum)
