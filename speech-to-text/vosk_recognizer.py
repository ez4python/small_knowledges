import os
import wave
import json
import subprocess
from vosk import Model, KaldiRecognizer

# Определяем абсолютные пути к директориям
BASE_DIR = os.path.abspath(os.path.dirname(__file__))
MP3_INPUT_DIR = os.path.join(BASE_DIR, "mp3")
WAV_OUTPUT_DIR = os.path.join(BASE_DIR, "wav")
TXT_OUTPUT_DIR = os.path.join(BASE_DIR, "txt")
MODEL_PATH = os.path.join(BASE_DIR, "small_model")

# Проверяем наличие модели
if not os.path.exists(MODEL_PATH):
    raise FileNotFoundError(f"❌ Ошибка: Модель не найдена в '{MODEL_PATH}'")

# Загружаем Vosk-модель
model = Model(MODEL_PATH)

# Создаём папки, если они отсутствуют
os.makedirs(MP3_INPUT_DIR, exist_ok=True)
os.makedirs(WAV_OUTPUT_DIR, exist_ok=True)
os.makedirs(TXT_OUTPUT_DIR, exist_ok=True)


def convert_mp3_to_wav(mp3_path, wav_path):
    """Конвертация MP3 в WAV с выводом в реальном времени."""
    command = ["ffmpeg", "-i", mp3_path, "-ar", "16000", "-ac", "1", "-c:a", "pcm_s16le", wav_path]

    process = subprocess.Popen(command, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)

    for line in process.stderr:
        print("FFmpeg:", line.strip())

    process.wait()

    if process.returncode != 0:
        print(f"❌ FFmpeg завершился с ошибкой при обработке {mp3_path}")
        return False
    return os.path.exists(wav_path)


# Обрабатываем файлы
for filename in os.listdir(MP3_INPUT_DIR):
    mp3_path = os.path.join(MP3_INPUT_DIR, filename)

    if filename.endswith(".mp3"):  # Конвертация MP3 в WAV
        wav_filename = filename.replace(".mp3", ".wav")
        wav_path = os.path.join(WAV_OUTPUT_DIR, wav_filename)

        # if not convert_mp3_to_wav(mp3_path, wav_path):
        #     print(f"❌ Ошибка конвертации {filename}")
        #     continue

    if filename.endswith(".wav"):  # Распознавание речи из WAV
        wav_path = os.path.join(WAV_OUTPUT_DIR, filename)
        print(f"🔄 Обрабатываю: {wav_path}")

        try:
            print(f"🔄 Открываю файл: {wav_path}")
            with wave.open(wav_path, "rb") as wf:
                print(f"✅ Файл {wav_path} успешно открыт!")
                if wf.getnchannels() != 1:
                    raise ValueError(f"❌ {filename} имеет больше 1 канала! Нужно моно-аудио.")

                recognizer = KaldiRecognizer(model, wf.getframerate())
                text = ""

                while True:
                    data = wf.readframes(4000)
                    if not data:
                        break
                    if recognizer.AcceptWaveform(data):
                        result = json.loads(recognizer.Result())
                        text += result.get("text", "") + " "

                text = text.strip()
                print(f"📌 Распознанный текст для {filename}: {text}")

                if not text:
                    print(f"⚠️ Внимание! Файл {filename} не содержит распознаваемого текста.")
                    continue

                # Сохранение результата в файл
                txt_output_path = os.path.join(TXT_OUTPUT_DIR, filename.replace(".wav", ".txt"))
                with open(txt_output_path, "w", encoding="utf-8") as f:
                    f.write(text)

                print(f"✅ Готово! Текст сохранён в: {txt_output_path}")

        except Exception as e:
            print(f"❌ Ошибка при обработке {filename}: {e}")

print("🎉 Обработка всех файлов завершена!")
