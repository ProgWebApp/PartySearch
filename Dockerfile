FROM nginx:1.20-alpine

# Copy sources files
COPY ./src /usr/share/nginx/html

# Production launch command
CMD ["nginx", "-g", "daemon off;"]
