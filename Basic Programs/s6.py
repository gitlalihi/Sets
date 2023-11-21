#Python program to find common elements in three lists using sets
list1=[]
num=int(input("Enter your number of lists:"))
for i in range(num):
    ele=input("Enter your Elements:")
    list1.append(ele)
print("Yours First list is:",list1)    

list2=[]
num2=int(input("Enter your number of lists:"))
for i in range(num2):
    ele2=input("Enter your Elements:")
    list2.append(ele2)
print("Yours Second list is:",list2)   

list3=[]
num3=int(input("Enter your number of lists:"))
for i in range(num3):
    ele3=input("Enter your Elements:")
    list3.append(ele3)
print("Yours Third list is:",list3)   

def find_common(list1, list2, list3):
    common = set()
    for value in list1:
        if value in list2 and value in list3:
            common.add(value)
    return common

common = find_common(list1, list2, list3)
print(common)