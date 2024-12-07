import discord 
from discord.ext import commands # discord kütüphanesindeki discord.ext fonksiyonunu kullanarak commands fonksiyonunu import ettik


intents = discord.Intents.default()
intents.typing = False                                  # intents = içindekiler ,amaçlar , niyetler
bot = commands.Bot(command_prefix='!', intents=intents) # botu  komutlarını belirleyen işaret   # prefix = botumuuz bizim komutlarımızı algılamasını sağlar

# bot çalıştığunda etkinleşen fonksiyon
@bot.event  # = etkinlik, olay
async def on_ready():
    print(f'{bot.user.name} olarak giriş yaptık.')    # asenkron = async = eş zamanlı
    print('Botunuz hazır!')                            # on_ready = hazır  
                                                        #senkron = eş zamanlı olmayan

    async def on_message(message):
        if message.author == bot.user.name:  # author = yazar , botun sahibi
            return
        if message.content.lower() == 'selam':
            await message.channel.send('Selam! Benim adım Bot.')

            await bot.process_commands(message)  # process = hazırlamak, işlemek

            @bot.command()
            async def selamver(ctx):
                await ctx.send('Selam! Nasılsın?')


# botu çalıştırmak için buraya botunuzun tokenini yazın

bot.run('DİSCORDDAN ALDIĞINIZ BOT TOKENİNİZİ BURAYA GİRİNİZ')