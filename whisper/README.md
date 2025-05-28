# Настройка окружения для генерации SRT файла

В данном примере мы разбираем способ создания файла субтитров в формате SRT из любого видео. 

Для этого используем whisper от OpenAI. 

## Достоинства подхода:

- полностью локальная обработка, Ваши данные никуда не отправляются;
- полностью бесплатно, Вам не нужно искать и оплачивать какие-то специальные сервисы. 

## Установка

⚠️ __*Python должен быть установлен предварительно*__

✅ Создаем виртуальное окружение 

```
python3 -m venv venv
```

✅ Активируем виртуальное окружение

__Mac и Ubuntu / Debian__
```
source venv/bin/activate
```
Windows:

__cmd__
```
venv\Scripts\activate
```
__PowerShell__
```
venv\Scripts\Activate.ps1
```

✅ Устанавливаем модуль whisper
```
pip install -U openai-whisper
```
✅ Устанавливаем библиотеку ffmpeg 
__Mac__ 
```
brew install ffmpeg
```
__Ubuntu / Debian__
```
sudo apt update
sudo apt install ffmpeg
```

__Windows (Chocolatey)__
```
choco install ffmpeg
```
__Windows (Scoop)__
```
scoop install ffmpeg
```

✅ Запускаем скрипт для генерации субтитров 
```
python generate_srt.py  video.mp4 > result.srt
```

## Место хранения скачанных моделей

__На Mac__

```
.cache/whisper
или
~/Library/Caches/whisper

```

__На Linux__

```
~/.cache/whisper
```

__На Windows__
```
%LOCALAPPDATA%\whisper 
обычно C:\Users\<пользователь>\AppData\Local\whisper
```

Путь можно изменить с помощью переменной окружения:

```
export XDG_CACHE_HOME=/your/custom/path
```

Если переменная окружения определена, то модели будут находиться здесь

```
$XDG_CACHE_HOME/whisper
```