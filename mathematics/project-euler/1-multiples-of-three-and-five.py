# Function calculates sum of multiples of k less than n
def sum_multiples(n,k):
    sum = 0
    if n >= k:
        for i in range(1,int(n/k)):
            sum += k*i
        # It should be range(1,int(n/k)+1) for k such that n % k != 0, so
        if n % k != 0:
            sum += int(n/k)*k
    return sum

# Function calculates sum of all multiples of 3 or 5 below n
def sum_multiples_3_5(n):
    return sum_multiples(n,3) + sum_multiples(n,5) - sum_multiples(n,15)

# Read input
t = int(input().strip())
for j in range(t):
    n = int(input().strip())
    print(sum_multiples_3_5(n))