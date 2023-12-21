import requests

bot_token = 'YOUR_BOT_TOKEN'  # Replace 'YOUR_BOT_TOKEN' with your actual bot token
channel_username = 'YOUR_CHANNEL_USERNAME'  # Replace 'YOUR_CHANNEL_USERNAME' with your channel's username

# Function to get the chat ID of a channel
def get_channel_id():
    try:
        url = f"https://api.telegram.org/bot{bot_token}/sendMessage?chat_id=@{channel_username}&text=Test"
        response = requests.get(url)
        data = response.json()
        chat_id = data['result']['chat']['id']
        return chat_id
    except Exception as e:
        print("An error occurred:", e)
        return None

# Get the channel ID
channel_id = get_channel_id()
print("Channel ID:", channel_id)
