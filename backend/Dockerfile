FROM python:3.10.12-slim
WORKDIR /opt/app
COPY requirements.txt . 
# COPY . .
RUN pip install -r requirements.txt

EXPOSE 8000

CMD ["python", "main.py"]