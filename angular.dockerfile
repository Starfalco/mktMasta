# Pinned to SHA256 digest for production security to prevent tag mutation
FROM node@sha256:fb4cd12c85ee03686f6af5362a0b0d56d50c58a04632e6c0fb8363f609372293
WORKDIR /frontend

COPY frontend/package*.json ./

COPY frontend/ .

RUN npm install -g npm

RUN npm install -g @angular/cli

RUN npm install