
a=open ("a.txt", "r")
for i, line in enumerate(a):
   if i % 2 != 0 :
       print(line)