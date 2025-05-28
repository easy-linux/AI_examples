import whisper
import sys
import os

# Получаем имя файла из аргументов или stdin
if len(sys.argv) > 1:
    file_path = sys.argv[1]
else:
    file_path = input("Введите путь к видео/аудио-файлу: ").strip()

# Проверка существования файла
if not os.path.exists(file_path):
    print(f"Файл не найден: {file_path}")
    sys.exit(1)

# Загружаем модель
model = whisper.load_model("small")

# Распознаём речь
result = model.transcribe(file_path, verbose=False)

# Функция преобразования времени в формат SRT
def format_srt_time(seconds: float) -> str:
    h = int(seconds // 3600)
    m = int((seconds % 3600) // 60)
    s = int(seconds % 60)
    ms = int((seconds - int(seconds)) * 1000)
    return f"{h:02}:{m:02}:{s:02},{ms:03}"

# Вывод SRT в stdout
for i, segment in enumerate(result["segments"], start=1):
    start_time = format_srt_time(segment["start"])
    end_time = format_srt_time(segment["end"])
    text = segment["text"].strip()

    print(f"{i}")
    print(f"{start_time} --> {end_time}")
    print(f"{text}\n")
