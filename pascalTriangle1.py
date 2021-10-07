#program to print pascal triangle in O(1)
n = int(input('Enter Number To Generate Pascal Triangle'))
print('Pascal Triangle Series Of No',n,'is : ')
for x in range(n):
  print(" "*(n-x),end=" ")
  print(" ".join(str(11**x)))
