import http
import json
import requests
import os
from discord_webhook import DiscordWebhook, DiscordEmbed
import dotenv
dotenv.load_dotenv()
HOOK_URL=os.getenv("DISCORD_WEBHOOK_URL")

def send_discord_message(webhook_url, content, embed_title=None, embed_description=None):
    """
    Send a message to a Discord channel via webhook.
    
    :param webhook_url: The Discord webhook URL (string)
    :param content: Plain text message (string)
    :param embed_title: Optional embed title (string)
    :param embed_description: Optional embed description (string)
    """
    try:
        # Create webhook object
        webhook = DiscordWebhook(url=webhook_url, content=content)

        # If embed data is provided, add it
        if embed_title or embed_description:
            embed = DiscordEmbed(title=embed_title or "", description=embed_description or "", color=0x00ff00)
            webhook.add_embed(embed)

        # Execute webhook
        response = webhook.execute()

        # Check response
        if response.status_code in (200, 204):
            print("✅ Message sent successfully!")
        else:
            print(f"⚠️ Failed to send message. HTTP {response.status_code}: {response.text}")

    except Exception as e:
        print(f"❌ Error: {e}")

# Example usage
if __name__ == "__main__":

    send_discord_message(
        webhook_url=HOOK_URL,
        content="Hello from Python! 🚀",
        embed_title="Sample Embed",
        embed_description="This is an example embed message."
    )
