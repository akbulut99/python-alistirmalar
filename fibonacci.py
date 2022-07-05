a = 1
b = 1
fib = [a, b]
for i in range(12):
    a, b = b, a + b
    fib.append(b)
    print(fib)
