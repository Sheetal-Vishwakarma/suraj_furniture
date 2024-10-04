FROM phpmyadmin:5.2.1

LABEL version="1.0"
LABEL description="PhpMyadmin setup dockerfile"

RUN a2dissite 000-default.conf

RUN apt-get update && apt-get install vim htop cron net-tools -y

COPY ./docker/phpmyadmin/default-ssl.conf /etc/apache2/sites-enabled/default-ssl.conf

RUN a2enmod ssl

EXPOSE 443

