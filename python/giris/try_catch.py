try:
    num = int(input("Enter a number"))
    resul = 10 / num
    print("Result",resul)

except ZeroDivisionError:
    print("Error : Division by zero is not allowed")
except ValueError:
    print("Error : Invalid input Please enter a valig number")

except (ZeroDivisionError,ValueError):
    print("BU ŞEKİLDE ÜSTTEKİLERİ BİRLEŞTİRDİK")
#else: bir hata olmazsa buraya çalışır

finally: #bu her zaman çalışır
    print("Program bitti")

###NOT raise ValueError("") ile kendi istisnamızı oluşturabiliriz bu şekilde