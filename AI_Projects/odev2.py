def en_yakin_fibonacci(sayi):
    fib = [0, 1]
    while fib[-1] < 100:
        fib.append(fib[-1] + fib[-2])

    # En yakın olanı bul
    return min(fib, key=lambda x: abs(x - sayi))

okul_no = input("Okul numaranızı giriniz: ")
# Fibonacci kurallı yeni numara
fib_no = ""

for rakam in okul_no:
    if rakam.isdigit():
        yakin_fib = en_yakin_fibonacci(int(rakam))
        fib_no += str(yakin_fib)
    else:
        fib_no += rakam  

print("Orijinal okul numarası :", okul_no)
print("Fibonacci kuralına göre:", fib_no)