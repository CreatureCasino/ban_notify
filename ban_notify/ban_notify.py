from redbot.core import commands

class BanNotify(commands.Cog):
    """Sends a DM with a hosted MP4 when a user is banned."""

    def __init__(self, bot):
        self.bot = bot
        self.video_url = "https://www.blackjackthefox.com/wp-content/uploads/2025/09/youvebeenbanned.mp4"

    @commands.Cog.listener()
    async def on_member_ban(self, guild, user):
        try:
            dm_channel = await user.create_dm()
            await dm_channel.send(f"You got banned! Watch this: {self.video_url}")
        except Exception as e:
            print(f"Failed to send DM to {user}: {e}")
