import smtplib 
import time 
from email.mime.multipart import MIMEMultipart 
from email.mime.text import MIMEText 
import requests 
import json

# mail adresi ve şifreyi algılayın
host = "smtp.gmail.com"
port = 587
username = input("Mail adresinizi girin: ") 
password = input("Şifrenizi girin: ")

# mail adresine gönderilen mesajı kontrol edin
def check_email():
    server = smtplib.SMTP(host,port)
    server.starttls()
    server.login(username,password)
    resp, emails = server.list()
    emails = emails[0].split()
    for mail in emails:
        resp, data = server.retr(mail)
        if "Yeni mail" in data[0]:
            return True
    server.quit()
    return False

# kullanıcıdan telefon numarasını alın
phone_number = input("Telefon numaranızı girin: ")

# haberi göndermek için WhatsApp API'sini kullanın
def send_whatsapp_message(phone_number, message):
    url = "https://eu44.chat-api.com/instance112459/sendMessage?token=vj8zw0h2ke0eolx4"
    data = {
    'phone': phone_number,
    'body': message
    }
    response = requests.post(url, data=data)
    data = json.loads(response)
    data = json.loads(response)
    return response

# mail kontrolünü sürekli yap
while True:
    if check_email():
        send_whatsapp_message(phone_number, "Yeni bir mail var!")
    time.sleep(30)
