FROM python:3.8

RUN apt-get update && apt-get upgrade -y
WORKDIR /home/app

COPY requirements.txt .
RUN pip install -r requirements.txt

COPY . .

EXPOSE 5050

CMD ["python3", "app.py"]