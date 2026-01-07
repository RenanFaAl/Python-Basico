def fibo_recursividade(a):
    if a <= 1:
        return a
    return fibo_recursividade(a - 1) + fibo_recursividade(a - 2)

print(fibo_recursividade(10))

def fibo_iterativo(n):
    a, b = 0, 1
    for i in range(n):
        a, b = b, a + b
    return a
    
print(fibo_iterativo(10))

