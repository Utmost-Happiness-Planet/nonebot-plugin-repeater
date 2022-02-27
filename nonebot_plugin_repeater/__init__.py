from nonebot import get_driver, on_message, logger
from nonebot.adapters.onebot.v11 import Bot, GroupMessageEvent, MessageSegment
from nonebot.typing import T_State
from nonebot.params import State
import re
config = get_driver().config.dict()
repeater_group = config.get('repeater_group',[])
shortest = config.get('repeater_minlen',[])

m = on_message(priority=10, block=False)

last_message = {}
has_repeated = {}


# 消息类型判别 - 分类普通文本消息、QQ表情、图片
def messageType(message: str):
    if message[0] == "[":
        data = message.split(",")
        return data[0][1:]
    else:
        return "Normal"


# 获取图片消息的url与hash
def getPicMeta(message: str):
    return re.findall("url=(.*?)[,|\]]", message)[0], re.findall("file=(.*?)[,|\]]", message)[0]


@m.handle()
async def repeater(bot: Bot, event: GroupMessageEvent, state: T_State = State()):
    global last_message, has_repeated
    gid = str(event.group_id)
    if gid in repeater_group:
        logger.debug(event.message)
        mt = messageType(str(event.message))
        logger.debug(mt)

        # 对不同类别的消息处理方式不同，图片是最麻烦的
        data = None
        if mt == "Normal":
            if event.message == last_message.get(gid) and len(str(event.message)) >= shortest:
                data = event.message
            else:
                has_repeated[gid] = False
            last_message[gid] = event.message
        elif mt == "CQ:face":
            if event.message == last_message.get(gid):
                data = event.message
            else:
                has_repeated[gid] = False
            last_message[gid] = event.message
        elif mt == "CQ:image":
            meta = getPicMeta(str(event.message))  # 图片消息元数据
            if meta[1] == last_message.get(gid):
                data = MessageSegment.image(meta[0])
            else:
                has_repeated[gid] = False
            last_message[gid] = meta[1]
        else:
            last_message[gid] = None

        logger.debug(str(data))
        # 如果这条消息已经复读过了就不参与复读了
        if not has_repeated.get(gid) and data is not None:
            has_repeated[gid] = True
            await bot.send(event, data)
