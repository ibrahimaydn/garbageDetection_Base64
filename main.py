import firebase_admin
from firebase_admin import credentials, db
from ultralytics import YOLO
import cv2
import base64
import time
from datetime import datetime
import uuid


cred = credentials.Certificate("myapplication.json")
firebase_admin.initialize_app(cred, {
    'databaseURL': 'https://myapplication.com/'
})

# Model
model = YOLO("yeniyolov8tespit.pt")

# USB kamera
cap = cv2.VideoCapture(0)

if not cap.isOpened():
    print("Kamera açılamadı.")
    exit()

print("Çöp tespiti başlatıldı...")

try:
    while True:
        ret, frame = cap.read()
        if not ret:
            print("Kare alınamadı.")
            break


        results = model.predict(frame, conf=0.5)

        # tespit varsa
        if results and results[0].boxes:

            _, buffer = cv2.imencode('.jpg', frame)
            img_base64 = base64.b64encode(buffer).decode('utf-8')


            data = {
                "timestamp": datetime.now().isoformat(),
                "image": img_base64,
                "id": str(uuid.uuid4())
            }

            db.reference("cop_tespitleri").push(data)
            print("Tespit edilen görüntü Firebase'e gönderildi.")

        time.sleep(5)

except KeyboardInterrupt:
    print("Durduruldu.")

finally:
    cap.release()
    cv2.destroyAllWindows()
