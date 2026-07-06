🚗 RC Car

Proyek RC Car berbasis ESP32 dengan kontrol menggunakan Python dan fitur FPV (First Person View) menggunakan ESP32-CAM melalui RTSP.

📂 Struktur Project
main.py

Program utama untuk mengontrol mobil remote, meliputi:

🚗 Gas
🛑 Rem
⚙️ Kopling
↔️ Steering
🎮 Pembacaan input dari steering wheel / joystick
axisandbutton.py

Digunakan untuk mengecek nomor axis dan button pada joystick atau steering wheel sebelum dipetakan ke main.py.

📷 Menjalankan RTSP pada ESP32-CAM
1. Buka Project RTSP

Masuk ke folder:

ESP32-RTSP-master/src/src.ino

Lalu buka file src.ino menggunakan Arduino IDE.

2. Install Library OneButton

Download library:

https://github.com/mathertel/OneButton

Kemudian di Arduino IDE pilih:

Sketch → Include Library → Add .ZIP Library...

Pilih file ZIP yang telah diunduh.

3. Install Library Micro-RTSP

Download library Micro-RTSP dari repository GitHub yang digunakan pada project ini, kemudian install dengan cara yang sama:

Sketch → Include Library → Add .ZIP Library...
4. Konfigurasi WiFi

Ubah SSID dan password pada source code:

const char* ssid = "YOUR_WIFI";
const char* password = "YOUR_PASSWORD";
5. Upload Program
Pilih board AI Thinker ESP32-CAM
Pilih COM Port yang sesuai
Klik Upload
6. Jalankan Stream

Setelah ESP32-CAM terhubung ke WiFi, buka alamat RTSP menggunakan VLC atau aplikasi lain yang mendukung RTSP.

Contoh:

rtsp://IP_ESP32_CAM:8554/mjpeg/1
