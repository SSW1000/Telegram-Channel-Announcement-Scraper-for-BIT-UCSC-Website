import asyncio
import requests
from bs4 import BeautifulSoup
from telegram import Bot
import os.path
from datetime import datetime, timedelta

# Function to fetch previously sent announcements from a file
def fetch_previous_announcements():
    file_path = 'previous_announcements.txt'
    previous_announcements = set()

    if os.path.exists(file_path):
        with open(file_path, 'r') as file:
            previous_announcements = set(file.read().splitlines())

    return previous_announcements

# Function to save the current announcements to a file
def save_current_announcements(announcements):
    file_path = 'previous_announcements.txt'
    
    with open(file_path, 'w') as file:
        file.write('\n'.join(announcements))

async def send_messages():
    while True:
        # URL of the website to scrape
        url = 'https://www.bit.lk/index.php/category/announcement/'  
        
        # Send a GET request to the URL
        response = requests.get(url)
        
        # Parse the HTML content using BeautifulSoup
        soup = BeautifulSoup(response.content, 'html.parser')
        
        # Find the specific article containing the announcements
        article = soup.find('article', class_='post-6')
        
        if article:
            # Find all <h4> tags containing announcement titles and their links
            announcement_tags = article.find_all('h4')
            
            # Initialize your Telegram bot with your bot token
            bot = Bot(token='YOUR_BOT_TOKEN')
        
            # Replace 'YOUR_CHANNEL_ID' with your actual Telegram channel ID
            channel_id = 'YOUR_CHANNEL_ID'
            
            # Fetch previously sent announcements
            previous_announcements = fetch_previous_announcements()
            new_announcements = []

            for tag in announcement_tags:
                announcement_title = tag.text.strip()  # Extract the text within <h4> tags
                strong_tag = tag.find_next('strong')   # Find the next <strong> tag after <h4>
                announcement_date = strong_tag.text.strip() if strong_tag else 'N/A'  # Extract the text within <strong> tags
                
                # Construct the message
                message = f"Title: {announcement_title}\nDate: {announcement_date}\n"
                
                # Check if the announcement is new
                if message not in previous_announcements:
                    new_announcements.append(message)
                    previous_announcements.add(message)

            # Send the new announcements to the Telegram channel
            if new_announcements:
                await bot.send_message(chat_id=channel_id, text='\n\n'.join(new_announcements))
            
            # Save the updated announcements to the file
            save_current_announcements(previous_announcements)

        else:
            print("Article not found or structure changed. Please check the website structure.")

        # Sleep for an hour before checking for new announcements again
        await asyncio.sleep(3600)

async def main():
    await send_messages()

if __name__ == "__main__":
    loop = asyncio.get_event_loop()
    loop.run_until_complete(main())
