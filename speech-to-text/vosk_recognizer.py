import os
import wave
import json
from vosk import Model, KaldiRecognizer

# Пути к папкам
INPUT_DIR = "mp3"  # Папка с аудиофайлами
OUTPUT_DIR = "wav"  # Папка для текстовых файлов
MODEL_PATH = "vosk-model-ru"  # Путь к модели[vosk-model-small-ru-0.22]

# Проверяем наличие модели
if not os.path.exists(MODEL_PATH):
    raise FileNotFoundError(f"❌ Ошибка: Модель не найдена в '{MODEL_PATH}'")

# Загружаем Vosk-модель
model = Model(MODEL_PATH)

# Создаём папку для вывода, если её нет
os.makedirs(OUTPUT_DIR, exist_ok=True)

# Обрабатываем все файлы в папке INPUT_DIR
for filename in os.listdir(INPUT_DIR):
    if filename.endswith(".wav"):  # Проверяем, что это аудиофайл
        filepath = os.path.join(INPUT_DIR, filename)
        print(f"🔄 Обрабатываю: {filepath}")

        try:
            # Открываем аудиофайл
            wf = wave.open(filepath, "rb")
            if wf.getnchannels() != 1:
                raise ValueError(f"❌ {filename} имеет больше 1 канала! Нужно моно-аудио.")

            recognizer = KaldiRecognizer(model, wf.getframerate())

            # Распознаём текст
            text = ""
            while True:
                data = wf.readframes(4000)
                if len(data) == 0:
                    break
                if recognizer.AcceptWaveform(data):
                    result = json.loads(recognizer.Result())
                    text += result.get("text", "") + " "

            # Если ничего не распознано – пропускаем
            if not text.strip():
                print(f"⚠️ Внимание! Файл {filename} не содержит распознаваемого текста.")
                continue

            # Записываем результат в файл
            output_filepath = os.path.join(OUTPUT_DIR, filename.eplace(".wav", ".txt"))
            with open(output_filepath, "w", encoding="utf-8") as f:
                f.write(text.strip())

            print(f"✅ Готово! Текст сохранён в: {output_filepath}")

        except Exception as e:
            print(f"❌ Ошибка при обработке {filename}: {e}")

print("🎉 Обработка всех файлов завершена!")
