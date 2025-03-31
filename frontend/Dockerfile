FROM node:20-alpine as builder
WORKDIR /opt/app
COPY *.json ./
RUN npm install
COPY . .
RUN npm run build
CMD ["sh", "-c", "\
if [ \"$APP_MODE\" = 'development' ]; then \
npm run dev; \
else npm run start; fi"]

EXPOSE 3000
