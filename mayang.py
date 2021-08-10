import discord
import datetime
import random
import asyncio
import os
intents = discord.Intents.all()
client = discord.Client(intents=intents)

@client.event
async def on_ready():
    print('봇 온라인')
    print(client.user.name)
    print(client.user.id)
    print('====================================')
    game = discord.Game('[크아앙 마냥이가 울부짖었다]')
    await client.change_presence(status=discord.Status.online, activity=game)

@client.event
async def on_message(message):

    y = datetime.datetime.now().year
    m = datetime.datetime.now().month
    d = datetime.datetime.now().day
    h = datetime.datetime.now().hour
    min = datetime.datetime.now().minute
    sec = datetime.datetime.now().second
    bot_logs = '874482354687733760'
    embed = discord.Embed(title='메시지 로그', colour=discord.Colour.red())
    embed.add_field(name='유저', value=f'<@{message.author.id}>({message.author})')
    embed.add_field(name='채널', value=f'<#{message.channel.id}>')
    embed.add_field(name='내용', value=message.content, inline=False)
    embed.add_field(name='날짜', value=f"{y}-{m}-{d} {h}:{min}:{sec}", inline=False)
    embed.add_field(name='참고', value=f"마냥이로 삭제한 글들은 안떠요!", inline=False)
    embed.set_footer(text=f"유저 ID:{message.author.id} • 메시지 ID: {message.id}")
    await client.get_channel(int(bot_logs)).send(embed=embed)

    if message.content == '마냥아 내정보':
        user = message.author
        date = datetime.datetime.utcfromtimestamp(((int(user.id) >> 22) + 1420070400000) / 1000)
        await message.channel.send(f"{message.author.mention}의 가입일 : {date.year}/{date.month}/{date.day}")
        await message.channel.send(f"{message.author.mention}의 이름 / 이름 아이디 / 서버 닉네임 : {user.name} / {user.id} / {user.display_name}")

    if message.content.startswith('!청소'):
        try:
            # 메시지 관리 권한 있을시 사용가능
            if message.author.guild_permissions.manage_messages:
                amount = message.content[4:]
                await message.delete()
                await message.channel.purge(limit=int(amount))
                message = await message.channel.send(embed=discord.Embed(title='메시지 ' + str(amount) + '개 삭제되었어요!', colour=discord.Colour.green()))
                await asyncio.sleep(2)
            else:
                await message.channel.send('``명령어 사용권한이 없습니다.``')
        except:
            pass

    if message.content.startswith("!추방"):
        member = message.guild.get_member(int(message.content.split(" ")[1]))
        await message.guild.kick(member, reason=' '.join(message.content.split(" ")[2:]))

    if message.content.startswith("!차단"):
        member = message.guild.get_member(int(message.content.split(" ")[1]))
        await message.guild.ban(member, reason=' '.join(message.content.split(" ")[2:]))

@client.event
async def on_message_edit(before, after):
    if before.author.bot:
        return
    else:
        y = datetime.datetime.now().year
        m = datetime.datetime.now().month
        d = datetime.datetime.now().day
        h = datetime.datetime.now().hour
        min = datetime.datetime.now().minute
        bot_logs = '874482392847511572'
        embed = discord.Embed(title='메시지 수정됨', colour=discord.Colour.red())
        embed.add_field(name='유저', value=f'<@{before.author.id}>({before.author})', inline=False)
        embed.set_footer(text=f"유저 ID:{before.author.id} • 메시지 ID: {before.id}")
        embed.add_field(name='수정 전', value=before.content + "\u200b", inline=True)
        embed.add_field(name='수정 후', value=after.content + "\u200b", inline=True)
        embed.add_field(name='날짜', value=f"{y}-{m}-{d} {h}:{min}", inline=False)
        await client.get_channel(int(bot_logs)).send(embed=embed)

@client.event
async def on_message_delete(message):
    y = datetime.datetime.now().year
    m = datetime.datetime.now().month
    d = datetime.datetime.now().day
    h = datetime.datetime.now().hour
    min = datetime.datetime.now().minute
    bot_logs = '874482432982810624'
    embed = discord.Embed(title='메시지 삭제됨', colour=discord.Colour.orange())
    embed.add_field(name='유저', value=f'<@{message.author.id}>({message.author})')
    embed.add_field(name='채널', value=f'<#{message.channel.id}>')
    embed.add_field(name='내용', value=message.content, inline=False)
    embed.add_field(name='날짜', value=f"{y}-{m}-{d} {h}:{min}", inline=False)
    embed.set_footer(text=f"유저 ID:{message.author.id} • 메시지 ID: {message.id}")
    await client.get_channel(int(bot_logs)).send(embed=embed)

access_token = os.environ["BOT_TOKEN"]
client.run(access_token)
