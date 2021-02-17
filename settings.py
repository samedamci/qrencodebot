#!/usr/bin/env python3

import os
from os.path import join, dirname
from dotenv import load_dotenv

dotenv_path = join(dirname(__file__), "environment")
load_dotenv(dotenv_path)

TOKEN = os.getenv("TOKEN")
CACHING_CHAT_ID = os.getenv("CACHING_CHAT_ID")

PLACEHOLDER_QR = "https://i.imgur.com/mEy0Bsl.png"
SOURCE_URL = "https://github.com/samedamci/qrencodebot"
