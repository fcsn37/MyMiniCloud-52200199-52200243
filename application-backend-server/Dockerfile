FROM python:3.11-alpine
WORKDIR /app
COPY app.py .
COPY requirements.txt .  
RUN pip install --no-cache-dir -r requirements.txt 
COPY students.json . 
EXPOSE 8081
CMD ["python","app.py"]