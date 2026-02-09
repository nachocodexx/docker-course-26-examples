FROM python:3.9
COPY requirements.txt .
COPY src/ .
RUN pip install -r requirements.txt 
CMD ["python3", "app.py"]
