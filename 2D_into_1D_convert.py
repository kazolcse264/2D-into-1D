n = int (input("Enter your 1st matrix size :"))
list1 = []
for i in range(n):
    list2 = []
    for j in range(n):
        list2.append(int(input()))
    list1.append(list2)
print(list1)
print("Your entered 1st matrix is :")
for i in  range(n):
    for j in range(n):
        print(list1[i][j],end=" ")
    print()
#2nd matrix
m = int (input("Enter your 2nd matrix size :"))
list3 = []
for i in range(m):
    list4 = []
    for j in range(m):
        list4.append(int(input()))
    list3.append(list4)
print(list3)
print("Your entered 2nd  matrix is :")
for i in  range(m):
    for j in range(m):
        print(list3[i][j],end=" ")
    print()
#addtion
print("Addition of two matrix :")

for i in  range(n):
    for j in range(n):
        list1[i][j] = list1[i][j] + list3[i][j]

for k in list1:
    print(k)
#print 1d list
print("This is 1D list :")
list5  = []
for i in  range(len(list1)):
    for j in range(len(list1)):
        list5.append(list1[i][j])

print(list5)