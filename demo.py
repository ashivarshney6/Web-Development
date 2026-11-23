# a=input("enter your first name:")
# # b=len(a)
# # print(b)
# c=a.count("$")
# print(f"$ comes {c} times.")
# light=input("what is the current light is showing?")
# if(light == "red"):
#     print("stop")
# elif(light == "green"):
#     print("you can go") 
# elif(light == "yellow"):
#     print("wait please!") 
# else:
#     print("light is broken")          
# marks=int(input("enter your marks:"))
# if(marks >= 90):
#     print("student grade is A")
# elif(90 > marks >=80):
#     print("student grade is B")
# elif(80 > marks >=70):
#     print("student grade is C")
# else:
#     print("student grade is D")            
# age=int(input("enter your age:"))
# if(age>=18):
#     if(age>=80):
#         print("you cannot drive.")
#     else:
#         print("you can drive.")    
# num=int(input("enter the number:"))
# if(num%2==0):
#     print("given number is even.")
# else:
#     print("given number is odd.")    
# num1=int(input("enter first number:"))
# num2=int(input("enter second number:"))
# num3=int(input("enter second number:"))
# if(num1>num2 and num1>num3):
#     print("num1 is the gretest number.")
# elif(num2>num3):
#     print("num2 is gretest number.")
# else:
#     print("num3 is gretest number.")    
# num=int(input("enter the number:"))
# if(num%7==0):
#     print("number is multiple of 7.")
# else:
#     print("number is not mulyiple of 7.")
# a = "ashi varshney"
# b=len(a)
# print(b)
# list=["ashi","riddhii","naitik","ashi"]
# list[0]="pooja"
# print(list)  
# str="my name is ashi varshney"
# a=str.replace("my","her")  
# print(a)
# list.insert(1,"pooja")
# print(list)
# list.remove("ashi")
# print(list)
# list.pop(1)
# print(list)
# tup=(1,2,3,4)
# print(type(tup))
# list=[]
# mov1=input("enter first movie:")
# mov2=input("enter second movie:")
# mov3=input("enter second movie:")
# list.append(mov1)
# list.append(mov2)
# list.append(mov2)
# print(list)
# list=[1,2,3,2,1]
# list1=list.copy()
# list1.reverse()
# if(list==list1):
#     print("list is palimdrome")
# else:
#     print("list is not palindrome")    
# list=["C","D","A","A","B","B","A"]
# # tup1=tup.count("A")
# # print(tup1)
# list.sort()
# print(list)

# # print(dict["name"])
# # print(dict["age"])
# # print(dict["location"])
# dict["name"]="riddhii"
# dict["surname"]="varshney"
# print(dict)
# student={
#     "name":"ashi",
#     "subject":{
#         "physics":98,"chemistry":99,"maths":100}
# }
# print(student["subject"]["physics"])
# dict={
#     "name":"ashi","age":"19","location":"aligarh","langauge":"python"
# }
# print(dict.keys())
# print(type(dict.keys()))
# dict.update({"subject":"english"})
# print(dict)
# dict["subject"]="english"
# print(dict) 
# collection={1,2,3,4,5}
# print(type(collection))
# marks_dict={}
# phy=int(input("enter marks of physics:"))
# chem=int(input("enter marks of chemistry:"))
# math=int(input("enter marks of maths:"))
# marks_dict.update({"physics":phy})
# marks_dict.update({"chemistry":chem})
# marks_dict.update({"maths":math})
# print(marks_dict)
# count=1
# while count<=5:
#     print("hello world")
#     count += 1
# print(count)       

# i=5
# while i>=1:
#     print(i)
#     i-=1
# print("print successfully")    
# i=1
# while i<=100:
#     print(i)
#     i+=1
# i=100
# while i>=1:
#     print(i)
#     i-=1
# n=int(input("enter the number:"))
# i=1
# while i<=10:
#     print(n*i)
#     i+=1
# i=0
# while i<=5:
#     if(i==3):
#         i+=1
#         continue
#     print(i)
#     i+=1
# i=0
# while i<=10:
#     if(i%2!=0):
#         i+=1
#         continue
#     print(i)
#     i+=1
# list=[1,2,3,4,5]
# for num in list:
#     print(num)
# str="apnacollege"
# for char in str:
#     if(char=="o"):
#         print("character o is found")
#         break
#     print(char)
# list=[1,4,9,16,25,36,48,64,81,100]
# for num in list:
#     print(num)
# list=[1,4,9,16,25,36,48,61,81,100]
# x=int(input("enter the number you want:"))
# indx=0
# for val in list:
#     if(x==val):
#         print("number is found at index",indx)
#         break
#     indx+=1   
# a=int(input("enter the number:"))
# count=0
# i=1
# while(i<=a):
#     if(a%i==0):
#         count+=1
#     i+=1    
# if(count==2):
#     print("it is prime number.")
# else:
#     print("it is not prime number.")  
# num=int(input("enter the number:"))
# count=0
# for i in range(1,num+1):
#     if(num%i==0):
#         count=count+1
# if(count==2):
#     print("it is a prime number")
# else:
#     print("it is not prime number") 


num=int(input("enter the number:"))
reverse=0
while(num>0):
    a=num%10
    reverse=reverse*10+a
    num=num//10
print(reverse)

