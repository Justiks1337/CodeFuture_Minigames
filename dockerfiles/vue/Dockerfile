FROM node:lts-alpine as build-stage
COPY ./front/package*.json ./
RUN npm install
COPY ./front .
