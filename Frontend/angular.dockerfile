FROM node:alpine

WORKDIR /visual

COPY . /visual

RUN npm install -g npm

RUN npm install -g @angular/cli

RUN npm install