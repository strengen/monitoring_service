FROM python:3.13-slim
WORKDIR /usr/app

COPY core/requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt
RUN mkdir -p /usr/app/data

COPY . . 
CMD ["python", "main.py"]