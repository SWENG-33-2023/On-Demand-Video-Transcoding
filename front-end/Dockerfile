FROM node:19

# Workdir
WORKDIR /code/front-end

# Copy to directory of src
COPY . . 

# Install app dependencies
WORKDIR /code/front-end/src
RUN npm ci --omit=dev

EXPOSE 3000
CMD [ "node", "App.js" ]
