reports=[]
ID1=[]
ID2=[]
similarity=[]
level=0
safe=0

while True:
    line = input()
    if not line:
        break
    reports.append(line)

for j in range(0,len(reports)):
    r=reports[j].split()
    report=[]
    for i in r:
        report.append(int(i))
    asc=sorted(report)

    dec=sorted(report,reverse=True)

    if report==asc:
        for k in range(0,(len(report)-1)):
            if (report[k+1]-report[k])>=1 and (report[k+1]-report[k])<=3:
                safe=1
            else:
                safe=0
                break;
        if safe==1:
            level+=1
    elif report==dec:
        for k in range(0, (len(report)-1)):
            if abs((report[k + 1] - report[k])) >= 1 and abs((report[k + 1] - report[k])) <= 3:
                safe = 1
            else:
                safe = 0
                break;
        if safe == 1:
            level += 1
    else:
        level+=0

print(level)




