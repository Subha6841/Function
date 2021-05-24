# program for common elements of two given list
def common_elements(l1,l2):
    l3=set(l1)
    l4=set(l2)
    l5=l3 & l4
    result=list(l5)
    return result
# main program
l1=[]
n1=int(input('Enter the number of elements of first list : '))
print('Enter the elements of the first list : ')
for i in range(n1):
    ele=float(input())
    l1.append(ele)
l2=[]
n2=int(input('Enter the number of elements of second list : '))
print('Enter the elements of the second list : ')
for i in range(n2):
    ele=float(input())
    l2.append(ele)
print('The given first list is : ',l1)
print('The given second list is : ',l2)
print('The list of common numbers is :',common_elements(l1,l2))

        
