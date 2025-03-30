FROM python:3.10.12-slim
WORKDIR /opt/app
COPY . .
RUN pip install --no-cache-dir -r requirements.txt
RUN pip install uvicorn[standard]

EXPOSE 8000

CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000"]