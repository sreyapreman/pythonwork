#1
# r=int(input("Enter the rows:"))
# for i in range(1,r+1):
#     for j in range(i):
#         print("*",end=" ")
#     print()


# 2
# r=int(input("Enter the rows:"))
# for i in range(1,r+1):
#     for s in range(r-i):
#         print(" ",end="")
#     for j in range(i):
#         print("*",end=" ")
#     print( )
#reverse
#3
# r=int(input("Enter the row:"))
# for i in range(r):
#     for s in range(i):
#         print(" ",end="")
#     for j in range(r-i):
#         print("*",end=" ")
#     print( )
#
#4
# r=int(input("Enter the row:"))
# for i in range(r):
#     for j in range(r-i):
#         print("*",end=" ")
#     print( )
'''NUMBER PATTERN'''
#5
# r=int(input("Enter the row:"))
# for i in range(1,r+1):
#     for j in range(i):
#         print(j+1,end=" ")
#     print( )

#6
# r=int(input("Enter the row:"))
# for i in range(1,r+1):
#     for s in range(r-i):
#         print(" ",end="")
#     for j in range(i):
#         print(j+1,end=" ")
#     print( )

#reverse

# r=int(input("Enter the rows:"))
# for i in range(1,r+1):
#     for j in range(r-i):
#         print(j+1,end=" ")
#     print( )
#
# r=int(input("Enter the rows:"))
# for i in range(r,0,-1):
#     for j in range(i,0,-1):
#         print(j,end=" ")
#     print( )

'''Alphabet'''
# r=int(input("enter the rows:"))
# k=ord("A")
# for i in range(1,r+1):
#     for j in range(i):
#         print(chr(k),end=" ")
#         k=k+1
#     print( )