FROM node:20-alpine as builder
WORKDIR /opt/app
COPY *.json ./
RUN npm install
COPY . .
CMD ["sh", "-c", "\
if [ \"$APP_MODE\" = 'development' ]; then \
npm run dev; \
else npm run build && npm run start; fi"]

EXPOSE 3000
