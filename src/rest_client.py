from typing import Final
from gateway_contracts import MessageEvent

import aiohttp

DISCORD_API_GATEWAY: Final = "https://discord.com/api/v10/"

_token: str


def init_rest_client(token: str):
    global _token
    _token = token


def is_command(content: str) -> bool:
    return content.startswith("!")


async def handle_command(session: aiohttp.ClientSession, msg: MessageEvent):
    if msg.content == "zjeb":
        await send_message(session, msg.channel_id, "<@!269132306227265536>")
    else:
        await send_message(session, msg.channel_id, "invalid command")


async def send_message(session: aiohttp.ClientSession, channel: str, messsage: str):
    response = await session.post(
        f"{DISCORD_API_GATEWAY}/channels/{channel}/messages",
        headers={
            "Authorization": f"Bot {_token}",
            "User-Agent": "DiscordBot (crabot, 0.0.1)",
        },
        data={"content": messsage},
    )

    response.raise_for_status()
