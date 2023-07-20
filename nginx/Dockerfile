FROM nginx:latest
COPY ./havanavard.top.pem  /etc/ssl/certs/
COPY ./havanavard.top.key /etc/ssl/private/
COPY ./default.conf /etc/nginx/conf.d/
RUN chmod 777  /etc/ssl/
