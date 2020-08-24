from wxpy import *

bot = Bot()

my_friend = bot.friends().search('飞鱼', sex=MALE, city="上海")[0]