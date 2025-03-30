FROM node:20-alpine as builder
WORKDIR /opt/app
COPY *.json ./
RUN npm install
COPY . .
RUN npm run build
CMD ["npm", "run", "dev"]

EXPOSE 3000