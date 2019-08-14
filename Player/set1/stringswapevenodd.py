swapString = str(input())

finalString = []
index = 0
str1 = []
str2 = []

for i in swapString:
    if (index % 2 == 0):
        str1.append(swapString[index])
    else:
        str2.append(swapString[index])
    index += 1

i = 0

while (i < (len(swapString)/2)):

    finalString.append(str2[i]);
    finalString.append(str1[i]);
    i += 1

print("".join(finalString))
