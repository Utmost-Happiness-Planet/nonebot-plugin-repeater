from nonebot import get_driver, on_message, logger
from nonebot.adapters.cqhttp import Bot, GroupMessageEvent, MessageSegment
from nonebot.typing import T_State

repeater_group = get_driver().config.repeater_group
shortest = get_driver().config.repeater_minlen

m = on_message(priority=10, block=False)

last_message = {}
has_repeated = {}


def messageType(message: str):
    if message[0] == "[":
        data = message.split(",")
        return data[0][1:]
    else:
        return "Normal"


@m.handle()
async def repeater(bot: Bot, event: GroupMessageEvent, state: T_State):
    global last_message, has_repeated
    gid = str(event.group_id)
    if gid in repeater_group:
        logger.debug(last_message)
        mt = messageType(str(event.message))
        if mt == "Normal" and event.message == last_message.get(gid) and len(str(event.message)) >= shortest:
            data = event.message
        elif mt == "CQ:face" and event.message == last_message.get(gid):
            data = event.message
        elif mt == "CQ:image" and str(event.message).split(",")[1] == last_message.get(gid):
            data = MessageSegment.image(str(event.message).split(",")[3][4:-1])
        else:
            data = None

        if mt == "CQ:image":
            last_message[gid] = str(event.message).split(",")[1]
        else:
            last_message[gid] = event.message

        # logger.debug(data)
        if not has_repeated.get(gid) and data is not None:
            has_repeated[gid] = True
            await bot.send(event, data)
        else:
            has_repeated[gid] = False
