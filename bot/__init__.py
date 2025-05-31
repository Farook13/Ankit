#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# (c) @AlbertEinsteinTG

import os
import logging
import time
from logging.handlers import RotatingFileHandler
from .translation import Translation  # Make sure this module exists

# ✅ Environment variables with optional default values for local testing
import os

APP_ID = int(os.environ.get('API_ID', '123456'))
API_HASH = environ.get('API_HASH', '49aacd0bc2f8924add29fb02e20c8a16')
BOT_TOKEN = environ.get('BOT_TOKEN', '7693803634:AAFIWfW8gfzMYv-G5-I9hAnge1mYFVkspio')
DB_URI = os.environ.get('DB_URI', 'mongodb+srv://batman13:batman13@batman.sawvl.mongodb.net/?retryWrites=true&w=majority&appName=batman')
USER_SESSION = os.environ.get('USER_SESSION', '')  # Optional if not using userbot

# Dictionary placeholder (use as needed)
VERIFY = {}

# ✅ Logging configuration
logging.basicConfig(
    level=logging.INFO,
    format="[%(asctime)s - %(levelname)s] - %(name)s - %(message)s",
    datefmt='%d-%b-%y %H:%M:%S',
    handlers=[
        RotatingFileHandler(
            "autofilterbot.txt",  # Log file
            maxBytes=50_000_000,  # 50MB
            backupCount=10        # Rotate after 10 logs
        ),
        logging.StreamHandler()
    ]
)
logging.getLogger("pyrogram").setLevel(logging.WARNING)

# ✅ Track bot start time
start_uptime = time.time()

# ✅ Logger function
def LOGGER(name: str) -> logging.Logger:
    return logging.getLogger(name)
