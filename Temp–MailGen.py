import requests
import json
import random
import re
from faker import Faker
from time import sleep

faker = Faker()

def GenPas():
    return ''.join(random.choices('abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789', k=8))

def GetNewEmail():
    name = faker.first_name()
    url = 'https://api.internal.temp-mail.io/api/v3/email/new'
    data = {'name': name, 'domain': 'ehra.com'}
    headers = {'User-Agent': 'Mozilla/5.0'}

    response = requests.post(url, json=data, headers=headers)
    if response.status_code == 200:
        req = response.json()
        Email = req['email']
        print(f"Your Email is {Email}")
        return Email
    else:
        print(f"Failed to create account. Status code: {response.status_code}")
        return None

def GetMessage(email):
    while True:
        sleep(2)
        url = f'https://api.internal.temp-mail.io/api/v3/email/{email}/messages'
        response = requests.get(url)
        if response.status_code == 200:
            messages = response.json()
            if messages:
                for msg in messages:
                    body_text = msg.get('body_text', '')
                    subject = msg.get('subject', '')
                    print(f"Subject: {subject}")
                    match = re.search(r'\b\d{4}\b', body_text)
                    if match:
                        code = match.group(0)
                        print(f"Your verification code is: {code}")
                        return code
            else:
                print("No messages yet.")
        else:
            print(f"Failed to get messages. Status code: {response.status_code}")

def OTP(email, code):
    url = "https://v1.prd.socket.araby.ai/otp/verify"
    payload = json.dumps({
        "otp": code,
        "email": email,
    })
    headers = {
        'User-Agent': "Dart/3.2 (dart:io)",
        'Accept-Encoding': "gzip",
        'Content-Type': "application/json",       
    }
    
    response = requests.post(url, data=payload, headers=headers)
    if "Authentication successful" in response.text:
        token = response.json()["token"]
        print(f"Authentication successful. Token: {token}")
        with open("Ai Tokens.txt", "a") as f:
         f.write(token +'\n')
        return token
    else:
        print("Failed to verify OTP.")
        return None

def Reg(email, password):
    url = "https://v1.prd.socket.araby.ai/register"
    payload = json.dumps({
        "email": email,
        "password": password,
        "method": "OTP",
        "is_mobile": True
    })
    headers = {
        'User-Agent': "Dart/3.2 (dart:io)",
        'Accept-Encoding': "gzip",
        'Content-Type': "application/json"
    }

    response = requests.post(url, data=payload, headers=headers)
    if "User registered successfully! Please verify your email." in response.text:
        print("User registered successfully. Please verify your email.")
        code = GetMessage(email)
        if code:
            return OTP(email, code)
    else:
        print("Failed to register user.")

while True:
    email = GetNewEmail()
    if email:
        password = GenPas()
        print(f"Generated password: {password}")
        token = Reg(email, password)
        if token:
            print(f"Registration completed. Token: {token}")

