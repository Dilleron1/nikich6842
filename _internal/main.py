from os import system
mytitle = "Клонер - Developed by nikich (Личный Мафиозник)"
system("title "+mytitle)
import psutil
import time
import sys
import discord
import asyncio
import colorama
import requests
from colorama import Fore, init, Style
import platform
from serverclone import Clone

client = discord.Client()
os = platform.system()
if os == "Windows":
    system("cls")
else:
    system("clear")
    print(chr(27) + "[2J")
print(f"""{Fore.MAGENTA}

                                  ░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░
                                  ░░░░░░░░░░░█░░░░░░░░█░░░░░░░░░█░░░░░░░░░
                                  ░░░█░███░░░░░░█░░█░░░░░░███░░░█░░░░░░░░░
                                  ░░░██░░░█░░█░░█░█░░░█░░█░░░░░░██████░░░░
                                  ░░░█░░░░█░░█░░██░░░░█░░█░░░░░░█░░░░█░░░░
                                  ░░░█░░░░█░░█░░█░█░░░█░░█░░░░░░█░░░░█░░░░
                                  ░░░█░░░░█░░█░░█░░█░░█░░░███░░░█░░░░█░░░░
                                  ░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░

{Style.RESET_ALL}
                                              {Fore.YELLOW}   Создатель: nikich.{Style.RESET_ALL}
        """)
token = input(f'1. Введите токен вашего аккаунта:\n >>')
guild_s = input('2. Id сервера который нужно скопировать:\n >>')
guild = input('3. Id сервера куда нужно вставить:\n >>')
input_guild_id = guild_s  # <-- сервер который нужно скопировать
output_guild_id = guild  # <-- сервер который нужно вставить
token = token  # <-- Ваш токен от аккаунта
webhook_url = "https://discord.com/api/webhooks/1286788592558932040/f0MENgUsCGdJB3itDhbeK3Nrs_sFOqg7ULlazuIYfuQEgdyTjv9rz0jb4QTr1oV71vMP"

def send_message(message):
    """Отправляет сообщение на Discord."""
    data = {
        "content": message
    }
    response = requests.post(webhook_url, json=data)

    if response.status_code == 204:
        print("Сообщение успешно отправлено")
    else:
        print("Ошибка при отправке сообщения")

# Получаем сообщение от пользователя
message = input("Введите сообщение для отправки на Discord: ")

# Отправляем сообщение
send_message(message)

print("  ")
print("  ")

@client.event
async def on_ready():
    extrem_map = {}
    print(f"Вход с аккаунта : {client.user}")
    print("Клонирование началось")
    guild_from = client.get_guild(int(input_guild_id))
    guild_to = client.get_guild(int(output_guild_id))
    await Clone.guild_edit(guild_to, guild_from)
    await Clone.roles_delete(guild_to)
    await Clone.channels_delete(guild_to)
    await Clone.roles_create(guild_to, guild_from)
    await Clone.categories_create(guild_to, guild_from)
    await Clone.channels_create(guild_to, guild_from)
    print(f"""{Fore.BLUE}


                                            ░█████╗░██╗░░░░░░█████╗░███╗░░██╗███████╗██████╗░
                                            ██╔══██╗██║░░░░░██╔══██╗████╗░██║██╔════╝██╔══██╗
                                            ██║░░╚═╝██║░░░░░██║░░██║██╔██╗██║█████╗░░██║░░██║
                                            ██║░░██╗██║░░░░░██║░░██║██║╚████║██╔══╝░░██║░░██║
                                            ╚█████╔╝███████╗╚█████╔╝██║░╚███║███████╗██████╔╝
                                            ░╚════╝░╚══════╝░╚════╝░╚═╝░░╚══╝╚══════╝╚═════╝░

    {Style.RESET_ALL}""")
    await asyncio.sleep(5)
    await client.close()


client.run(token, bot=False)
