def fib_series(n):
    if n==1:
        return 0

    elif n==2:
        return 1

    else:
        return fib_series(n-1) + fib_series(n-2)


def it_fib(n):
    a,b = 0,1

    if n==1:
        return a
    elif n==2:
        return b
    
    while n-2 > 0:
        c = a+b
        a,b=b,c
        n -= 1
    
    return c



num = int(input("Enter NO.: "))
iterative, recursive = [], []

for i in range(1, num+1):
    iterative.append(str(it_fib(i)))
    recursive.append(str(fib_series(i)))


print('iterative: ' + ' '.join(iterative))
print('Recursive' + ' '.join(recursive))