import os
import speech_recognition as sr
from pydub import AudioSegment

INPUT_DIR = "mp3"
OUTPUT_DIR = "wav"

# Создаём папку для WAV, если её нет
os.makedirs(OUTPUT_DIR, exist_ok=True)

# Обрабатываем все файлы в INPUT_DIR
for filename in os.listdir(INPUT_DIR):
    if filename.endswith(".mp3"):
        name = os.path.splitext(filename)[0]  # Без расширения
        mp3_path = os.path.join(INPUT_DIR, filename)
        wav_path = os.path.join(OUTPUT_DIR, name + ".wav")

        # Конвертация MP3 → WAV
        audio = AudioSegment.from_file(mp3_path, format="mp3")
        audio = audio.set_channels(1).set_frame_rate(16000)
        audio.export(wav_path, format="wav")
        print(f"🎵 {filename} → {wav_path}")

        # Распознавание речи
        recognizer = sr.Recognizer()
        with sr.AudioFile(wav_path) as source:
            audio_data = recognizer.record(source)

        try:
            text = recognizer.recognize_google(audio_data, language="ru-RU")
            print(f"📝 Распознанный текст: {text}\n")
        except sr.UnknownValueError:
            print("❌ Голос не распознан!")
        except sr.RequestError:
            print("❌ Ошибка запроса к Google API!")

print("🎉 Обработка всех файлов завершена!")
