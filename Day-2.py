Basic Python Programs (Short)
1. Even or Odd
n=int(input("Enter no: "))
if n%2==0:
    print("Even")
else:
    print("Odd")
2. Largest of Three Numbers
b=0
for i in range(3):
    a=int(input("Enter no: "))
    if a>b:
        b=a
print("Largest:",b)
3. Positive, Negative or Zero
a=int(input("Enter no: "))
if a>0:
    print("Positive")
elif a<0:
    print("Negative")
else:
    print("Zero")
4. Divisible by 3 and 5
a=int(input("Enter no: "))
if a%3==0 and a%5==0:
    print("Divisible by both 3 and 5")
else:
    print("Not divisible")
5. Print Numbers 1 to N
n=int(input("Enter n: "))
for i in range(1,n+1):
    print(i)
6. Print Even Numbers from 1 to N
n=int(input("Enter n: "))
for i in range(1,n+1):
    if i%2==0:
        print(i)
7. Sum of First N Natural Numbers
n=int(input("Enter n: "))
s=0
for i in range(1,n+1):
    s=s+i
print("Sum:",s)
8. Factorial of a Number
n=int(input("Enter no: "))
f=1
while n>0:
    f=f*n
    n=n-1
print("Factorial:",f)
9. Multiplication Table
n=int(input("Enter no: "))
for i in range(1,11):
    print(n*i)
10. Count Digits
a=int(input("Enter no: "))
count=0
while a>0:
    count+=1
    a=a//10
print(count)
11. Reverse a Number
a=int(input("Enter no: "))
rev=0
while a>0:
    rem=a%10
    rev=rev*10+rem
    a=a//10
print(rev)
12. Palindrome Number
a=int(input("Enter no: "))
temp=a
rev=0
while a>0:
    rem=a%10
    rev=rev*10+rem
    a=a//10
if temp==rev:
    print("Palindrome")
else:
    print("Not Palindrome")
13. Sum of Digits
a=int(input("Enter no: "))
s=0
while a>0:
    rem=a%10
    s+=rem
    a=a//10
print(s)
14. Armstrong Number
a=int(input("Enter no: "))
temp=a
s=0
while a>0:
    rem=a%10
    s+=rem**3
    a=a//10
if temp==s:
    print("Armstrong")
else:
    print("Not Armstrong")
15. Numbers Divisible by 7 (1 to N)
n=int(input("Enter n: "))
for i in range(1,n+1):
    if i%7==0:
        print(i)
