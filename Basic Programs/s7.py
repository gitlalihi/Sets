#Python | Find missing and additional values in two lists
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


print("Missing values in second list:", (set(list1).difference(list2)))
print("Additional values in second list:", (set(list2).difference(list1)))

print("Missing values in first list:", (set(list2).difference(list1)))
print("Additional values in first list:", (set(list1).difference(list2)))