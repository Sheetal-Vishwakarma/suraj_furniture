#FROM python:3.11.4-slim-bullseye AS BASE
FROM python:3.11.9 AS BASE

ENV PYTHONUNBUFFERED 1
ENV PYTHONDONTWRITEBYTECODE 1

WORKDIR /app

COPY requirements.txt /app/
RUN pip install -r requirements.txt
RUN pip install python-dotenv==0.19.1

RUN apt-get update && \
    apt-get install -y \
    gcc \
    default-libmysqlclient-dev \
    pkg-config \
    curl && \
    pip install --no-cache-dir -r requirements.txt && \
    apt-get remove -y \
    gcc \
    pkg-config && \
    rm -rf /var/lib/apt/lists/*

# Install cron and other utilities
RUN apt-get update && \
    apt-get install -y cron nano

COPY /app .

EXPOSE 8000

RUN apt update
RUN apt install weasyprint -y
RUN apt install python3-pip libpango-1.0-0 libpangoft2-1.0-0 -y
RUN apt install python3-pip libpango-1.0-0 libpangoft2-1.0-0 libjpeg-dev libopenjp2-7-dev libffi-dev -y

# COPY ./app/hrms-cron /etc/cron.d/hrms-cron

# RUN chmod 644 /etc/cron.d/hrms-cron && \
#     touch /var/log/cron.log && \
#     chmod 644 /var/log/cron.log && \
#     crontab /etc/cron.d/hrms-cron && \
#     service cron start

#CMD [" sh -c" "python3 manage.py migrate --noinput && python3 manage.py collectstatic --noinput && python manage.py runserver 0.0.0.0:8000" , "/usr/sbin/cron start"]

# Copy entrypoint script
COPY docker/django/docker-entrypoint.sh /app/docker-entrypoint.sh
RUN chmod +x /app/docker-entrypoint.sh

# Use the entrypoint script to start cron and Django
ENTRYPOINT ["/app/docker-entrypoint.sh"]