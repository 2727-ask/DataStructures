#program to print pascal triangle in O(1)
n = 5
for x in range(n):
  print(" "*(n-x),end=" ")
  print(" ".join(str(11**x)))
