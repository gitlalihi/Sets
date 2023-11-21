#Python | Difference between two lists
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

s = set(list2)
result = [x for x in list1 if x not in s]
print(result)