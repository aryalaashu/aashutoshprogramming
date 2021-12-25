#remove an item from a set if it is present in the set
a={1,2,3,4,5,"Aashu"}
if "Aashu" in a:
    a.remove("Aashu")
print(a)