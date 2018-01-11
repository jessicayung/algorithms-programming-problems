def solveMeFirst(a,b):
  return a+b

num1 = int(input())
num2 = int(input())
res = solveMeFirst(num1,num2)
print(res)


def solveMeSecond(a,b):
   return a+b
n = int(input())
for i in range(0,n):
    a, b = input().split()
    a,b = int(a),int(b)
    res = solveMeSecond(a,b)
    print (res)
