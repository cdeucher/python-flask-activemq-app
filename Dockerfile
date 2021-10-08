# docker build -t activemq-cli:0.1 . 
# docker run -itd --name activemq-cli -p 8080:8080 -p 8181:8181 -v $(pwd):/usr/src/app activemq-cli:dev
FROM python:3

RUN mkdir -p /usr/src/app
RUN apt update -y

WORKDIR /usr/src/app
COPY . /usr/src/app
RUN python setup.py install

CMD [ "python", "run.py" ]
