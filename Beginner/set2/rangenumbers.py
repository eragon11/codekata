x = [int(i) for i in input().split()];

for i in range(x[0]+1,x[1]):
    if (i%2 != 0):
        print(i,end = " ")        