FROM python:3.12

RUN groupadd -r py && useradd -r -g py py
RUN pip install --upgrade pip
RUN pip install Flask==3.0.3 requests==2.31.0 redis==5.0.3
WORKDIR /app
COPY app /app
COPY cmd.sh /cmd.sh

EXPOSE 9090
USER py

