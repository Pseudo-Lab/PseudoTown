FROM node:20.9.0

WORKDIR /app

COPY . /app

RUN npm install
RUN npm run build

CMD ["node", "build"]