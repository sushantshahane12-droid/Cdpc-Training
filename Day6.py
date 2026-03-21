# https://www.hackerrank.com/challenges/compare-the-triplets/problem
compare triplets-
def points(a,b):
     ap=0
     bp=0
      for i in range(3):
         if a[i]>b[i]:
            ap=ap+1
        elif a[i]<b[i]:
            bp=bp+1
     return(ap,bp)
# Input:
  5 6 7
  3 6 10
# Output:
  1 1

# https://www.hackerrank.com/challenges/a-very-big-sum/problem
# big sum
  def aVeryBigSum(ar):
     sum=0
      for i in range(len(ar)):
        sum += ar[i]
      return sum    
# Input:
  5
  1000000001 1000000002 1000000003 1000000004 1000000005
# Output:
  5000000015

# https://www.hackerrank.com/challenges/diagonal-difference/problem
  def diagonalDifference(arr):
      sum1=0
      sum2=0
      n=len(arr)
      for i in range(n):
          sum1=sum1+arr[i][i]
          sum2=sum2+arr[i][n-1-i]
      return abs(sum1-sum2)
# Input:
  3
  11 2 4
  4 5 6
  10 8 -12
# Output:
  15

# https://www.hackerrank.com/challenges/plus-minus/problem
  def plusMinus(arr):
      n = len(arr)
    
       positive = 0
       negative = 0
       zero = 0
     
       for num in arr:
          if num > 0:
              positive += 1
          elif num < 0:
              negative += 1
          else:
             zero += 1
    
      print(f"{positive/n:.6f}")
      print(f"{negative/n:.6f}")
      print(f"{zero/n:.6f}")
# Input:
  6
  -4 3 -9 0 4 1
# Output:
  0.500000
  0.333333
  0.166667

# Rotate array:
  ar=eval(input("Enter: "))
  n=int(input("enter n: "))
  len=len(ar)
  ar=ar[len-n:]+ar[:len-n]
  print(ar)
# Output: 
  Enter: [2,4,5,6,2]
  enter n: 3
  [5, 6, 2, 2, 4]
