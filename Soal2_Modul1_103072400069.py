#  mencari Fibo ke-n
def fibonacci(n):
    if n <= 0:
        return 0
    elif n == 1 or n == 2:
        return 1
    else:
        a = 1
        b = 1
        for i in range(3, n + 1):
            c = a + b
            a = b
            b = c
        return b


# mencetak deret Fibonacci
def cetakFibo(n):
    a = 1
    b = 1
    print("Deret Fibonacci:")

    for i in range(1, n + 1):
        if i == 1 or i == 2:
            print(1, end=" ")
        else:
            c = a + b
            print(c, end=" ")
            a = b
            b = c

n = int(input("Masukkan nilai n: "))
print("Fibonacci ke-", n, "adalah:", fibonacci(n))
cetakFibo(n)