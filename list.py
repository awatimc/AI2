list=[];

l=int(input("Enter number of value insert into list="));
i=0; 
for i in range(l):
    s=int(input(">>"));
    list.append(s);    

print("inserted value in the list");
for i in list:
    print(i);