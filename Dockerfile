FROM ubuntu

RUN apt-get update -y && \
    apt-get install -y python3 python3-pip

COPY ./requirements.txt /app/requirements.txt

WORKDIR /app

RUN pip3 install -r requirements.txt

COPY . /app

ENV FLASK_ENV development

ENTRYPOINT ["python3"]
CMD ["app.py"]