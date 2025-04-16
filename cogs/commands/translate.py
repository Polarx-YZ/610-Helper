import discord
from discord.ext import commands
import re
import random


class Translator(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    async def get_vowels(self, sentence):
        vowels = list("aieou")
        letters = []
        for letter in sentence:
            if letter in vowels:
                letters.append(letter)
        return letters

    @commands.command(brief="Decode the symbols")
    async def decode(self, ctx, *args):
        if len(args) <= 0:
            return await ctx.reply("Please supply a message to decode!")
        
        try:
            message = re.sub(r"(?is)\!", "a", " ".join(args)) 
            message = re.sub(r"(?is)\;", "b", message)
            message = re.sub(r"(?is)\“", "c", message)
            message = re.sub(r"(?is)\#", "d", message)
            message = re.sub(r"(?is)\÷", "e", message)
            message = re.sub(r"(?is)\$", "f", message)
            message = re.sub(r"(?is)\%", "g", message)
            message = re.sub(r"(?is)\&", "h", message)
            message = re.sub(r"(?is)\>", "i", message)
            message = re.sub(r"(?is)j", "j", message)
            message = re.sub(r"(?is)\(", "k", message)
            message = re.sub(r"(?is)\)", "l", message)
            message = re.sub(r"(?is)\?", "m", message)
            message = re.sub(r"(?is)\,", "n", message)
            message = re.sub(r"(?is)\[", "o", message)
            message = re.sub(r"(?is)\]", "p", message)
            message = re.sub(r"(?is)q", "q", message)
            message = re.sub(r"(?is)\=", "r", message)
            message = re.sub(r"(?is)\@", "s", message)
            message = re.sub(r"(?is)\/", "t", message)
            message = re.sub(r"(?is)\<", "u", message)
            message = re.sub(r"(?is)\:", "v", message)
            message = re.sub(r"(?is)\×", "w", message)
            message = re.sub(r"(?is)x", "x", message)
            message = re.sub(r"(?is)\_", "y", message)
            message = re.sub(r"(?is)z", "z", message)
            
            await ctx.reply(message)
        except Exception as e:
            await ctx.reply("Something went wrong.")
            print(e)
        
    @commands.command(brief="Read what P34RL is saying")
    async def read(self, ctx, *args):
        if len(args) <= 0:
            return await ctx.reply("Please supply a message to read!")
        
        message = re.sub(r"(?is)3", "e", " ".join(args)) 
        message = re.sub(r"(?is)2", "s", message)
        message = re.sub(r"(?is)6", "b", message)
        message = re.sub(r"(?is)7", "t", message)
        message = re.sub(r"(?is)l<", "k", message)
        message = re.sub(r"(?is)4", "a", message)
        message = re.sub(r"(?is)vv", "w", message)
        message = re.sub(r"(?is)0", "o", message)
        message = re.sub(r"(?is)1", "i", message)
        message = re.sub(r"(?is)€", "c", message)

        await ctx.reply(message)

    
async def setup(bot):
    await bot.add_cog(Translator(bot))
