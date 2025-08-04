# ♻️ Raspberry Pi 5 ile Çöp Tespiti Sistemi

Bu proje, Raspberry Pi 5 üzerinde çalışan ve USB kamera kullanarak çevredeki çöp görüntülerini tespit eden bir görüntü işleme uygulamasıdır. Tespit edilen görseller Firebase Realtime Database'e base64 formatında gönderilir.

## 🚀 Özellikler

- YOLOv8 ile gerçek zamanlı çöp tespiti
- USB kamera ile görüntü alma
- Tespit edilen görsellerin Firebase'e base64 formatında yüklenmesi
- Raspberry Pi 5 ile tam uyumlu

## 🧰 Kullanılan Teknolojiler

- Python
- OpenCV
- Ultralytics YOLOv8
- Firebase Realtime Database
- Raspberry Pi 5

## 📸 Örnek Ekran

Firebase'e gönderilen veriler şu formatta görünür:
```json
{
  "timestamp": "2025-08-04T21:30:00",
  "image": "data:image/jpeg;base64,/9j/4AAQSkZJRgABAQAAAQABAAD...",
  "id": "f5b24e3f-9b6e-4d3b-bd4a-4c0ffddc1282"
}
