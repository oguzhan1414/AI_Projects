#[expression for item in iterable if condition]


squares = [x**2 for x in range(10)]
print(squares)

numbers = [1,2,3,4,5,6,7]
kontrol = [x for x in numbers if x % 2 ==0 ]
print(kontrol)

names = ["Ali","Ayşe","Oguzhan","Fatma","Mustafa"]
short_names = [name for name in names if len(name) <5]
print(short_names)

labels = ["Even" if x % 2 ==0 else "Odd" for x in numbers]
print(labels)

numara = input("Okul numarasını girin")  ##2893
numara_liste = [int(x) for x in numara]
sonuc = []
for i in range(0,4):
    for j in range(0,4):
        if(numara_liste[i] + numara_liste[j] >= 10):
            print(f"{numara_liste[i]} + {numara_liste[j]}")
