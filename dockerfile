# Use the official Node.js image.
FROM node:slim

# Set the working directory.
WORKDIR /application

# Copy package.json and package-lock.json.
COPY . /application

# Install dependencies.
RUN npm install

# Expose the application port.
EXPOSE 3000

# Command to run the application.
CMD node app.js
