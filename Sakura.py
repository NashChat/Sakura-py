import os
import random
import string
import webbrowser
import requests
import base64
import datetime

WEBHOOK_URLS = {
    "scanner": "", 
    "password_secure": "", 
    "ddos_tool": "",
    "random_cc_gen": "",
    "discord_raider_bot": "",
    "message_spammer": "",
    "website_ping_checker": ""
}

AES_KEY = None

BOT_NAME = "Sakura AI"
BOT_AVATAR_URL = "https://i.pinimg.com/564x/03/ee/79/03ee79e738d8f47aed9ac892b7a73ec8.jpg"

def print_title():
    print("\033[95m" + "██████  ▄▄▄       ██ ▄█▀ █    ██  ██▀███   ▄▄▄          ▄▄▄       ██▓")
    print("\033[95m" + "▒██    ▒ ▒████▄     ██▄█▒  ██  ▓██▒▓██ ▒ ██▒▒████▄       ▒████▄    ▓██▒")
    print("\033[95m" + "░ ▓██▄   ▒██  ▀█▄  ▓███▄░ ▓██  ▒██░▓██ ░▄█ ▒▒██  ▀█▄     ▒██  ▀█▄  ▒██▒")
    print("\033[95m" + "  ▒   ██▒░██▄▄▄▄██ ▓██ █▄ ▓▓█  ░██░▒██▀▀█▄  ░██▄▄▄▄██    ░██▄▄▄▄██ ░██░")
    print("\033[95m" + "▒██████▒▒ ▓█   ▓██▒▒██▒ █▄▒▒█████▓ ░██▓ ▒██▒ ▓█   ▓██▒    ▓█   ▓██▒░██░")
    print("\033[95m" + "▒ ▒▓▒ ▒ ░ ▒▒   ▓▒█░▒ ▒▒ ▓▒░▒▓▒ ▒ ▒ ░ ▒▓ ░▒▓░ ▒▒   ▓▒█░    ▒▒   ▓▒█░░▓  ")
    print("\033[95m" + "░ ░▒  ░ ░  ▒   ▒▒ ░░ ░▒ ▒░░░▒░ ░ ░   ░▒ ░ ▒░  ▒   ▒▒ ░     ▒   ▒▒ ░ ▒ ░")
    print("\033[95m" + "░  ░  ░    ░   ▒   ░ ░░ ░  ░░░ ░ ░   ░░   ░   ░   ▒        ░   ▒    ▒ ░")
    print("\033[95m" + "      ░        ░  ░░  ░      ░        ░           ░  ░         ░  ░ ░  ")
    print("\033[95m" + "                                                                        ")
    print("Made By NacHash ")

def clear():
    os.system('cls' if os.name == 'nt' else 'clear')

def generate_credit_card_number():
    first_four_digits = ''.join(random.choices('123456789', k=4))
    expiration_date = ''.join(random.choices(string.digits, k=2)) + '/' + ''.join(random.choices(string.digits, k=2))
    ccv = ''.join(random.choices(string.digits, k=3))
    remaining_digits = ''.join(random.choices('0123456789', k=12))
    credit_card_number = first_four_digits + ' ' + remaining_digits + ' ' + expiration_date + ' ' + ccv
    return credit_card_number

def generate_aes_key():
    global AES_KEY
    AES_KEY = ''.join(random.choices(string.ascii_letters + string.digits, k=16)).encode()

def encrypt_text(text):
    # Your encryption logic here
    pass

def decrypt_text(iv, ct):
    # Your decryption logic here
    pass

def set_webhook_url(selection):
    webhook_url = input(f"Please enter the webhook URL for {selection}: ")
    WEBHOOK_URLS[selection] = webhook_url

def send_to_webhook(selection, content):
    if not WEBHOOK_URLS[selection]:
        print(f"Webhook URL for {selection} is not set.")
        return

    headers = {"Content-Type": "application/json"}
    data = {
        "username": BOT_NAME,
        "avatar_url": BOT_AVATAR_URL,
        "embeds": [{
            "title": "Hello Customer",
            "description": content,
            "color": 16711680,  
        }]
    }
    response = requests.post(WEBHOOK_URLS[selection], json=data, headers=headers)
    if response.status_code == 200:
        print("Data sent successfully.")
    else:
        print("Failed to send data.")

def website_ping_checker():
    webhook_url = input("Please enter the webhook URL for website ping checker: ")
    WEBHOOK_URLS["website_ping_checker"] = webhook_url

    website_url = input("Please enter the URL of the website you want to check: ")
    response = os.system(f'ping -c 3 {website_url}')
    
    if response == 0:
        content = f"{website_url} is UP"
    else:
        content = f"{website_url} is DOWN"

    send_to_webhook("website_ping_checker", content)

def print_menu():
    print("1. Discord Raider Bot")
    print("2. Scanner")
    print("3. Password Secure")
    print("4. Roblox ExeCuter")
    print("5. Ddos Tool")
    print("6. Random CC Gen")
    print("7. Message Spammer")
    print("8. Website Ping Checker")
    print("9. Active Customers")

def print_active_customers():
    print("__        __  ___  __         ___  __  ")
    print("/  ` |  | /__`  |  /  \\  |\\/| |__  |__) ")
    print("\\__, \\__/ .__/  |  \\__/  |  | |___ |  \\ ")
    print("                                        ")
    print("Active 473 Customers")

while True:
    clear()
    print_title()
    user_input = input("Welcome to terminal, please write: ")

    if user_input.lower() == "another":
        print_menu()
        selection = input("Please select an option (1/9): ")

        if selection == "1":
            print("Discord Raider Bot selected.")
            webbrowser.open("https://discord.com/api/oauth2/authorize?client_id=1221587721294839838&permissions=0&scope=bot%20applications.commands")
        elif selection == "2":
            print("Scanner selected.")
            set_webhook_url("scanner")
            send_to_webhook("scanner", "https://github.com/pwn0sec/PwnXSS")
        elif selection == "3":
            print("Password Secure selected.")
            set_webhook_url("password_secure")
            password = input("Please enter the password you want to encrypt: ")
            generate_aes_key()
            iv, ct = encrypt_text(password)
            encoded_iv = base64.b64encode(iv.encode()).decode()
            encoded_ct = base64.b64encode(ct.encode()).decode()
            send_to_webhook("password_secure", f"Encrypted Text:\nIV: {encoded_iv}\nCT: {encoded_ct}")
        elif selection == "4":
            print("Roblox ExeCuter selected.")
            set_webhook_url("roblox_executer")
            # Your code for Roblox ExeCuter here
        elif selection == "5":
            print("Ddos Tool selected.")
            set_webhook_url("ddos_tool")
            website = input("Please enter the target website: ")
            send_to_webhook("ddos_tool", "Attack initiated successfully.")
        elif selection == "6":
            print("Random CC Gen selected.")
            filename = "cc.txt"
            set_webhook_url("random_cc_gen")
            cc_data = "\n".join(generate_credit_card_number() for _ in range(10))
            send_to_webhook("random_cc_gen", cc_data)
        elif selection == "7":
            print("Message Spammer selected.")
            set_webhook_url("message_spammer")
            message = "@everyone @here discord.gg/922 discord.gg/1337 Selamlar NacHash burdaydi"
            for _ in range(100):
                send_to_webhook("message_spammer", message)
        elif selection == "8":
            print("Website Ping Checker selected.")
            website_ping_checker()
        elif selection == "9":
            print("Active Customer selected.")
            print_active_customers()
            input("Press Enter to continue...")
