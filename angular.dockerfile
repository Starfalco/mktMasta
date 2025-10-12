FROM node:alpine

WORKDIR /frontend

COPY frontend/package*.json ./

COPY frontend/ .

RUN npm install -g npm

RUN npm install -g @angular/cli

RUN npm install