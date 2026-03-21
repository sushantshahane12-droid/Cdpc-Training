# https://www.hackerearth.com/practice/basic-programming/input-output/basics-of-input-output/practice-problems/algorithm/roy-and-profile-picture/
  L=int(input())
  N=int(input())
  for i in range(N):
      W, H=map(int, input().split())
      if W<L or H<L:
          print("UPLOAD ANOTHER")
      elif W==H:
          print("ACCEPTED")
      else:
          print("CROP IT")
# Sample Input
  180
  3
  640 480
  120 300
  180 180
# Sample Output
# CROP IT
# UPLOAD ANOTHER
# ACCEPTED

# https://www.hackerearth.com/problem/algorithm/monk-and-rotation-3-bcf1aefe/
  T=int(input())
  for i in range(T):
      N, K=map(int, input().split())
      ar=list(map(int, input().split()))
      K=K%N
      new=ar[-K:]+ar[:-K]
      print(*new)
# Sample Input
  1
  5 2
  1 2 3 4 5
# Sample Output
  4 5 1 2 3

# Sample Input
  1
  5 2
  1 2 3 4 5
# Sample Output
  4 5 1 2 3 

# https://www.hackerearth.com/practice/basic-programming/input-output/basics-of-input-output/practice-problems/algorithm/modify-the-string/ 
 s = input()
 result = ""

 for i in s:
    if 'A' <= i <= 'Z':
         result += chr(ord(i) + 32)
     elif 'a' <= i <= 'z':
         result += chr(ord(i) - 32)
     else:
         result += i

 print(result)

# Sample Input
 abcdE
# Sample Output
 ABCDe

# Majority number in array:
 ar=list(map(int, input().split()))
 b=0
 for i in range(len(ar)):
     if ar.count(i)>(len(ar)/2):
         if i>b:
             b=i
 print(b)
