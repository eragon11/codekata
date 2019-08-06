n = int(input());

limit = int(input());

for i in range(1,n+1):
    x.append(input())

sumofn = 0;
print(x);
for i in range(len(x)):
    if (i+1 <= limit):
        sumofn += x[i]

print(sumofn);