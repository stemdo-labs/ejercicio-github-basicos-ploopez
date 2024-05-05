# Use an existing base image
FROM alpine:latest

# Install any necessary dependencies
RUN apk update && apk add --no-cache bash

# Define a default command to run when the container starts
CMD ["echo", "Hello, world!"]
