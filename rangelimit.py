x = [int(i) for i in input().split()]
limit = int(input());

sumofn = 0;

for i in range(len(x)):
    if (i+1 <= limit):
        sumofn += x[i]

print(sumofn);