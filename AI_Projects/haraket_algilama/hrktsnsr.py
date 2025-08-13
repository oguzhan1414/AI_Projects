import cv2
import time
import pyautogui
import webbrowser

def send_whatsapp_message():
    phone_number = "05434402842"
    timestamp = time.strftime("%d %H:%M")  # güncel tarih ve saat

    message = f"Hareket tespit edildi Tarih/Saat : {timestamp}"
    web_url = f"https://web.whatsapp.com/send?phone={phone_number}&text={message}"

    try:
        print(f"[INFO] Whatsapp üzerinden mesaj gönderiliyor: {message}")
        webbrowser.open(web_url)
        time.sleep(20)  # WhatsApp Web açılması için bekle
        pyautogui.press("enter")  # mesajı gönder
        time.sleep(5)
        pyautogui.hotkey("ctrl", "w")  # tarayıcı sekmesini kapat
        time.sleep(2)
        print(f"[INFO] Whatsapp üzerinden mesaj gönderildi")
        return True

    except Exception as e:
        print(f"[ERROR] Whatsapp üzerinden mesaj gönderilirken hata oluştu:", e)
        return False

def main():
    pyautogui.PAUSE = 1.5
    cap = cv2.VideoCapture(0)  # kamera ID'si 0

    if not cap.isOpened():
        print("ERROR Kamera açılmadı")
        return

    # MOG2 algoritması ile hareket algılama
    backSub = cv2.createBackgroundSubtractorMOG2(
        history=500,
        varThreshold=25,
        detectShadows=True
    )

    last_motion_time = 0
    bekleme = 10  # mesaj arası bekleme süresi (sn)

    while True:
        ret, frame = cap.read()
        if not ret:
            print("[Error] Kamera görüntüsü alınamadı")
            break

        fgMask = backSub.apply(frame)
        _, thresh = cv2.threshold(fgMask, 250, 255, cv2.THRESH_BINARY)
        thresh = cv2.erode(thresh, None, iterations=2)
        thresh = cv2.dilate(thresh, None, iterations=2)

        contours, _ = cv2.findContours(thresh, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
        motion_detected = False

        for contour in contours:
            if cv2.contourArea(contour) < 1500:  # küçük hareketleri yok say
                continue
            motion_detected = True
            break

        current_time = time.time()

        if motion_detected and (current_time - last_motion_time > bekleme):
            print("[INFO] Hareket algılandı")
            if send_whatsapp_message():
                last_motion_time = current_time
                cv2.putText(frame, "Hareket algılandı", (10, 30),
                            cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 0, 255), 2)
            else:
                print("WARNING: Whatsapp mesajı gönderilemedi")
                time.sleep(5)
        else:
            cv2.putText(frame, "Hareket algılanmadı", (10, 30),
                        cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 0), 2)

        # canlı görüntü ve hareket maskesi
        cv2.imshow("Kamera", frame)
        cv2.imshow("Hareket Maskesi", thresh)

        # çıkış için q tuşu
        if cv2.waitKey(1) & 0xFF == ord("q"):
            break

    # kaynakları serbest bırak
    cap.release()
    cv2.destroyAllWindows()

if __name__ == "__main__":
    main()
