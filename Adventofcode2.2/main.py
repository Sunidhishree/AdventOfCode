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
    asc = sorted(report)
    dec = sorted(report, reverse=True)



    if report==asc:
        for k in range(0,(len(asc)-1)):
            if (asc[k+1]-asc[k])>=1 and (asc[k+1]-asc[k])<=3:
                safe=1
            else:
                safe=0
                break;
        if safe==1:
            level+=1
    elif report==dec:
        for k in range(0, (len(dec)-1)):
            if abs((dec[k + 1] - dec[k])) >= 1 and abs((dec[k + 1] - dec[k])) <= 3:
                safe = 1
            else:
                safe = 0
                break
        if safe == 1:
            level += 1
    else:

        if (len(report)-len(set(asc) & set(report)))<=1:
            for k in range(0, (len(asc) - 1)):
                if (asc[k + 1] - asc[k]) >= 1 and (asc[k + 1] - asc[k]) <= 3:
                    safe = 1
                else:
                    safe = 0
                    break;
            if safe == 1:
                level += 1
        if (len(report)-len(set(dec) & set(report)))<=1:
            for k in range(0, (len(dec) - 1)):
                if abs((dec[k + 1] - dec[k])) >= 1 and abs((dec[k + 1] - dec[k])) <= 3:
                    safe = 1
                else:
                    safe = 0
                    break
            if safe == 1:
                level += 1




print(level)