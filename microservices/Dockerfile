FROM python:3-alpine3.11

MAINTAINER Projeto TCE-UNITINS

COPY conf /conf

WORKDIR /app

RUN pip install -r ../conf/requirments.txt

EXPOSE 80

#CMD ["python", "app.py"]

#docker build -t microservice .
#docker run -it --name service -p 5000:5000 --volume ~/git/tce-infra/microservices/app:/app  microservice /bin/sh
