import time
import sounddevice as sd
import librosa
import librosa.display
import numpy as np
import tensorflow as tf
import noisereduce as nr
import matplotlib.pyplot as plt

# Load model yang telah dilatih
model = tf.keras.models.load_model("D:\\College\\Skripsi\\Program\\kws_model_biasa.h5")

# Mapping label dari training
label_mapping = {
    0: 'Buka pintu', 
    1: 'Kunci pintu', 
    2: 'Lampu belakang mati',
    3: 'Lampu belakang nyala', 
    4: 'Lampu depan mati',
    5: 'Lampu depan nyala', 
    6: 'Matikan kipas', 
    7: 'Nyalakan kipas'
}

# Fungsi preprocessing audio
def preprocess_audio(signal, sr, target_sr=16000):
    try:
        # Resampling jika sampling rate tidak cocok
        if sr != target_sr:
            signal = librosa.resample(signal, orig_sr=sr, target_sr=target_sr)
        
        # Normalisasi
        signal = signal / np.max(np.abs(signal))
        
        # Noise reduction
        signal = nr.reduce_noise(y=signal, sr=target_sr)
        
        return signal
    except Exception as e:
        print(f"Error in preprocessing: {e}")
        return None

# Fungsi prediksi
def predict_command(audio, sr, threshold=0.7):
    try:
        # Preprocessing audio
        audio = preprocess_audio(audio, sr)
        if audio is None:
            return None

        # Ekstraksi MFCC
        mfccs = librosa.feature.mfcc(y=audio, sr=16000, n_mfcc=13)

        # Menentukan panjang target untuk padding
        required_length = 1131
        mfccs_padded = np.zeros((13, required_length))
        if mfccs.shape[1] < required_length:
            mfccs_padded[:, :mfccs.shape[1]] = mfccs
        else:
            mfccs_padded[:, :] = mfccs[:, :required_length]

        # Reshape untuk model
        features = mfccs_padded.T.reshape(1, required_length, 13)
        
        # Prediksi
        predictions = model.predict(features)
        max_confidence = np.max(predictions)
        predicted_label = np.argmax(predictions)

        # Threshold untuk confidence
        if max_confidence < threshold:
            return None
        return label_mapping[predicted_label]
    except Exception as e:
        print(f"Error in prediction: {e}")
        return None

# Runtime
def run_runtime():
    print("Sistem siap menangkap perintah...")
    while True:
        try:
            # Rekam audio selama 3 detik
            duration = 3
            fs = 16000
            print("\nSilakan berbicara...")
            audio = sd.rec(int(duration * fs), samplerate=fs, channels=1, dtype='float32')
            sd.wait()

            # Prediksi perintah
            command = predict_command(audio[:, 0], fs)
            if command is None:
                print("Perintah tidak dikenali, silahkan coba lagi.")
            else:
                print(f"Perintah terdeteksi: {command}")

            # Jeda 3 detik sebelum menerima perintah berikutnya
            print("Sistem akan siap menerima perintah berikutnya dalam 3 detik...")
            time.sleep(1.5)
        except KeyboardInterrupt:
            print("\nRuntime dihentikan oleh pengguna.")
            break
        except Exception as e:
            print(f"Unexpected error: {e}")
            print("Mengulangi proses...")
            continue

# Jalankan runtime
if __name__ == "__main__":
    run_runtime()
