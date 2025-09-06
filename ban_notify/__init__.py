from .ban_notify import BanNotify

async def setup(bot):
    await bot.add_cog(BanNotify(bot))
