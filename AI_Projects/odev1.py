###Soru1 : Okul Numaranızın son hanesine göre tek olanlar 1 den yüze tek sayılar çift olanlar 1 den yüze kadar çift sayılar #########

okul_no = input("Okul Numarası son hanesini gir ")

okul_no = int(okul_no)

if okul_no % 2 == 0:
    toplam = 0
    for i in range(2, 101, 2):
        toplam += i
    print("Çift sayıların toplamı:", toplam)

else:
    toplam = 0
    for i in range(1, 101, 2):
        toplam += i
    print("Tek sayıların toplamı:", toplam)


