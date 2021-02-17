# QR Bot

[Telegram bot](https://t.me/qrencodebot) to generate and send QR codes into your chat.

## Usage

Use `/start` or `/help` option to display available commands.

## Self-hosting

+ Clone this repo.
```
$ git clone https://github.com/samedamci/qrencodebot && cd qrencodebot
```
+ Install required modules.
```
$ pip3 install --user -r requirements.txt
```
+ Create `environment` file with your bot token and instance URL.
```
TOKEN=your_token_here
```
+ Start bot with `python3 main.py`.

### With Docker

+ Build image itself.
```
# docker build -t samedamci/qrencodebot .
```
+ Run bot in container.
```
# docker run --rm -d -e TOKEN='your_token_here' --name qrencodebot samedamci/qrencodebot
```
