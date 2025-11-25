# Gerekli kütüphaneleri içe aktarıyoruz.
# datetime: Tarih ve saat işlemleri için.
# timedelta: İki tarih/saat arasındaki farkı temsil etmek için.
# time: Programı belirli bir süre bekletmek gibi zamanla ilgili işlevler için.
from datetime import datetime, timedelta
import time

# -- İlk Örnekler (datetime modülünün temel kullanımı) --

# O anki tarih ve saati alıp değişkene atar.
current_time = datetime.now()
print("Current Date and Time: ", current_time)

# Belirli bir tarih ve saati manuel olarak oluşturur.
# Yıl, ay, gün, saat, dakika, saniye şeklinde parametre alır.
event_date = datetime(2025, 12, 25, 9, 0, 0)
print(event_date)

# O anki tarih ve saati tekrar alır.
current_time2 = datetime.now()
# strftime metodu ile tarihi istediğimiz formatta (Yıl-Ay-Gün Saat:Dakika:Saniye) bir metne dönüştürür.
formatted_time = current_time2.strftime("%Y-%m-%d %H:%M:%S")
print(formatted_time)

# Gelecekteki belirli bir tarihi (sadece gün olarak) tanımlar.
ozel_gun = datetime(2025, 12, 25)
# Şimdiki tarihi alır.
current_Date = datetime.now()
# İki tarih arasındaki farkı hesaplar. Sonuç bir timedelta nesnesidir.
time_diff = ozel_gun - current_Date
# Kalan süreyi ekrana yazdırır (gün, saat, dakika, saniye olarak).
print(time_diff)


###### ETKİNLİK GERİ SAYIM SAYACI #################

# Fonksiyon 1: Kullanıcıdan etkinlik tarihini ve saatini alır.
def get_event_datetime():
    # try-except bloğu, kullanıcının hatalı formatta giriş yapma olasılığına karşı programın çökmesini engeller.
    try:
        # Kullanıcıdan belirtilen formatta tarih ve saat girmesini ister.
        date_input = input("Enter the event date (YYYY-MM-DD HH:MM:SS): ")
        # Girilen metni (string) strptime ile bir datetime nesnesine dönüştürür.
        return datetime.strptime(date_input, "%Y-%m-%d %H:%M:%S")

    # Kullanıcı yanlış formatta bir tarih girerse bu blok çalışır.
    except ValueError:
        print("Invalid date format. Please use YYYY-MM-DD HH:MM:SS")
        # Hatalı giriş durumunda None (boş değer) döndürür.
        return None


# Fonksiyon 2: Hedef tarih ile şimdiki zaman arasındaki farkı hesaplar.
def calculate_time(event_Date):
    # O anki tarih ve saati alır.
    current_datetime = datetime.now()
    # Hedef tarih ile şimdiki tarih arasındaki farkı hesaplayıp döndürür.
    time_difference = event_Date - current_datetime
    return time_difference


# Fonksiyon 3: Kalan süreyi ekrana formatlı bir şekilde yazdırır.
def display_countdown(time_left):
    # timedelta nesnesinden toplam gün sayısını alır.
    days = time_left.days
    # divmod fonksiyonu, toplam saniyeyi 3600'e (bir saatteki saniye sayısı) böler.
    # Bölümü (saat) ve kalanı (saniye) ayrı değişkenlere atar.
    hours, remainder = divmod(time_left.seconds, 3600)
    # Bir önceki adımdan kalan saniyeyi 60'a bölerek dakika ve saniyeyi bulur.
    minutes, seconds = divmod(remainder, 60)
    # f-string kullanarak kalan süreyi düzenli bir şekilde ekrana yazdırır.
    # end="\r" parametresi, bir sonraki yazdırma işleminde satır başı yapmak yerine aynı satırın üzerine yazılmasını sağlar.
    # Bu, geri sayımın tek bir satırda güncelleniyormuş gibi görünmesini sağlar.
    print(f"Time Remaining: {days} days, {hours} hours, {minutes} minutes, {seconds} seconds", end="\r")


# Fonksiyon 4: Geri sayım döngüsünü başlatır.
def start_countdown(event_date):
    # while True ile sonsuz bir döngü başlatılır. Döngü içerideki 'break' komutuyla kırılacaktır.
    while True:
        # Her döngü adımında kalan süreyi yeniden hesaplar.
        time_left = calculate_time(event_date)
        # Eğer kalan saniye 0 veya daha az ise, yani zaman dolmuşsa...
        if time_left.total_seconds() <= 0:
            print("\nCountdown Complete!")  # Geri sayımın bittiğini belirten bir mesaj yazdırır.
            break  # Döngüyü sonlandırır.

        # Kalan süreyi ekranda gösterir.
        display_countdown(time_left)
        # Programı 1 saniye bekletir. Bu sayede her saniye güncelleme yapılır.
        time.sleep(1)


# --- Ana Program Akışı ---

# İlk olarak kullanıcıdan etkinlik tarihini almak için fonksiyonu çağırırız.
event_datetime = get_event_datetime()
# Eğer kullanıcı geçerli bir tarih girdiyse (fonksiyon None döndürmediyse)...
if event_datetime:
    # Geri sayımın hangi tarih için ayarlandığını kullanıcıya bildirir.
    print(f"Countdown set for: {event_datetime}")
    # Geri sayım döngüsünü başlatır.
    start_countdown(event_datetime)