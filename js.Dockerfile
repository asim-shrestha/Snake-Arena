FROM node:14-buster

# Install dependencies
COPY ./client/package.json .
COPY ./client/package-lock.json ./
RUN npm install

# Bundle app source
COPY ./client ./

ARG PORT

CMD ["npm", "start"]
