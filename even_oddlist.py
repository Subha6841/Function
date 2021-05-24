# program for separated lis
def odd_evenlist(l1):
    l2=[]
    l3=[]
    l4=[]
    for i in l1:
        if i%2==0:
            l2.append(i)
        else:
            l3.append(i)
    l4.append(l2)
    l4.append(l3)
    return l4
l1=[]
n=int(input('Enter the no. of elemnts in the list : '))
print('Enter the elements of list ')
for i in range(n):
    ele=int(input())
    l1.append(ele)

print('The given list is : ')
print('The updated list is :',odd_evenlist(l1))


            
