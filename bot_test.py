from datetime import datetime
import discord
import random
from discord import message
import fontstyle
from discord.ext import commands
import asyncio

fontstyle.apply('GEEKSFORGEEKS', 'bold/Italic/red/GREEN_BG')

TOKEN = 'ODkzNzY1MzQ0ODE1MTA0MDQw.YVgN1w.voUWNDP5u_ImsaA0OvRe4QTmIIs'

client = discord.Client()


bodyImage = ['https://scontent.fsgn2-3.fna.fbcdn.net/v/t1.15752-9/242461959_898427124417803_2795730846549236492_n.jpg?_nc_cat=108&ccb=1-5&_nc_sid=ae9488&_nc_ohc=c15dRIaYIpwAX9rVZ2y&_nc_ht=scontent.fsgn2-3.fna&oh=655ca8e9a0627efbee452fc9fb777d35&oe=617DB99C', 'https://scontent.fsgn2-3.fna.fbcdn.net/v/t1.15752-9/242615973_1194288397732828_5132327580554350570_n.jpg?_nc_cat=106&ccb=1-5&_nc_sid=ae9488&_nc_ohc=gBK4r6g9qAEAX8oi6tr&_nc_ht=scontent.fsgn2-3.fna&oh=ca48c76cbd3064a5f8e9d824c3e29d60&oe=61809B2C', 'https://scontent.fsgn2-3.fna.fbcdn.net/v/t1.15752-9/242198963_559161498534551_2435290135785564724_n.jpg?_nc_cat=108&ccb=1-5&_nc_sid=ae9488&_nc_ohc=dN0C9epOU8IAX-O_sTK&tn=vBVNBVJHdLUPzbp9&_nc_ht=scontent.fsgn2-3.fna&oh=ecc99be1f482634acff152565eb3efa0&oe=617E4C24', 'https://scontent.fsgn2-5.fna.fbcdn.net/v/t1.15752-9/120048115_1739784769503362_3594889784677712416_n.jpg?_nc_cat=104&ccb=1-5&_nc_sid=ae9488&_nc_ohc=KfikudNJ8ysAX-iDe4L&tn=vBVNBVJHdLUPzbp9&_nc_ht=scontent.fsgn2-5.fna&oh=9eaad7d2f32dfec7a5460fc930c3659c&oe=617FD424']

#fileInput = open('hinhae.txt', 'r')
#fileInput.readline().splitlines()
#image = random.choice(fileInput)

with open('shop.txt', 'r', encoding='utf-8') as fileInpshop:
    dataShop = fileInpshop.readlines()
    shop = ''.join(dataShop).replace('\n',' ')


@client.event
async def on_ready():
    print('𝘞𝘦 𝘩𝘢𝘷𝘦 𝘭𝘰𝘨𝘨𝘦𝘥 𝘪𝘯 𝘢𝘴 {0.user}'.format(client))


@client.event
async def on_message(message):
    username = str(message.author).split('#')[0]
    user_message = str(message.content)
    channel = str(message.channel.name)
    print(f'{username}: {user_message} ({channel})')

    if message.author == client.user:
        return

    #bot = commands.Bot(command_prefix=commands.when_mentioned_or(','))


    if message.channel.name == 'coin-test':
        if user_message.lower() == ',hello':
            await message.channel.send(f'𝖃𝖎𝖓 𝖈𝖍𝖆𝖔 {username}!')
        elif user_message.lower() == ',bye':
            await message.channel.send(f'𝕿𝖆𝖒 𝖇𝖎𝖊𝖙 {username} 𝖓𝖍𝖆!')
        elif user_message.lower() == ',myping':
            await message.channel.send(f' {round(client.latency * 1000)}ms')
        elif user_message.lower() == ',body':
            await message.channel.send(random.choice(bodyImage))
        elif user_message.lower() == ',hinh':
            await message.channel.send((random.choice(list(open('hinhae.txt')))))
        elif user_message.lower() == ',reminder':
            await message.channel.send(f'!remind-me 4h quán-ăn-qhuy  @everyone MỌI NGƯỜI NHỚ ĂN UỐNG ĐẦY ĐỦ KẺO ĐÓI LĂN RA CHẾT!!! --everyone --repeat 500')
    #if message.channel.name == 'gta-test-bot':
        elif user_message.lower() == ',shop':
                    await message.channel.send(shop)
        elif user_message.lower() == ',shop1':
                    fileOutinv = open('invent.txt', 'a')
                    fileOutinv.write(f'\n chicken')
                    fileOutinv.close()
                    await message.channel.send(f'Đã mua thành công')                   
        elif user_message.lower() == ',shop2':
                    fileOutinv = open('invent.txt', 'a', encoding='utf-8')
                    fileOutinv.write(f'\n weed')
                    fileOutinv.close()
                    await message.channel.send(f'Đã mua thành công')          
        elif user_message.lower() == ',shop3':
                    fileOutinv = open('invent.txt', 'a', encoding='utf-8')
                    fileOutinv.write(f'\n water')
                    fileOutinv.close()
                    await message.channel.send(f'Đã mua thành công')
        elif user_message.lower() == ',shop4':
                    fileOutinv = open('invent.txt', 'a', encoding='utf-8')
                    fileOutinv.write(f'\n bánh mì')
                    fileOutinv.close()
                    await message.channel.send(f'Đã mua thành công')
        elif user_message.lower() == ',inventory':
            with open('invent.txt', 'r', encoding='utf-8') as fileinvent:
                invent = fileinvent.readlines()
                inventjoined = ''.join(invent).replace('\n',' ')
                await message.channel.send('Balô của bạn đang có:')
                await message.channel.send(invent)
        elif user_message.lower() == ",baucua":
            baucua = ['Dịch vụ bầu cua đang bảo trì']
            await message.channel.send(baucua)
            await message.channel.send(random.choice(baucua) + ' ' + random.choice(baucua) + ' ' + random.choice(baucua))

        elif user_message.lower() == ',work':
            moneyfromwork = random.randint(50, 1000)
            await message.channel.send(f'{username} đã nhận được {moneyfromwork}$')
            #with open('money.txt', 'w') as fileInpmon:
             #           fileInpmon.write(str(moneyfromwork))
              #          fileInpmon.write('$')
            int_moneyfromwork = int(moneyfromwork)
            #print(int_moneyfromwork)

            user_money = open('user_money.txt', 'r')
            base_money = user_money.readline()
            int_basemoney = int(base_money)
            print(int_basemoney)

            present_money = (int_basemoney + int_moneyfromwork)
            int_presentmoney = int(present_money)
            print(int_presentmoney)
            user_money = open('user_money.txt', 'w')
            user_money.write(str(int_presentmoney))

        elif user_message.lower() == ',mymoney':
            mymoney = open('user_money.txt', 'r')
            mymoneyread = mymoney.readline()
            await message.channel.send(f'Tài khoản đang có: {mymoneyread}$')


        while user_message.lower() == ',startmining':
            primary_code = random.randint(1, 10)
            print(primary_code)
            secondary_code = random.randint(1, 100)
            print(secondary_code)

            if secondary_code % primary_code  == 0:
                    print('Bitcoin earned')
                    now = datetime.now()
                    earnedbitcon = ('\n Bitcoin earned')
                    date_time = now.strftime(" %d/%m/%Y %H:%M:%S")
                    user_bitcoin = open('userbitcoin.txt', 'a')
                    user_bitcoin.write(str(earnedbitcon) + (date_time))
                    user_bitcoin.close()
                    await message.channel.send(f'Bitcoin earned')
            else:
                    await message.channel.send(f'Exchange failed, continue progress...')
            await asyncio.sleep(10)
            if user_message.lower() == ',stopmining':
                break

        if user_message.lower() == ',mybitcoin':
            user_bitcoin = open('userbitcoin.txt', 'r')
            mybitcoin = user_bitcoin.readlines()
            await message.channel.send(mybitcoin)




        


        
    

      
    
    
   

client.run(TOKEN)

    