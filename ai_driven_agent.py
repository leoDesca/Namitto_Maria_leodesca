import os
import requests
import time
from datetime import datetime
from telegram import Bot
from telegram.error import TelegramError
import asyncio
import schedule
import logging

# Load environment variables
TELEGRAM_BOT_TOKEN = "7829797401:AAH_ouSMEOHOf0IIUXGecmVxclRTx7e-86Q"
CHAT_ID =-1002756709393
#url = f"https://api.telegram.org/bot{TELEGRAM_BOT_TOKEN}/sendMessage?chat_id={CHAT_ID}&text={message}"
#r = requests.get(url)
#print(r.json())




# Configure logging
print("Starting Telegram Daily Poster")
print(f"Current time: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")




# Main posting loop
while True:
    current_time = datetime.now().strftime("%H:%M")
    
    if current_time == "09:00":  # Post at 9 AM daily
        print("Preparing daily post...")
        
        # Create message content
        today = datetime.now().strftime("%A, %B %d")
        message =( f"📢 Good morning! Here's your daily update for {today}.\n\n" \
                  f"Stay tuned for today's news and updates! #DailyPost")
        
        # Send to Telegram
        url = f"https://api.telegram.org/bot7829797401:AAH_ouSMEOHOf0IIUXGecmVxclRTx7e-86Q/sendMessage"
        payload = {
            "chat_id": -1002756709393,
            "text": message,
            "parse_mode": "HTML"
        }
        
        try:
            response = requests.post(url, json=payload)
        
            if response.status_code == 200:
                print("Message sent successfully!")
                print(f"Content: {message[:50]}...")
            else:
                print(f"Error sending message: {response.text}")
        except Exception as e:
            print(f"Connection failed: {e}")
        
        # Wait 60 seconds to avoid duplicate posts
        time.sleep(60)
    
    # Check time every 30 seconds
    time.sleep(30)
