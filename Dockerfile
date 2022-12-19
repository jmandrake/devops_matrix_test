FROM python:3.8.13-slim-buster

RUN mkdir -p /app
COPY . app.py /app/
WORKDIR /app
RUN apt-get update && apt-get install -y git
RUN pip install -r requirements.txt
EXPOSE 8080
CMD [ "app.py" ]
ENTRYPOINT [ "python" ]