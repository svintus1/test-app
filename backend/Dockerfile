FROM python:3.10.12-slim
WORKDIR /opt/app
COPY . .
RUN pip install --no-cache-dir -r requirements.txt

EXPOSE 8000

CMD ["python", "main.py"]