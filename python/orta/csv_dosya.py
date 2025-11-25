import csv

with open("../txt_csv_vs/kullanicilar.csv", "r") as file:
    reader = csv.reader(file)
    for row in reader:
        print(row)

with open("../txt_csv_vs/kullanicilar.csv", "r") as file:
    read = csv.DictReader(file)
    for row in read:
        print(row)

"""
with open("new_kullanicilar.csv","w") as file:
    writer = csv.writer(file)
    writer.writerow(["ID","Isim","Soyisim","Sehir"])
    writer.writerow(["4","Mehmet","Kaya","Bolu"])
"""
