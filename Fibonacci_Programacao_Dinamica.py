def fibonacci_dinamico(n,firstIteration=True):
    if n<=1:
        return 1
    if fibs[n] > -1:
        return fibs[n]
    else:
        fibs[n] = fibonacci_dinamico(n - 1) + fibonacci_dinamico(n - 2)
        return fibs[n]

n = 20
fibs = [-1 for x in range(n+2)]
fibs[0], fibs[1] = 1, 1
for i in range(n):
    print(fibonacci_dinamico(i))
