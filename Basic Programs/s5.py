#Python | Check if two lists have at-least one element common
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

def common_member(list1,list2):
    a_set = set(list1)
    b_set = set(list2)
    if (a_set & b_set):
        return True
    else:
        return False
print("Your common element is :",common_member(list1,list2))        