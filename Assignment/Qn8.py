#convert a tuple to a string
tuple = ('a', 'b', 'h', 'y', 'a', 's')
j=''
for i in tuple:
    i=j+i
    print(i,end='')
print()
print(type(i))