FROM python:3.12-rc-slim-bullseye

# Копирование requirements.txt в контейнер
COPY ./requirements.txt /app/requirements.txt

# Установка зависимостей
RUN pip install --no-cache-dir -r /app/requirements.txt

# Определение рабочей директории
WORKDIR /app

COPY . /app

EXPOSE 8000

# Ваш код и прочие инструкции Dockerfile
CMD ["uvicorn", "src.main:app", "--host", "0.0.0.0", "--port", "8000"]