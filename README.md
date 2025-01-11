# Voice-Recognition-Based-Smart-Home-Using-Convolutional-Neural-Network-and-Keyword-Spoting
File yang diperlukan untuk menggunakan sistem

langkah 1: Silahkan unduh file berikut:
"Runtime GPIO.py" pada repository diatas dan "kws_model_biasa.h5" pada link google drive berikut : https://drive.google.com/file/d/1PCkCHxGPPTfaExJHWNEzull6pPOHfCn_/view?usp=sharing 
Jika anda telah mengunduhnya, silahkan buat folder baru pada raspberry pi 5 anda untuk menyimpan file tersebut. Pastikan kedua file terletak pada folder yang sama dan tidak terpisah. Jika sudah program siap digunakan.

langkah 2: Buat virtual enviroment untuk program dan library yang dibutuhkan. Penting untuk diingat bahwa library yang dibutuhkan harus diinstall di dalam virtual environment dan program dijalankan di dalam virtual environment tersebut. pastikan dahulu bahwa anda telah menginstall pyhthon 3. 

Jalankan kode berikut pada terminal:
kode 1: python3 -m venv nama_env (nama_env bisa diganti dengan nama virtual environment yang anda mau) 
kode 2: source nama_env/bin/activate (untuk mengaktifkan virtual environment)

langkah 3: Install library yang dibutuhkan. Jalankan kode berikut:
kode 1: pip3 install sounddevice librosa numpy tensorflow noisereduce gpiozero

langkah 4: Wiring sistem sesuai dengan gambar pada file skematik.png
langkah 5: Pastikan directory file model kws sudah benar pada kode program sebelum menjalankannya
