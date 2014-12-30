"""

8ball.py - A simple 8ball module for the willie bot.
Copyright 2014, undernocircumstance

"""

import random
import willie
from willie.module import commands, example


answers = ["It is certain", "It is decidedly so", "Without a doubt", "Yes definitely",
           "You may rely on it", "As I see it, yes", "Most likely", "Outlook good",
           "Yes", "Signs point to yes", "Reply hazy, try again", "Ask again later",
           "Better not tell you now", "Cannot predict now", "Concentrate and ask again",
           "Don't count on it", "My reply is no", "My sources say no",
           "Outlook not so good", "Very doubtful", "This is stupid" ]

@commands('8ball')
@example('.8ball will it rain today?')
def eightball(bot,trigger):
	query = trigger.group(2)
	answer = random.choice(answers)
	if not query:
	  bot.reply("you need to ask something.")
	elif "?" not in query:
		bot.reply("this isnt a question.")
	else:
	  bot.reply(answer)
