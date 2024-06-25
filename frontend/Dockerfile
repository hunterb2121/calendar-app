# syntax=docker/dockerfile:1

FROM node:22.3-alpine3.20

WORKDIR /app

COPY package.json /app/

RUN npm install

COPY . /app/

EXPOSE 5173

CMD ["npm", "run", "dev"]