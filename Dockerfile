FROM python:3.11

WORKDIR /app

RUN apt-get update && apt-get install -y nodejs npm
RUN npm install webtorrent-cli -g

COPY . .

RUN pip install -r requirements.txt

EXPOSE 8000
CMD ["python", "app.py"]
