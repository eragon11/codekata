x = str(input());

y = list(x);
y.reverse();

if (x == ("".join(y))):
    print("yes")
else:
    print("no");