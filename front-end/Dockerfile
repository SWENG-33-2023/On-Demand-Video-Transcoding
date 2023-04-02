FROM node:19

# Workdir
WORKDIR /src

# Copy to directory of src
COPY . .

# Install app dependencies
RUN npm ci --omit=dev

EXPOSE 3000
CMD [ "node", "App.js" ]
