Python Functions
1. Function Without Parameters
def add():
    a=int(input("Enter value: "))
    b=int(input("Enter value: "))
    res=a+b
    print(res)

if __name__=="__main__":
    add()
2. Function With Parameters
def add(x,y):
    res=x+y
    print(res)

if __name__=="__main__":
    a=int(input("Enter value: "))
    b=int(input("Enter value: "))
    add(a,b)
3. Function With Return Value
def add(x,y):
    return x+y

if __name__=="__main__":
    a=int(input("Enter value: "))
    b=int(input("Enter value: "))
    res=add(a,b)
    print(res)
4. Function Returning Multiple Values
def cal(x,y):
    add=x+y
    sub=x-y
    mul=x*y
    div=x/y
    return add,sub,mul,div

if __name__=="__main__":
    a=int(input("Enter value: "))
    b=int(input("Enter value: "))
    r1,r2,r3,r4=cal(a,b)
    print(r1,r2,r3,r4)
Python Lists
ls=[11,22,33,44,55,66]

for i in range(len(ls)):
    print(ls[i])

for x in ls:
    print(x)

ls.append(12)
print(ls)

print(ls[0])      # first element
print(ls[-1])     # last element
print(ls[2:4])    # slicing
print(ls[::-1])   # reverse list
Python Strings
s="Ashish"

print(s[1:3])     # substring
print(s[::-1])    # reverse string

a=1234
print(len(str(a)))  # count digits
Reverse a String (Without Built-in Function)
a="rachit"
b=""

for i in a:
    b=i+b

print(b)

Output

tihcar
