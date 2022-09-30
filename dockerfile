FROM python:3.9.7-slim-buster
RUN apt update && apt upgrade -y
RUN apt install git curl python3-pip ffmpeg -y
RUN pip3 install -U pip
RUN curl -sL https://deb.nodesource.com/setup_16.x | bash -
RUN apt-get install -y nodejs
RUN npm install -g npm@7.22.0
RUN mkdir /app/
COPY . /app/
WORKDIR /app/
RUN pip3 install -U -r requirements.txt
CMD python3 main.py
Footer
© 2022 GitHub, Inc.
Footer navigation
Terms
Privacy
Security
