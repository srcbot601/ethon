# ignore this file

from telethon import Button


async def start_srb(event, st):
    await event.reply(
        st,
        buttons=[
            [
                Button.inline("SET THUMB.", data="set"),
                Button.inline("REM THUMB.", data="rem"),
            ],
            [
                Button.url(
                    "SOURCE-CODE",
                    url="https://github.com/AlphaMaxWolf/SaveRestrictedContentBot",
                )
            ],
        ],
    )


async def vc_menu(event):
    await event.edit(
        "**VIDEO CONVERTOR v1.4**",
        buttons=[
            [
                Button.inline("info.", data="info"),
                Button.inline("SOURCE", data="source"),
            ],
            [
                Button.inline("NOTICE.", data="notice"),
                Button.inline("Main.", data="help"),
            ],
            [Button.url("DEVELOPER", url="t.me/AlphaMaxWolf")],
        ],
    )
