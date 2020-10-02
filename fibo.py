def even_fibo(x):
    num = list(i for i in range(1, x + 1))
    fib =[]
    for i in num:
        fib.add(i + fib[fib.index(i) - 1])
        print (fib(6))










even_fibo(4)