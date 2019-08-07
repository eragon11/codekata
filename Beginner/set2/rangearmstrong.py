armstrong = [int(i) for i in input().split()];

for i in range(armstrong[0],armstrong[1]):
    buffer = i;
    sum =0;    
    while (buffer > 0):
        digit = buffer % 10;
        sum += digit ** len(str(i));
        buffer //=10;
    if(sum == i):
        print(sum, end=" ");