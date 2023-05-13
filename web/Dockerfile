FROM python:3.10.9

SHELL ["/bin/bash", "-c"]

# set environment variables
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

RUN pip install --upgrade pip

RUN apt update && apt -qy install gcc libjpeg-dev libxslt-dev \
    libpq-dev libmariadb-dev libmariadb-dev-compat gettext cron openssh-client flake8 locales vim


RUN useradd -rms /bin/bash app && chmod 777 /opt /run


WORKDIR /app

COPY --chown=app:app requirements.txt .
COPY --chown=app:app ./app .

RUN pip3 install -r requirements.txt

RUN mkdir -p /app/static && mkdir -p /app/media
RUN chmod -R 755 /app && chown -R app:app /app

USER app