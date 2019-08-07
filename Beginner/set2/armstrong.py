armstrong = int(input());


armlength = len(str(armstrong));

buffer = armstrong;
sum =0;
while (buffer > 0):
    digit = buffer % 10;
    sum += digit ** armlength;
    buffer //=10;

if(sum == armstrong):
    print("yes");
else:
    print("no");        