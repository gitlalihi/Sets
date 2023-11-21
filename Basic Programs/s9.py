#Python Set difference to find lost element from a duplicated array
arr1=[]
num=int(input("Enter your number of lists:"))
for i in range(num):
    ele=input("Enter your Elements:")
    arr1.append(ele)
print("Yours First list is:",arr1)    

arr2=[]
num2=int(input("Enter your number of lists:"))
for i in range(num2):
    ele2=input("Enter your Elements:")
    arr2.append(ele2)
print("Yours Second list is:",arr2)


def lostElement(arr1,arr2):
    A = set(arr1)
    B = set(arr2)
    if len(A) > len(B):
        print (list(A-B))
    else:
        print (list(B-A))
 
print("Your lost element is :" ,lostElement(arr1,arr2))