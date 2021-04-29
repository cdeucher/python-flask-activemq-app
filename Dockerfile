# docker build -t activemq-cli:0.1 . 
# docker run -itd --name activemq-cli -p 8080:8080 -p 8181:8181 -v $(pwd):/usr/src/app activemq-cli:dev


FROM python:3

RUN mkdir -p /usr/src/app
RUN apt update -y

#RUN apt -y install nodejs npm
#RUN npm install npm@latest -g
#RUN npm install -g @vue/cli@4.5.11

WORKDIR /usr/src/app
COPY . /usr/src/app
RUN python setup.py install

CMD [ "python", "run.py" ]

#CMD ["sh", "-c", "tail -f /dev/null"]
#CMD [ "bash", "/start.sh" ]
# vue create client
# cd client
# npm run serve --port 8181