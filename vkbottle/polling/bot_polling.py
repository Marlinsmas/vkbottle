from .abc import ABCPolling
from vkbottle.api import ABCAPI
from typing import Optional, AsyncIterator


class BotPolling(ABCPolling):
    """ Bot Polling class
    Documentation: https://github.com/timoniq/vkbottle/tree/v3.0/docs/polling/polling.md
    """

    def __init__(
        self,
        api: "ABCAPI",
        group_id: Optional[int] = None,
        wait: Optional[int] = None,
        rps_delay: Optional[int] = None,
    ):
        self.api = api
        self.group_id = group_id
        self.wait = wait or 25
        self.rps_delay = rps_delay or 0
        self.stop = False

    async def get_event(self, server: dict) -> dict:
        async with self.api.http as session:
            return await session.request_json(
                "POST",
                "{}?act=a_check&key={}&ts={}&wait={}&rps_delay={}".format(
                    server["server"], server["key"], server["ts"], self.wait, self.rps_delay,
                ),
            )

    async def get_server(self) -> dict:
        if self.group_id is None:
            self.group_id = (await self.api.request("groups.getById", {}))["response"][0]["id"]
        return (await self.api.request("groups.getLongPollServer", {"group_id": self.group_id}))[
            "response"
        ]

    async def listen(self) -> AsyncIterator[dict]:  # type: ignore
        server = await self.get_server()
        while not self.stop:
            event = await self.get_event(server)
            if not event.get("ts"):
                server = await self.get_server()
                continue
            server["ts"] = event["ts"]
            yield event
