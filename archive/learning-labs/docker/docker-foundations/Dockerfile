FROM python:3.12-slim

WORKDIR /app

COPY app.py .

ENV PORT=8000
ENV APP_MESSAGE="Hello from Docker!"

EXPOSE 8000

CMD ["python", "-u", "app.py"]