# All positive numbers in a range.
l=int(input("Enter the number:"))
list1=[]
list2=[]
# Gathering input from the user
for i in range(l):
    t=int(input("Enter the number:"))
    list1.append(t)
# Checking the number is positive or negative
for j in list1:
    if j>0:
        list2.append(j)
print(list2)