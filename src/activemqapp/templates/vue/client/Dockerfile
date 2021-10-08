# docker build -t cli:0.1 . 
# docker run --rm -v $(pwd):/usr/src/app cli:0.1 run build


FROM node:latest

RUN mkdir -p /usr/src/app
RUN apt update -y

RUN npm install -g @vue/cli@4.5.11

WORKDIR /usr/src/app
COPY . /usr/src/app

ENTRYPOINT ["npm"]
