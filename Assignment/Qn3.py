#count the number of strings where the string length is 2 or more and the first and last character are same from a given list of strings
a=['aba','121','kgf','abc']
y=0
for x in a:
    if len(x)>2:
        if x[0]==x[len(x)-1]:
            y=y+1
print(y)