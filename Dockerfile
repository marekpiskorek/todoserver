FROM python:latest
WORKDIR /app
COPY src ./

CMD ["python", "main.py"]
