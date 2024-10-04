#FROM nginx:1.21-alpine
FROM nginx:1.25.3-alpine

# Removing existing conf file for nginx and copy new conf file
RUN rm /etc/nginx/conf.d/default.conf

#COPY default.conf /etc/nginx/conf.d
COPY ./docker/nginx/default.conf /etc/nginx/conf.d

