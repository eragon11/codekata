even = [int(i) for i in input().split()];

for i in range(even[0]+1,even[1]):
    if (i%2 == 0):
        print(i,end = " ")        