FROM python:3.9-alpine

LABEL maintainer="samedamci@disroot.org"

ENV TOKEN TOKEN
ENV CACHING_CHAT_ID CACHING_CHAT_ID
RUN apk add --no-cache gcc musl-dev linux-headers libc-dev libffi-dev libressl-dev && \
    apk update py3-pip openssl && \
    pip3 install cryptography==3.1.1 python-telegram-bot python-dotenv qrcode && \
    mkdir /opt/bot && \
    apk del gcc musl-dev linux-headers libc-dev libressl-dev

COPY . /opt/bot/

RUN cd /opt/bot && \
    rm -rf README.md LICENSE requirements.txt .git*

CMD cd /opt/bot/ && python3 main.py
