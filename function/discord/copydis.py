mytitle = "MAKEBY:IKGA SO DARK MARKET"
from os import system
from pickle import REDUCE
from pypresence import Presence
import discord
import asyncio
from colorama import Fore, init, Style
import platform
import requests
from time import sleep
import discord, os, json
from json import load
from discord.ext import commands
import socket
import random
import threading
from httpx import patch
from time import sleep
from colorama import Fore
from pystyle import Colors, Colorate
import discord

os.system(f'cls & mode 80,20 & title  COPYSERVERIKGA SO')

re = Style.RESET_ALL
r = Fore.RED
g = Fore.GREEN
y = Fore.YELLOW
b = Fore.BLUE
m = Fore.MAGENTA
c = Fore.CYAN
lmg = Fore.CYAN

if (__name__ == '__main__'):
    system('')

intents = discord.Intents.all()  # สร้างวัตถุ Intents ใหม่ด้วยการตั้งค่าเริ่มต้น
client = discord.Client(intents=intents)  # ส่งพารามิเตอร์ intents เมื่อสร้างอินสแตนซ์ Client

os = platform.system()
if os == "Windows":
    system("cls")
else:
    system("clear")
    print(chr(27) + "[2J")
print(f"""{lmg}
          
┏━━━┓┏━━━┓┏━━━┓┏┓━━┏┓┏━━━┓┏━━━┓┏━━━┓┏┓━━┏┓┏━━━┓┏━━━┓
┃┏━┓┃┃┏━┓┃┃┏━┓┃┃┗┓┏┛┃┃┏━┓┃┃┏━━┛┃┏━┓┃┃┗┓┏┛┃┃┏━━┛┃┏━┓┃
┃┃━┗┛┃┃━┃┃┃┗━┛┃┗┓┗┛┏┛┃┗━━┓┃┗━━┓┃┗━┛┃┗┓┃┃┏┛┃┗━━┓┃┗━┛┃
┃┃━┏┓┃┃━┃┃┃┏━━┛━┗┓┏┛━┗━━┓┃┃┏━━┛┃┏┓┏┛━┃┗┛┃━┃┏━━┛┃┏┓┏┛
┃┗━┛┃┃┗━┛┃┃┃━━━━━┃┃━━┃┗━┛┃┃┗━━┓┃┃┃┗┓━┗┓┏┛━┃┗━━┓┃┃┃┗┓
┗━━━┛┗━━━┛┗┛━━━━━┗┛━━┗━━━┛┗━━━┛┗┛┗━┛━━┗┛━━┗━━━┛┗┛┗━┛
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

                [+] BY: The Bass Shop                                                          
                                                                                              
        """)
token = input(f'{y}กรุณาใส่ TOKEN ของคุณ: ')
print()
guild_s = input(f'{b}กรุณาใส่ GUILD ID ของผู้คนในเซิร์ฟเวอร์: \n > ')
print()
guild = input(f'{r}กรุณาใส่ GUILD ID ของเซิร์ฟเวอร์คุณ: \n > ')
input_guild_id = guild_s  # <-- ใส่ GUILD ID ของเซิร์ฟเวอร์ผู้คน
output_guild_id = guild  # <-- ใส่ GUILD ID ของเซิร์ฟเวอร์คุณ
token = token  # <-- TOKEN ของบัญชีคุณ
print(re)

print("  ")
print("  ")

@client.event
async def on_ready():
    extrem_map = {}
    print(f"{c}ล็อกอินสำเร็จเป็น : {client.user}")
    print(f"{c}กำลังคัดลอกเซิร์ฟเวอร์")
    guild_from = client.get_guild(int(input_guild_id))
    guild_to = client.get_guild(int(output_guild_id))
    await Clone.guild_edit(guild_to, guild_from)
    await Clone.roles_delete(guild_to)
    await Clone.channels_delete(guild_to)
    await Clone.roles_create(guild_to, guild_from)
    await Clone.categories_create(guild_to, guild_from)
    await Clone.channels_create(guild_to, guild_from)

    await asyncio.sleep(0)
    client.close()

def print_add(message):
    print(f'{g}[*]{re} {message}')

def print_delete(message):
    print(f'{r}[*]{re} {message}')

def print_warning(message):
    print(f'{r}[WARNING]{re} {message}')

def print_error(message):
    print(f'{r}[ERROR]{re} {message}')

class Clone:
    @staticmethod
    async def roles_delete(guild_to: discord.Guild):
            for role in guild_to.roles:
                try:
                    if role.name != f"{y}@everyone" :
                        await role.delete()
                        print_delete(f"{y}ลบ Role : {role.name}")
                except discord.Forbidden:
                    print_error(f"{y}เกิดข้อผิดพลาดในการลบ Role : {role.name}")
                except discord.HTTPException:
                    print_error(f"{y}ไม่สามารถลบ Role : {role.name}{re}")

    @staticmethod
    async def roles_create(guild_to: discord.Guild, guild_from: discord.Guild):
        roles = []
        role: discord.Role
        for role in guild_from.roles:
            if role.name != f"{y}@everyone" :
                roles.append(role)
        roles = roles[::-1]
        for role in roles:
            try:
                await guild_to.create_role(
                    name=role.name,
                    permissions=role.permissions,
                    colour=role.colour,
                    hoist=role.hoist,
                    mentionable=role.mentionable
                )
                print_add(f"{y}สร้าง Role {role.name}")
            except discord.Forbidden:
                print_error(f"{y}เกิดข้อผิดพลาดในการสร้าง Role : {role.name}")
            except discord.HTTPException:
                print_error(f"{y}ไม่สามารถสร้าง Role : {role.name}{re}")

    @staticmethod
    async def channels_delete(guild_to: discord.Guild):
        for channel in guild_to.channels:
            try:
                await channel.delete()
                print_delete(f"{y}ลบ Channel : {channel.name}")
            except discord.Forbidden:
                print_error(f"{y}เกิดข้อผิดพลาดในการลบ Channel: {channel.name}")
            except discord.HTTPException:
                print_error(f"{y}ไม่สามารถลบ Channel : {channel.name}{re}")

    @staticmethod
    async def categories_create(guild_to: discord.Guild, guild_from: discord.Guild):
        channels = guild_from.categories
        channel: discord.CategoryChannel
        new_channel: discord.CategoryChannel
        for channel in channels:
            try:
                overwrites_to = {}
                for key, value in channel.overwrites.items():
                    role = discord.utils.get(guild_to.roles, name=key.name)
                    overwrites_to[role] = value
                new_channel = await guild_to.create_category(
                    name=channel.name,
                    overwrites=overwrites_to)
                await new_channel.edit(position=channel.position)
                print_add(f"{y}สร้าง Category : {channel.name}")
            except discord.Forbidden:
                print_error(f"{y}เกิดข้อผิดพลาดในการลบ Category : {channel.name}")
            except discord.HTTPException:
                print_error(f"{y}ไม่สามารถลบ Category : {channel.name}{re}")

    @staticmethod
    async def channels_create(guild_to: discord.Guild, guild_from: discord.Guild):
        channel_text: discord.TextChannel
        channel_voice: discord.VoiceChannel
        category = None
        for channel_text in guild_from.text_channels:
            try:
                for category in guild_to.categories:
                    try:
                        if category.name == channel_text.category.name:
                            break
                    except AttributeError:
                        print_warning(f"{y}Channel {channel_text.name} ไม่มีหมวดหมู่!{re}")
                        category = None
                        break

                overwrites_to = {}
                for key, value in channel_text.overwrites.items():
                    role = discord.utils.get(guild_to.roles, name=key.name)
                    overwrites_to[role] = value
                try:
                    new_channel = await guild_to.create_text_channel(
                        name=channel_text.name,
                        overwrites=overwrites_to,
                        position=channel_text.position,
                        topic=channel_text.topic,
                        slowmode_delay=channel_text.slowmode_delay,
                        nsfw=channel_text.nsfw)
                except:
                    new_channel = await guild_to.create_text_channel(
                        name=channel_text.name,
                        overwrites=overwrites_to,
                        position=channel_text.position)
                if category is not None:
                    await new_channel.edit(category=category)
                print_add(f"{y}สร้าง Text Channel: {channel_text.name}")
            except discord.Forbidden:
                print_error(f"{y}เกิดข้อผิดพลาดในการสร้าง Text Channel: {channel_text.name}")
            except discord.HTTPException:
                print_error(f"{y}ไม่สามารถสร้าง Text Channel: {channel_text.name}{re}")

        for channel_voice in guild_from.voice_channels:
            try:
                for category in guild_to.categories:
                    try:
                        if category.name == channel_voice.category.name:
                            break
                    except AttributeError:
                        print_warning(f"{y}Channel {channel_voice.name} ไม่มีหมวดหมู่!{re}")
                        category = None
                        break

                overwrites_to = {}
                for key, value in channel_voice.overwrites.items():
                    role = discord.utils.get(guild_to.roles, name=key.name)
                    overwrites_to[role] = value
                try:
                    new_channel = await guild_to.create_voice_channel(
                        name=channel_voice.name,
                        overwrites=overwrites_to,
                        position=channel_voice.position,
                        bitrate=channel_voice.bitrate,
                        user_limit=channel_voice.user_limit)
                except:
                    new_channel = await guild_to.create_voice_channel(
                        name=channel_voice.name,
                        overwrites=overwrites_to,
                        position=channel_voice.position)
                if category is not None:
                    await new_channel.edit(category=category)
                print_add(f"{y}สร้าง Voice Channel: {channel_voice.name}")
            except discord.Forbidden:
                print_error(f"{y}เกิดข้อผิดพลาดในการสร้าง Voice Channel: {channel_voice.name}")
            except discord.HTTPException:
                print_error(f"{y}ไม่สามารถสร้าง Voice Channel: {channel_voice.name}{re}")

    @staticmethod
    async def guild_edit(guild_to: discord.Guild, guild_from: discord.Guild):
        try:
            await guild_to.edit(name=guild_from.name, icon=guild_from.icon)
            print_add(f"{y}เปลี่ยนชื่อและไอคอนของเซิร์ฟเวอร์เป็น: {guild_from.name}")
        except discord.Forbidden:
            print_error(f"{y}ไม่สามารถเปลี่ยนชื่อหรือไอคอนของเซิร์ฟเวอร์ได้")
        except discord.HTTPException:
            print_error(f"{y}ไม่สามารถเปลี่ยนชื่อหรือไอคอนของเซิร์ฟเวอร์ได้")

client.run(token)