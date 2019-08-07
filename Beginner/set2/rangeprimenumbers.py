rangeprime = [int(i) for i in input().split()];

for i in range(rangeprime[0]+1,rangeprime[1]):
    count = 0;
    for innerprime in range(2,i):
        if(i%innerprime == 0):
         count = count + 1;
    if (count <=0):
         print(i, end = " ");    