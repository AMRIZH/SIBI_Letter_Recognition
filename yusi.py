import cv2
from ultralytics import YOLO


def detect_realtime():
    # Muat model yang telah dilatih
    # Sesuaikan path model
    model = YOLO(
        r'C:\Amri\MY_LAB\yolo\repo\runs\classify\train\weights\best.pt')

    # Buka kamera
    cap = cv2.VideoCapture(0)

    while True:
        ret, frame = cap.read()
        if not ret:
            print("Gagal membuka kamera!")
            break

        # Deteksi objek dalam frame
        results = model(frame)

        # Gambar bounding box pada frame
        annotated_frame = results[0].plot()

        # Tampilkan hasil
        cv2.imshow('Sign Language Translator', annotated_frame)

        # Tekan 'q' untuk keluar
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    cap.release()
    cv2.destroyAllWindows()


if __name__ == "__main__":
    detect_realtime()
