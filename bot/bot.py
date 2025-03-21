#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# (c) @SpEcHIDe

from pyrogram import Client, enums, __version__

from . import API_HASH, APP_ID, LOGGER, BOT_TOKEN 

from .user import User

class Bot(Client):
    USER: User = None
    USER_ID: int = None

    def __init__(self):
        super().__init__(
            "bot",
            api_hash="085e9a7ff52085f8f38c8ccef42e09b7",
            api_id="22546702",
            plugins={
                "root": "bot/plugins"
            },
            workers=200,
            bot_token="7279964689:AAFZf8U5-OGPBKAnVOCXl1JSTstEGTWkdxg",
            sleep_threshold=10
        )
        self.LOGGER = LOGGER

    async def start(self):
        await super().start()
        bot_details = await self.get_me()
        self.set_parse_mode(enums.ParseMode.HTML)
        self.LOGGER(__name__).info(
            f"@{bot_details.username}  started! "
        )
        self.USER, self.USER_ID = await User().start()

    async def stop(self, *args):
        await super().stop()
        self.LOGGER(__name__).info("Bot stopped. Bye.")
