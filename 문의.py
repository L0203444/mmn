import discord

client = discord.Client()


@client.event
async def on_ready():
    print("봇을 사용하여도 좋습니다")
    await client.change_presence(status=discord.Status.online,activity=discord.Activity(type=discord.ActivityType.playing, name="💖모든문의는 문의봇💖"))


@client.event
async def on_message(message):
    if message.content == "팁":
        await message.channel.send("**문의내용 밑에 보시면 !답변 유저아이디 [내용]을 복사해서 답변내용을 적고 바로 보내실 수 있습니다**") 
    if message.content == "세팅방법":
        await message.channel.send("**기본세팅은 일반유저들이 문의받을 채널은 보이게 및 메세지읽기 가능으로 하시고 메세지 기록은 못보게 하시면 됩니다 설정하시면 됩니다**")
    if message.content == "제작자연결": 
        await message.channel.send("https://discord.gg/7uKVrCMqJk")
    if message.content == ("도움"):
        await message.channel.send("**도움이 필요할땐 [제작자연결]을 채팅에 치시고 디스코드 서버에 가입하셔서 ㄱㅅㄱ#0001 찾아주세요**")
    if message.content == "설명": 
        await message.channel.send("**[팁], [세팅방법], [제작자연결], [도움]을 채팅에 치시면 유용한 정보를 얻으실 수 있습니다.**")

    if message.guild is None:
        if message.author.bot:
            return
        else:
            embed = discord.Embed(color=0xfffdfd)
            embed.add_field(name='전송자', value=message.author, inline=False)
            embed.add_field(name='문의내용', value=message.content, inline=False)
            embed.set_footer(text=f'!답변 <@{message.author.id}> [답변내용] 을 통해 답변을 해주세요')
            await client.get_channel(807972003109273623).send(embed=embed)
            await message.channel.send('관리자에게 문의사항을 보냈습니다')

    if message.content.startswith('!답변'):
        if message.author.guild_permissions.manage_messages:
            embed = discord.Embed(color=0x41df41)
            embed.add_field(name='관리자', value=message.author, inline=False)
            embed.add_field(name='답변내용', value=message.content, inline=False)
            embed.set_footer(text='문의에 대한 관리자의 답변내용입니다')
            embed.set_thumbnail(url="https://imgur.com/undefined")#GIF링크
            await message.mentions[0].send(embed=embed)
            await message.channel.send(f'{message.mentions[0]}님에게 성공적으로 답변을 보냈습니다')
        else:
            return

client.run('ODA4MTcxOTc5NTA5MjAyOTQ0.YCCqzw.9CzxlJ2BHmoiYHlQ2KYoymwa0rE')
#2차로 수정 or 응용은 가능하나 소스코드를 판매하는 행위는 자제부탁드립니다. made by ㄱㅅㄱ#0001