# a=18^21
# print(a)
# b=17<<3
# print(b)
# c=9<<4
# print(c)
# a=21>>2
# print(a)
# b=84>>3
# print(b)
# print("hello world",end="")
# print("hello world")
# for i in range(1,6):
#     for j in range(0,i):
#         print("*" , end="")
#     print("") 
# a=int(input("enter the number:"))
# if(a>=0 and a<=10):
#     print("lying between 0-10")
# elif(a>=11 and a<=20):
#     print("lying between 11-20")
# elif(a>=21 and a<=30):
#     print("lying between 21-30")
# elif(a>=31 and a<=40):
#     print("lying between 31-40")
# elif(a>=0 and a<=10):
#     print("lying between 41-50")
# else:
#     print("your number is greater than 50")                     
# num=int(input("enter the number:"))
# if(num==0):
#     print("number is zero ")
# elif(num%2!=0):
#     print("number is odd")
# elif(num%2==0):
#     print("number is even")    
# 
# for i in range(0,5):
#     for j in range(0,5):
#         print("*", end="")
#     print("") 
# a=5
# for i in range(0,a):
#     for j in range(0,a-i-1):
#         print(" ",end="")
#     for j in range(0,2*i+1):
#         print("*",end="")    
#     print() 
# a=3
# for i in range(0,a):
#     for j in range(0,a-i-1):
#         print(" ",end="")
#     for j in range(0,2*i+1):
#         print("*",end="")
#     print()    
# b=2
# for k in range(0,2):
#     for m in range(0,(b-1)*k+1):
#         print(" ",end="")
#     for m in range(0,3,-2):
#         print("*",end="")    
#     print()                  
# a=12
# while(a<=12):
#     a+=1
#     print("hello world")
# a=int(input("enter the number:"))
# count=0
# for i in range(1,a+1):
#     if(a%i==0):
#         count+=1
# if(count==2):
#     print("it is a prime number.")
# else:
#     print("it is not a prime number.")

                
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

# a=int(input("enter the prime number:"))
# count=0
# i=1
# while(i<=a):
#     if(a%i==0):
#         count+=1
#     i+=1
# while(count!=2):
#     break
# print("hello world")



# prime=0
# while(prime<1):
#     count=0
#     i=1
#     a=int(input("enter the number"))
#     while(i<=a):
#         if(a%i==0):
#             count+=1
#         i+=1
#     if(count!=2):
#         break


# a=3
# while(a%2!=0):
#     a=int(input("enter the number:"))    

    
# def calcsum(a,b):
#     return a + b


# sum=calcsum(5,10)
# print(sum)    
# def print_hello():
#     print("hello world")

# a=print_hello()
# print(a)
# def average(a,b,c):
#     sum=a+b+c
#     average=sum/3
#     return average

# average=average(5,25,30)
# print(average)
# def calc_prod(a=5,b=10):
#     print(a*b)
#     return a*b
# calc_prod()
# calc_prod(2,4)
# def print_ele(list):
#     for item in list:
#         print(item,end=" ")
        

# print_ele([1,2,3,4,5])
# def fact(n):
#     factorial=1
#     for i in range(1,n+1):
#         factorial=factorial*i
#     print(factorial)
# fact(5)        
# def conv(usd):
#     inr=usd*90
#     print("indian rupee = ",inr)
#     return(inr)
# conv(2)    


#1
# n=int(input("enter the number"))
# items=list(map(int,input("enter price and quantity").split()))
# total=0
# for i in range(0,2*n,2):
#     price=items[i]
#     quantity=items[i+1]
#     total+=price*quantity
# if total>5000:
#     total=total*0.90
#     if total>=5000:
#         total=total*0.95
# if total<3000:
#     total=total+100
#     print("final bill:",total)
#     print("free delivery:","no")
# else:
#     print("free delivery:","yes")                

# 2
# password=input()
# upper=0
# lower=0
# digit=0
# special=0
# for char in password:
#     if char.isupper():
#         upper=1
#     elif char.islower():
#         lower=1
#     elif char.isdigit():
#         digit=1
#     else:
#         special=1
# count=upper+lower+digit+special
# print("character type=",count)
# if count==4:
#     print("diverse=","yes")
# else:
#     print("diverse= no")   



#3
# n=int(input())
# count=0
# for i in range(n):
#     prices=int(input())
#     if prices>1000:
#         count=count+1
# percentage=(count/n)*100        
# print("Expensive Items:",count)        
# print(f"Percentage:{percentage:.2f}")


#4
# n=int(input())
# dict={}
# for i in range(n):
#     name=input()
#     score=float(input())
#     dict[name]=score
# total=sum(dict.values())
# average=total/n  


# list=[10,20,30,40]
# nlist=list.copy()
# nlist.append(10)
# print(list)  
# print(nlist)
words=input().split()
b={}
for word in words:
    word=word.lower()
    b[word]=b.get(word,0)+1


a=input().split()
b={}
for items in a:
    category,amount=item.split(:)
    amount=int(amount)
    b[category]=b.get(category,0)+amount
    
                



                    
    



