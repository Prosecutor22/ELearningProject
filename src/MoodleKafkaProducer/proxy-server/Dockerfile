FROM python:3
COPY . /app
WORKDIR /app

RUN pip install -r requirements.txt

CMD [ "python", "server.py", "1234" ]

EXPOSE 1234