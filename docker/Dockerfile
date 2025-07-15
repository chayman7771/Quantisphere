FROM python:3.11-slim
WORKDIR /app

COPY . /app

RUN pip install --no-cache-dir -r requirements.txt

CMD ["python", "app/main.py"]

CMD ["streamlit", "run", "src/sandbox_app.py", "--server.port=8080", "--server.address=0.0.0.0"]
