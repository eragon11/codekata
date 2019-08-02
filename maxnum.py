arr = [int(input()) for i in range(3)];

print (arr);

max_no = 0;

for i in arr:
    if(i > max_no):
        max_no = i;
    else:
        i = max_no;


print (max_no);