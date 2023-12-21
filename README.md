# Telegram Channel Announcement Scraper for BIT UCSC Website

This project allows you to scrape announcements from the [BIT UCSC website](https://www.bit.lk/index.php/category/announcement/) and send them to a Telegram channel using a Telegram bot.

## Disclaimer

This project is created for educational purposes only and is intended to showcase web scraping techniques using Python. Users are advised to use this script responsibly and should ensure that their actions comply with applicable laws, terms of service, and ethical standards related to web scraping and data usage. 

It's essential to respect the website's content and server load, avoid excessive scraping that could impact the website's performance, and not violate any terms of service or policies set by the website.

This project does not encourage or endorse unauthorized data scraping, and users are solely responsible for their actions while using this script.

## Prerequisites

To use this project, you need the following:

- Python 3.7 or higher installed on your machine.[![Python Badge](https://img.shields.io/badge/Python-3776AB?logo=python&logoColor=white)](https://www.python.org/)
- An existing Telegram account.

## Setup Process

### 1. Channel Creation

- **Create a Telegram Channel**:
    - Open Telegram and go to the chat list.
    - Click on the three horizontal lines at the top-left.
    - Select "New Channel" and follow the instructions to create a new public or private channel.

### 2. Bot Creation

- **Create a Telegram Bot**:
    - Start a chat with BotFather on Telegram.
    - Use the `/newbot` command to create a new bot.
    - Follow the instructions, and you'll receive a token for your bot. **Ensure you keep this token safe and confidential.**

### 3. Add Bot as Channel Admin

- **Make the Bot an Administrator**:
    - Open the channel created earlier.
    - Go to the channel's settings by clicking on its name.
    - Click on "Administrators" and then select "Add Admin".
    - Search for your bot's username and add it as an administrator with appropriate permissions (at least permission to send messages).

### 4. Get Channel ID using id.py

- **Fetch Channel ID**:
    - Open `id.py`.
    - Replace `'YOUR_BOT_TOKEN'` with the bot token obtained from BotFather.
    - Replace `'YOUR_CHANNEL_USERNAME'` with the username of the channel created earlier.
    - Run `id.py`.
    - The script will output the channel ID in the console.

Ensure the bot has sufficient permissions to send messages in the channel before running `id.py` to fetch the channel ID.

### 5. Running bit.py

- **Scrape and Send Announcements**:
    - Open `bit.py`.
    - Replace `'YOUR_BOT_TOKEN'` and `'YOUR_CHANNEL_ID'` with the bot token and channel ID respectively.
    - Adjust the scraping logic if needed.
    - Run `bit.py`.
    - The script will scrape announcements from the [BIT UCSC website](https://www.bit.lk/index.php/category/announcement/) and send them to the channel.

## Running the Scripts

Ensure you have installed the required Python libraries by running:
```bash
pip install requests beautifulsoup4 python-telegram-bot

python id.py   # Fetches the Channel ID
python bit.py  # Scrapes and Sends Announcements to Channel
```
## Handling Flooded Channels

If the channel gets flooded due to `previous_announcements.txt` not created by the script, follow these steps:

### Specify Absolute File Path

Modify the Python script to include an absolute file path for `previous_announcements.txt` to ensure the file is created in a specific location where you have control over its contents.

```python
# Function to fetch previously sent announcements from a file
def fetch_previous_announcements():
    file_path = '/absolute/path/to/previous_announcements.txt'  # Specify absolute file path here
    previous_announcements = set()

    if os.path.exists(file_path):
        with open(file_path, 'r') as file:
            previous_announcements = set(file.read().splitlines())

    return previous_announcements

# Function to save the current announcements to a file
def save_current_announcements(announcements):
    file_path = '/absolute/path/to/previous_announcements.txt'  # Specify absolute file path here

    with open(file_path, 'w') as file:
        file.write('\n'.join(announcements))
```
