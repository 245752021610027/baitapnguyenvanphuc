print("nguyen van phuc")
print("245752021610027")
print("###########################")
########*##*#####################
def tao_list_fibonacci(n):
    if n <= 0:
        return []
    
    a, b = 0,1
    ds_fib = []

    while a < n:
        ds_fib.append(a)
        a, b = b, a + b
        
    return ds_fib

try:
    n = int(input("Nhap so nguyen n: "))
    list_fib = tao_list_fibonacci(n)
    print(list_fib)
except ValueError:
    print("Gia tri nhap khong hop le.")
