"""
    http://codeforces.com/problemset/problem/453/A
    the root problem: number of array A[n] of positive number that max(Ai) = x
    
      C(1,n)*(x-1)^(n-1) + C(2,n)*(x-1)^(n-2) + ...
    = x^n - (x-1)^n
    
    E = sum(i*(i^n-(i-1)^n)/m^n
      = sum(i*((i/m)^n - [(i-1)/m]^n)

"""
def power(a,n):
    if n == 1: return a
    x = power(a,n/2)
    if n%2==0:
        return x*x
    else:
        return x*x*a

m,n = map(int, raw_input().split())
result = sum(i * (power(i/1./m,n) - power((i-1)/1./m,n)) for i in range(1,m+1))
print result
