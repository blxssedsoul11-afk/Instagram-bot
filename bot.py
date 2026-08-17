import os
import time
from dotenv import load_dotenv
from instagrapi import Client
import logging

# Load environment variables
load_dotenv()

# Setup logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s'
)
logger = logging.getLogger(__name__)

# Instagram credentials
INSTAGRAM_USERNAME = os.getenv('INSTAGRAM_USERNAME')
INSTAGRAM_PASSWORD = os.getenv('INSTAGRAM_PASSWORD')
TARGET_USERNAME = '@xristovv_official77'
TARGET_MESSAGE = 'Здр брат'

def login_instagram():
    """Login to Instagram"""
    try:
        cl = Client()
        logger.info(f"Attempting to login as {INSTAGRAM_USERNAME}...")
        cl.login(INSTAGRAM_USERNAME, INSTAGRAM_PASSWORD)
        logger.info("✓ Successfully logged in!")
        return cl
    except Exception as e:
        logger.error(f"✗ Login failed: {e}")
        return None

def stay_online(client, interval=30):
    """Keep the bot online by sending periodic requests"""
    try:
        logger.info(f"Starting keep-alive mechanism (every {interval} seconds)...")
        while True:
            try:
                # Send a simple request to keep the session alive
                client.get_timeline_feed()
                logger.info("✓ Keep-alive ping sent")
                time.sleep(interval)
            except Exception as e:
                logger.warning(f"Keep-alive error: {e}")
                time.sleep(interval)
    except KeyboardInterrupt:
        logger.info("Keep-alive stopped by user")

def follow_user(client, username):
    """Follow a user"""
    try:
        logger.info(f"Attempting to follow {username}...")
        user_id = client.user_id_from_username(username.replace('@', ''))
        client.user_follow(user_id)
        logger.info(f"✓ Successfully followed {username}!")
        return True
    except Exception as e:
        logger.error(f"✗ Failed to follow {username}: {e}")
        return False

def send_message(client, username, message):
    """Send a direct message to a user"""
    try:
        logger.info(f"Attempting to send message to {username}...")
        user_id = client.user_id_from_username(username.replace('@', ''))
        client.send_message(user_id, message)
        logger.info(f"✓ Message sent to {username}: '{message}'")
        return True
    except Exception as e:
        logger.error(f"✗ Failed to send message to {username}: {e}")
        return False

def main():
    """Main bot function"""
    if not INSTAGRAM_USERNAME or not INSTAGRAM_PASSWORD:
        logger.error("✗ Instagram credentials not found in .env file")
        return
    
    # Login
    client = login_instagram()
    if not client:
        return
    
    # Follow user
    follow_user(client, TARGET_USERNAME)
    time.sleep(2)
    
    # Send message
    send_message(client, TARGET_USERNAME, TARGET_MESSAGE)
    time.sleep(2)
    
    # Stay online
    logger.info("Bot is now running and staying online...")
    stay_online(client, interval=30)

if __name__ == "__main__":
    main()
