# n=10
# if n%2==0:
#    print('n is even number',n)

# n=int(input('enter the num:'))
# if n%2==0:

#    print('n is even number',n)
# else:
#    print('n is odd number',n)    



# a=int(input('enter the number:'))
# b=int(input('enter the number:'))
# if a>b:
#    print('a is greater than b')
# else:
#    print('b is greater than a') 
 

# write a program to extract all the strings from the given list whose length is more than three
# a=['Kundhana' ,12,'Kundhu',5+6j,'Black','purple','evt']
# out=[]
# i=0
# while i<len(a):
#    if type(a[i])==str and len(a[i])>3:
#        out+=[a[i]]
#    i+=1    
# print(out)



# n=int(input('enter the number:'))
# count=0
# for i in range(1,6):
#    if n%i==0:      
#          count+=1
# if count==2:
#   print('the given number is prime number')
# else:
#   print('the number is not a prime number')                                                   

# to reverse the given number
# n=int(input('enter the numer:'))
# rev=0
# while n!=0:
#    rem=n%10
#    rev=rev*10+rem
#    n=n//10
# print(rev)


# to check given number is palindrome or not 
# n=int(input('enter the numer:'))
# rev=0
# temp=n
# while n!=0:
#    rem=n%10
#    rev=rev*10+rem
#    n=n//10
# if temp==rev:
#    print('number is palindrome')
# else:
#    print('number is not palindrome')       


# to count the number of digits in a given number
# n=int(input('enter the number'))
# c=0
# while n!=0:
#    n=n//10
#    c+=1
# print(c)    


# to find armstrong number

# n=int(input('enter the number'))
# t=n
# #a=n
# sum=0
# while n!=0:
#    n=n//10
#    c+=1
# while a!=0:
#  a=a//10
# if sum==t:
#    print('the given number is armstrong number')
#   print('the given number is  not an armstrong number')


# n=int(input('enter the given number'))
# n1=0
# n2=1
# sum
# for i in range(0,num):
#    print(sum)
#    n1=n2
#    n2=sumsum=n1+n2

# a='kundhana from EEE'.split()
# i=0
# out{}
# while i<len(a):
#    out[a[i]]=a[i][::-1]+str(len[a[i]])
#    i+=1
# print(out)


# to print a table
# num=int(input('enter the given number:'))
# i=1
# #   print(num,'*',i,'=',num*i)
# a=764
# i+=1


# n=764
# sum=0
# while n!=0:
#  rem=n%10
#  n=n//10
# print(sum)

# write a program to extract all the strings from the given list whose length is more than three
# a=['Kundhana' ,12,'Kundhu',5+6j,'Black','purple','evt']
# out=[]
# i=0
# while i<len(a):
#    if type(a[i])==str and len(a[i])>3:
#        out+=[a[i]]
#    i+=1    
# print(out)

#  write a program to execute upper case to lower case
# a='kundhana'
# i=0
# while i<len(a):
#     if 'a'<=a[i],='z':
#     out

# a='collectionc'
# i=0
# out={}
# while i<len(a):
#     if a.count(a[i])>1:
#         out[a[i]]=a.count(a[i])
#     i+=1
# print(out)      


# a='aabacdcdeacd'
# i=0
# out=''
# while i<len(a):
#     if a[i] not in out:
#         out+=a[i]+str(a.count(a[i]))
#     i+=1
# print(out)        

#write a program to check string is palindrome or not
# n=input('enter the string:')
# out=''
# i=len(n)-1
# while i>=0:
#     out+=n[i]
#     i-=1
# if out==n:
#     print('palindrome')    
# else:
#     print('not')


# a='aaabcddcca'
# i=0
# c=1
# out=''
# while i<len(a)-1:
#     if a[i]==a[i+1]:
#         c+=1
#     else:
#         out+=a[i]+str(c)
#         c=1
#     i+=1
# out+=a[-1]+str(c)
# print(out)            


# a=['hello',3+5j,9,8,[1,2,3],'ab','python']
# out={}
# i=0
# while i<len(a):
#     if type(a[i])==str:
#         out[a[i]]=len(a[i])
#     i+=1
# print(out)        

# a=[717,'hello',111,3+4j,231,999]
# i=0
# out=[]
# while i<len(a):
#     if type(a[i])==int and str(a[i])==str(a[i])[::-1]:
#         out+=[a[i]]
#     i+=1
# print(out)    


# a=[1,2,1,'hiee',2,'hieee']
# out=[]
# i=0
# while i<len(a):
#     if a[i] not in out:
#         out+=[a[i]]
#     i+=1
# print(out)        

# a='((())(())'
# i=0
# c=0
# c1=0
# while i<len(a):
#     if a[i]=='(':
#         c+=1
#     elif a[i]==")":
#         c1+=1
#     i+=1 
# print(c-c1)         


#perfect number or not
# a=int(input("enter the number:"))
# i=1
# sum=0
# while i<a:
#     if a%i--0:
#         sum+=i
#     i+=1
# if a==sum:
#     print('perfect number')
# else:
#     print('not')  



# a='python progrmming while loop'.split()
# out={}
# i=0
# while i<len(a):
#     if 'p' in a[i]:
#         out[a[i]]=1
#     else:
#          out[a[i]]=0
#     i+=1     
# print(out)         


# a='Hai Hello'
# i=0
# out={}
# while i<len(a):
#     out[a[i]]=[a[i],len(a[i])*2,str(len(a[i]))+a[i][::-1]]
#     i+=1
# print(out)    


# a='hello'
# b='bye'
# out=''
# i=0
# while i<max(len(a),len(b)):
#     if i<len(a):
#         out+=a[i]
#     if i<len(b):
#         out+=b[i]
#     i+=1
# print(out)            
 

# for i in range(1,11):
#     print(i,end='')


# for i in 'python':
#     print(i)

# for i in [1,2,3]:
#     print(i)


# for i in ['Kundhana','Bhumika','Nandini','Hemu']:
#     print(i)

# a='python'
# out=''
# for i in a:
#     if 'A'<=i<='Z':
#         out+=1
# print(out)        


# a='python is very easy'.split()
# out={}
# for i in range(len(a)):
#     if i%2==0:
#         out[a[i]]=len(a[i])
#     else:
#         out[a[i]]=a[i][::-1]
# print(out)        



# a='abcaeda'
# out=''
# for i in a:
#     if 'a'<=i<='z':
#         out+=str(ord(i)-96)
# print(out)        

# a='aqsbdtz'
# out=''
# for i in a:
#     if 'a'<=i<='z':
#         out+=chr(ord(i)+1)
#     elif i=='z':
#         out+=a
# print(out)     


#to print extension 
# a=['pro.py','home.html','google.com','gmail.com','yahoo.in']
# out=[]
# for i in a:
#  i=i.split('.')
#  out+=['.'+str(i[1])]
# print(out) 
                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                   
