⚠由于本人懒惰，PyPi不会及时更新（万恶的2FA验证），请于此仓库获取插件最新版本。

---

<div align="center">

  # Repeater
  ✨ 基于[NoneBot](https://github.com/nonebot/nonebot2)的插件，群聊复读机 ✨
  </br>
  ✨ auto +1 ✨
</div>

## 功能介绍

当群里开始+1时，机器人也会参与其中。

包括普通消息，QQ表情，还有图片（表情包）。

## 用法简介

三个全局配置：

```python
repeater_group = ["<群号1>", "<群号2>"]  # 支持复读的群号，群号设置为 all 可以默认所有群聊开启
repeater_min_message_length = 1  # 触发复读的文本消息最小长度（表情和图片无此限制）
repeater_min_message_times = 2  # 触发复读的消息次数
```

按常规方法导入插件即可。

## 已知BUG

发送形如 `<三个汉字><图片>` 消息时会风控，原因未知。

<a href="https://github.com/Utmost-Happiness-Planet/uhpstatus/blob/main/LICENSE">
    <img src="https://img.shields.io/badge/license-GPL%20v3.0-orange" alt="license">
  </a>
  
  <a href="https://github.com/nonebot/nonebot2">
    <img src="https://img.shields.io/badge/nonebot-v2-red" alt="nonebot">
  </a> 
  
  <a href="">
    <img src="https://img.shields.io/badge/release-v3.0-blueviolet" alt="release">
</a>
