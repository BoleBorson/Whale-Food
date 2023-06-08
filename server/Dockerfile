FROM python

WORKDIR /app

# set env variables
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

COPY requirements.txt ./requirements.txt
COPY chat.py .
COPY main.py .

RUN apt update
RUN apt install tesseract-ocr -y

RUN pip install -r requirements.txt
RUN pip install "uvicorn[standard]"
RUN ls -la
