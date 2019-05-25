import discord

from discord.ext import commands

class license(commands.Cog):
    
    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    async def license(self, ctx):
            await ctx.author.send('''```Copyright (c) 2019, Bryson Rogers
All rights reserved.

"Instances" refers to this software and modified versions being ran for the 
purpose of providing service(s) and utility without the sole intention to
develop this software, contribute to this software, or release source code publicly.```''')
            await ctx.author.send('''```
Redistribution and use in source and binary forms, with or without
modification, are permitted provided that the following conditions are met:
1. Redistributions of source code must retain the above copyright
   notice, this list of conditions and the following disclaimer.
2. Redistributions in binary form must reproduce the above copyright
   notice, this list of conditions and the following disclaimer in the
   documentation and/or other materials provided with the distribution.
3. All advertising materials mentioning features or use of this software
   must display the following acknowledgement:
   "This product includes software developed by Bryson Rogers and contributers."
   It must also link or display a link to the official GitHub repository/website maintained 
   by Bryson Rogers where source is available (as of 2019-05-24 is https://github.com/w3bb/vally).
4. The name of Bryson Rogers, "School Students Discord":
   or the names of its contributors may not be used to endorse or promote products
   derived from this software without specific prior written permission.
5. Instances must be able to reproduce the above copyright notice, this
   list of conditions, and the following disclaimer in such a way that it's
   easily readable to people interacting with the instance.```''')

            await ctx.author.send('''```THIS SOFTWARE IS PROVIDED BY BRYSON ROGERS ''AS IS'' AND ANY
EXPRESS OR IMPLIED WARRANTIES, INCLUDING, BUT NOT LIMITED TO, THE IMPLIED
WARRANTIES OF MERCHANTABILITY AND FITNESS FOR A PARTICULAR PURPOSE ARE
DISCLAIMED. IN NO EVENT SHALL BRYSON ROGERS BE LIABLE FOR ANY
DIRECT, INDIRECT, INCIDENTAL, SPECIAL, EXEMPLARY, OR CONSEQUENTIAL DAMAGES
(INCLUDING, BUT NOT LIMITED TO, PROCUREMENT OF SUBSTITUTE GOODS OR SERVICES;
LOSS OF USE, DATA, OR PROFITS; OR BUSINESS INTERRUPTION) HOWEVER CAUSED AND
ON ANY THEORY OF LIABILITY, WHETHER IN CONTRACT, STRICT LIABILITY, OR TORT
(INCLUDING NEGLIGENCE OR OTHERWISE) ARISING IN ANY WAY OUT OF THE USE OF THIS
SOFTWARE, EVEN IF ADVISED OF THE POSSIBILITY OF SUCH DAMAGE.```''')

            await ctx.author.send("You can view the source code at: https://www.github.com/w3bb/vally")


def setup(bot):
    bot.add_cog(license(bot))
