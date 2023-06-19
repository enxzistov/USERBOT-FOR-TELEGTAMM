from time import sleep
from datetime import datetime, timedelta, date
from colorama import just_fix_windows_console
just_fix_windows_console()


from pyrogram.errors import FloodWait
from pyrogram import Client, filters, types
from pyrogram.types import Message
from pyrogram.types import ChatPermissions


from pyrogram import Client, filters
from pyrogram.errors import FloodWait
 
from pyrogram.types import ChatPermissions
 
import time
from time import sleep
import random

import arrow
import time


from io import StringIO


import wikipedia


from pyowm import OWM


import random


import requests


from aiogram.utils.markdown import hlink


from translate import Translator


import logging


import openai


from langdetect import detect, detect_langs


import sqlite3


import os
import sys
import configparser


import asyncio


l = None
d = N
print()
print('\033[31m' +                                      "█▀▀ █▄░█ ▀▄▀ ▀█ █ █▀ ▀█▀")
print("██▄ █░▀█ █░█ █▄ █ ▄█ ░█░")
print('\033[39m' + "добро пложаловать ваш Юзер бот уже активен! \n (P.S ниже будет ошибка при ошибке) \n") 

owm = OWM('4d9c68ba051733b61d30fa2406658670')
mgr = owm.weather_manager()





api_id = 123456 # Здесь в int
api_hash = "a12b3cdi6fg45hijklmnop"
app = Client('my_account', api_id=api_id, api_hash=api_hash)


utc = arrow.utcnow()
local = utc.to('UTC+2')


wikipedia.set_lang("ru")
translator = Translator(to_lang="ru")

Welcome = ["привет", "ку", "здаров", "даров", "хэллоу ", "привіт",
         "доброго Дня", "добрий день", "пр", "здраствуй",  "hello",  "hi", "хай",
         "прив", "приветик", "здраствуй", "Дароу", "здраствуйте", "дароу", "здрасте"]


helpid = ["какой ид чата?", "какой id чата?", "какой ид чата", "какой id чата",
          "какой айди чата?", "какой айди чата", "какой ид?", "какой ид", "айди этого чата", "айди чата"]

afk_info = {
    "start": datetime.now(),
    "is_afk": False,
    "reason": "",
}

is_afk = filters.create(lambda _, __, ___: afk_info["is_afk"])


@app.on_message(is_afk & ~filters.me & ((filters.private & ~filters.bot) | (filters.mentioned & filters.group)))
async def afk_handler(_, message: types.Message):
    end = datetime.now().replace(microsecond=0)
    afk_time = end - afk_info["start"]
    await message.reply_text(
        f"❕ Этот пользователь <b>AFK</b>.\n💬 Причина:</b> <i>{afk_info['reason']}</i>\n<b>⏳ Продолжительность:</b> {afk_time}"
    )


@app.on_message(filters.command("afk", prefixes=".") & filters.me)
async def afk(_, message):
    if len(message.text.split()) >= 2:
        reason = message.text.split(" ", maxsplit=1)[1]
    else:
        reason = "None"

    afk_info["start"] = datetime.now().replace(microsecond=0)
    afk_info["is_afk"] = True
    afk_info["reason"] = reason

    await message.edit(f"❕ This user <b>AFK</b>.\n<b>💬 Reason:</b> <i>{reason}</i>.")


@app.on_message(filters.command("unafk", prefixes=".") & filters.me)
async def unafk(_, message):
    if afk_info["is_afk"]:
        end = datetime.now().replace(microsecond=0)
        afk_time = end - afk_info["start"]
        await message.edit(f"<b>❕ I'm not <b>AFK</b> anymore.\n" f"⏳ I was <b>AFK:</b> {afk_time}")
        afk_info["is_afk"] = False
    else:
        await message.edit("<b>❌ You weren't afk</b>")


@app.on_message(filters.command('online', prefixes='/') & filters.me)
def online(_, msg):
    msg.edit("Ник было кастомизированно")
    while True:
        app.update_profile(first_name=f"Python | online Python chat: {app.get_chat_online_count(msg.chat.id)} | ")
        sleep(45)


@app.on_message(filters.command("date", prefixes='/') & filters.me)
def date(_, msg):
 msg.edit(f" ⚫️Успешно обновилось время в профиле")
 while True:
   Hour = int(datetime.now().strftime("%H")) 
   Minute = datetime.now().strftime("%M")
   app.update_profile(last_name=f"|time {Hour}:{Minute}|")
   sleep(30)


@app.on_message(filters.command("chat_info", prefixes='/'))
def chat_info(_, msg):
    chat_description = app.get_chat(msg.chat.id).description
    title = msg.chat.title
    id2 = msg.chat.id
    chat_online = app.get_chat_online_count(msg.chat.id)
    members_count = app.get_chat_members_count(msg.chat.id)
    groupinfo = (f"**Информация о чате:**\n"
        f" **Название** :  {title}\n"
        f" **Описание** {chat_description}\n\n"
        f" **Aйди:**  `{id2}`\n"
        f" **Текущий онлайн:** {chat_online}\n"
        f" **Всего участников** {members_count}")
    app.send_message(chat_id=msg.chat.id, text=groupinfo, reply_to_message_id=msg.id)


string = {
      "code": f"<b><emoji id=4985626654563894116>💻</emoji> Код:</b>\n",
      "success": f"<b><emoji id=5197688912457245639>✅</emoji> Результат</b>:\n",
      "error": f"<b><emoji id=5852812849780362931>❌</emoji> Ошибка</b>:\ns",
      }


@app.on_message(filters.command(["py", "eval", "e"], prefixes="/") & filters.me)
def user_exec(client, message):
    r = message.reply_to_message
    code = ""
    try:
        code = message.text.split(" ", maxsplit=1)[1]
    except IndexError:
        try:
            code = message.text.split(" \n", maxsplit=1)[1]
        except IndexError:
            pass

    result = sys.stdout = StringIO()
    try:
        exec(code)

        message.edit(
            f"{string['code']}"
            f"<code>{code}</code>\n\n"
            f"{string['success']}"
            f"<code>{result.getvalue()}</code>"
        )
    except:
        message.edit(
            f"{string['code']}"
            f"<code>{code}</code>\n\n"
            f"{string['error']}"
            f"<code>{sys.exc_info()[0]}: {sys.exc_info()[1]}</code>"
        )


@app.on_message(filters.command('check', prefixes='/') & filters.me)
def det_info(_, msg):
    user_id = msg.reply_to_message.from_user.id
    name = msg.reply_to_message.from_user.first_name
    last_name = msg.reply_to_message.from_user.last_name
    username = msg.reply_to_message.from_user.username

    if msg.reply_to_message.from_user.username is None:
         msg.edit(
            f"Name - {name} {last_name}\nID - {user_id}\n \n   f'🗓 Дата проверки: - {time.asctime()}\n' ")

    if last_name is None:
        msg.edit(
            f"💼 Ник- {name}\n🆔 ID: - {user_id}\nUsername - @{username} \n🗓 Дата проверки: - {time.asctime()}\n")

    else:
        msg.edit(f"💼 Ник: -  {name} {last_name}\n"
                 f"🆔 ID:  - <code>{user_id}</code>\n"
                 f"Username - @{username}\n"
                 f"🗓 Дата проверки: - {time.asctime()}\n"
                 )


@app.on_message(filters.command("mute", prefixes='!') & filters.me)
async def mute_py(client, msg):
    user_id = msg.reply_to_message.from_user.id
    chat_id = msg.chat.id
    list_values = msg.text.replace('!mute ', '').split()
    await app.restrict_chat_member(chat_id, user_id, ChatPermissions(),
    datetime.now() + timedelta(minutes=int(list_values[0])))
    await msg.reply_text(f"{msg.reply_to_message.from_user.mention()} Был замучен на {list_values[0]} минут, администратором {msg.from_user.mention()} \n**Причина: "
                         f"{list_values[1]}")


@app.on_message(filters.command("unmute", prefixes="!") & filters.me)
async def unmute(client, message):
   chat_id = message.chat.id
   user_id = message.reply_to_message.from_user.id
   await app.restrict_chat_member(chat_id, user_id, ChatPermissions(can_send_messages=True, can_send_media_messages=True, can_send_other_messages=True))
   await message.reply(f"{message.reply_to_message.from_user.mention()} был размучен администратором {message.from_user.mention()}")


@app.on_message(filters.command("kick", "!") & filters.me)
async def info(client, message):
    user_id = message.reply_to_message.from_user.id
    chat_id = message.reply_to_message.chat.id
    await client.ban_chat_member(chat_id, user_id)
    await client.unban_chat_member(chat_id, user_id)


@app.on_message(filters.command("love", prefixes='#'))
def date(_, msg):
    msg.edit("🤍🤍🤍🤍🤍🤍🤍🤍🤍🤍\n🤍🤍🤍❤️❤️    ❤️❤️🤍🤍🤍\n🤍🤍❤️❤️❤️❤️❤️❤️❤️🤍🤍🤍\n🤍🤍❤️❤️❤️❤️❤️❤️❤️🤍🤍🤍\n🤍🤍🤍❤️❤️❤️❤️❤️🤍🤍🤍\n"
             "🤍🤍🤍🤍❤️❤️❤️🤍🤍🤍🤍🤍\n🤍🤍🤍🤍🤍❤️🤍🤍🤍🤍🤍")
    sleep(1)
    msg.edit(
        "🖤🖤🖤🖤🖤🖤🖤🖤🖤🖤\n🖤🖤🖤❤️❤️    ❤️❤️🖤🖤🖤\n🖤🖤❤️❤️❤️❤️❤️❤️❤️🖤🖤🖤\n🖤🖤❤️❤️❤️❤️❤️❤️❤️🖤🖤🖤\n🖤🖤🖤❤️❤️❤️❤️❤️🖤🖤🖤\n"
        "🖤🖤🖤🖤❤️❤️❤️🖤🖤🖤🖤🖤\n🖤🖤🖤🖤🖤❤️🖤🖤🖤🖤🖤")
    sleep(0.25)
    msg.edit(
        "💙💙💙💙💙💙💙💙💙💙💙💙\n💙💙💙💛💛    💛💛💙💙💙💙\n💙💙💛💛💛💛💛💛💛💙💙💙\n💙💙💛💛💛💛💛💛💛💙💙💙\n💙💙💙💛💛💛💛💛💙💙💙💙\n"
        "💙💙💙💙💛💛💛💙💙💙💙💙\n💙💙💙💙💙💛💙💙💙💙💙💙")
    sleep(0.25)
    msg.edit("🤍🤍🤍🤍🤍🤍🤍🤍🤍🤍\n🤍🤍🤍❤️❤️    ❤️❤️🤍🤍🤍\n🤍🤍❤️❤️❤️❤️❤️❤️❤️🤍🤍🤍\n🤍🤍❤️❤️❤️❤️❤️❤️❤️🤍🤍🤍\n🤍🤍🤍❤️❤️❤️❤️❤️🤍🤍🤍\n"
             "🤍🤍🤍🤍❤️❤️❤️🤍🤍🤍🤍🤍\n🤍🤍🤍🤍🤍❤️🤍🤍🤍🤍🤍")
    sleep(0.25)
    msg.edit(
        "🖤🖤🖤🖤🖤🖤🖤🖤🖤🖤\n🖤🖤🖤❤️❤️    ❤️❤️🖤🖤🖤\n🖤🖤❤️❤️❤️❤️❤️❤️❤️🖤🖤🖤\n🖤🖤❤️❤️❤️❤️❤️❤️❤️🖤🖤🖤\n🖤🖤🖤❤️❤️❤️❤️❤️🖤🖤🖤\n"
        "🖤🖤🖤🖤❤️❤️❤️🖤🖤🖤🖤🖤\n🖤🖤🖤🖤🖤❤️🖤🖤🖤🖤🖤")
    sleep(0.25)
    msg.edit(
        "💙💙💙💙💙💙💙💙💙💙💙💙\n💙💙💙💛💛    💛💛💙💙💙💙\n💙💙💛💛💛💛💛💛💛💙💙💙\n💙💙💛💛💛💛💛💛💛💙💙💙\n💙💙💙💛💛💛💛💛💙💙💙💙\n"
        "💙💙💙💙💛💛💛💙💙💙💙💙\n💙💙💙💙💙💛💙💙💙💙💙💙")
    sleep(0.25)
    msg.edit("")


@app.on_message(filters.command("type", prefixes="#") & filters.me)
def type(_, msg):
    orig_text = msg.text.split("#type ", maxsplit=1)[1]
    text = orig_text
    tbp = ""  # to be printed
    typing_symbol = "▒"

    while (tbp != orig_text):
        try:
            msg.edit(tbp + typing_symbol)
            sleep(0.05)  # 50 ms

            tbp = tbp + text[0]
            text = text[1:]

            msg.edit(tbp)
            sleep(0.05)

        except FloodWait as e:
            sleep(e.x)


@app.on_message(filters.command("hack", prefixes="#") & filters.me)
def hack(_, msg):
    perc = 0
    
    while (perc < 100):
        try:
            text = "👮‍ Взлом телеграма ..." + str(perc) + "%"
            msg.edit(text)

            perc += random.randint(1, 3)
            sleep(0.1)

        except FloodWait as e:
            sleep(e.x)

    msg.edit("🟢 Телеграм успешно взломан!")
    sleep(3)

    msg.edit("🔎 Поиск секретных данных  ...")
    perc = 0

    while (perc < 100):
        try:
            text = "🔎 Поиск секретных данных ..." + str(perc) + "%"
            msg.edit(text)

            perc += random.randint(1, 5)
            sleep(0.15)

        except FloodWait as e:
            sleep(e.x)

    msg.edit("🔓 Найдены данные истории браузера все пользавателей телеграмм " )
    sleep(3)

    msg.edit("👮‍ Чтение ...")
    perc = 0

    while (perc < 100):
        try:
            text = "👮‍ Чтение ..." + str(perc) + "%"
            msg.edit(text)

            perc += random.randint(1, 3)
            sleep(0.45)

        except FloodWait as e:
            sleep(e.x)
    msg.edit("🚓 Данные будут вышлены на почту **__######################__**" )

@app.on_message(filters.command('help', prefixes='.'))
async def help_py(client, msg):
    await msg.reply_text('**Rich Userbot**\n**Команды бота**\n🟢/🔴  - __ Для всех/Для меня\n🎞 - Анимация \n🕰 - в процессе \n🎞 = 🔴 __ '
                             f"\n\n\n⚙️**Главное**\n `.help`__ - помощь🟢__  \n`.afk`__ (reason)- включить афк режим 🔴__ \n`.unafk`__ выйти с афк режима🔴__"
                             f"\n\n\n◽** Изменения ника **\n` /online` __ - добавить онлайн любой группы в ник🔴__\n`/date` __ -изменить время в нике🔴__"
                             f"\n\n\n👋** Ответы на сообщения **\nавтоматический ответ на приветствие🔴\nкакой id чата🟢"
                             f"\n\n\n🕵🏻** Получение информации **\n`/check` - __проверить информацию о человеке__🔴 \n `/chat_info` __ - проверить информацию о группе.🟢 __\n `/c`__ (1 число)(2 число)[действие (1 - +,2 - -,3 - *,4 - %)] - калькулятор🕰"
                             f"\n\n\n✏** Анимация **\n`#hack`__ - красивая анимация Взлома🎞 \n`#type` - __красивая анимация печати🎞__ \n`#love`__ - анимация сердца🎞"
                             f"\n\n\n◽**   Спам команды **\n `.spam`__[повтор циклов] [промежуток] [текст]__🔴"
                             f"\n\n\n📜** Гугл команды **\n__ `/w` __(город)- узнать погоду🟢__ \n`/wiki`__ (запрос) - загуглить что-то🟢__ \n`/translate`__ (текст) - переводчик🟢__ "
                             f"\n`/lang`__ (текст) - узнать язык текста🟢__\n`/py` __(код) - запустить код питона в тг🔴__"
                             f"\n\n\n👮🏻** Модерация **\n__ автоматическое приветствие новых людей (в чатах)🔴 \n`!mute` __(время в минутах)- замутить человека🔴 __"
                             f"\n__ `!unmute`__ - размутить человека🔴__ `!kick`__ - кикнуть человека🔴 \nавтоматический мут на 15 минут за мат🔴 __"
                             f"\n\n\n◽** Скопировать **\n `/copy`__ - скопировать профиль🔴 \n `/backmyname`__ - вернуть свое имя🔴"
                             f"\n\n\n🏆 __Developer __ \n @enxzisty"






                             , disable_web_page_preview=True)



@app.on_message(filters.command('translate', prefixes='/'))
def translate_py(_, msg):
    translate = msg.text.replace("/translate ", "")
    translation = translator.translate(translate)
    app.send_message(chat_id=msg.chat.id, text=(f"Перевод  '{translate}': \n{translation} "), reply_to_message_id=msg.id)


@app.on_message(filters.command('wiki', prefixes='/'))
def wiki_py(_, msg):
    wiki_r = msg.text.replace("/wiki ", "")
    app.send_message(chat_id=msg.chat.id, text=(f"Информация о {wiki_r}:\n{wikipedia.summary(wiki_r, 7)}"), reply_to_message_id=msg.id)


@app.on_message(filters.regex('/backmyname'))
async def copy_username(_, message: Message):
    await app.set_username(f'ImCoderAndILoveDonuts')
    await app.update_profile(
            first_name="🎅♡ꫀꪀ᥊ɀ𝓲𝘴𝓽 ᥴꪶꪮ᭙ꪀ♡ •",
            last_name="{}",
            bio=("🐉 Python: ♙Bot ♝UserBot| Дизайнер-Программист. Писать по делу."))


@app.on_message(filters.command('lang', prefixes="/"))
def weather(_, msg):
    lang = msg.text.split("/lang ", maxsplit=1)[1]
    if detect(lang) == "fi":
        app.send_message(chat_id=msg.chat.id, text="English", reply_to_message_id=msg.id)
    if detect(lang) == "mk":
        app.send_message(chat_id=msg.chat.id, text="Russia", reply_to_message_id=msg.id)
    else:         app.send_message(chat_id=msg.chat.id, text=detect(lang), reply_to_message_id=msg.id)


@app.on_message(filters.command('w', prefixes='/'))
def weather(_, msg):
    sity = msg.text.split("/w ", maxsplit=1)[1]

    observation = mgr.weather_at_place(sity)
    w = observation.weather
    ds = w.detailed_status
    wind = w.wind()
    vlaga = w.humidity
    temp = w.temperature('celsius')['temp']
    rain = w.rain
    clouds = w.clouds

    weather = f"""Weather in {sity}:
🌅 **Статус:** {str(ds)}\n
🍃 **Ветер:** {str(wind["speed"])}m/s, {str(wind["deg"])}°\n
💦 **Влажность:** {str(vlaga)}
🌡 **Температура:** {str(temp)} °C\n
🌦 **дождь:** {str(rain)}\n
☁ **Облака:** {str(clouds)}\n
🗓 **Дата проверки:** - {time.asctime()}"""
    app.send_message(chat_id=msg.chat.id, text=weather, reply_to_message_id=msg.id)


@app.on_message(filters.new_chat_members & ~filters.chat(-1001321822188))
async def welcome(client, msg):
    await msg.reply_text(f'Новый пользователь в группе, и зовут его: <a href="tg://user?id={msg.from_user.id}">{msg.from_user.first_name}</a>!')


@app.on_message(filters.regex('/copy')& filters.me)
async def copy_username(_, message: Message):
    try:
        await app.set_username(f'{message.reply_to_message.from_user.username}{random.randint(1, 100)}')
        await app.update_profile(
            first_name=message.reply_to_message.from_user.first_name,
            last_name=message.reply_to_message.from_user.last_name,
            bio=(await app.get_chat(message.reply_to_message.from_user.id)).bio
        )
    except Exception as ex:
        logging.warning(f'Ошибка изменения профиля!\n'
                        f'Детали: {ex}')
if __name__ == '__main__':
    logging.info('Запущен!')


mat = ["сука", "чмо", "даун", "конченый", "уеба", "уебан", "дебил"]





@app.on_message(filters.command("spam", prefixes=".") & filters.me)
def farm(_, message):
   try:
      
      
      p = int(message.text.split()[1])
      q = float(message.text.split()[2])
      text = ' '.join(message.text.split()[3:])
   
      message.edit("⏳ Спам начался")
      app.send_message(message.chat.id, text)
      for _ in range(p - 1):
         sleep(q)
         app.send_message(message.chat.id, text)
      message.edit("⌛️ Спам окончен")
   
   except:
      message.edit("❕ Были введены неверные аргументы для спама, пример ↓\n.spam [повтор циклов] [промежуток] [текст]")






















app.run()
