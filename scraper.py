import requests
from bs4 import BeautifulSoup
import smtplib


URL = 'https://www.grailed.com/listings/13116372-fog-x-fear-of-god-x-pacsun-fear-of-god-essentials-graphic-mesh-drawstring-shorts-sz-s'
headers = {"User-Agent": 'Mozilla/5.0: (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/79.0.3945.130 Safari/537.36'}
def check_price():
    page = requests.get(URL, headers=headers)
    soup = BeautifulSoup(page.content, 'html.parser')

    title = soup.find(attrs={'listing-title sub-title'}).get_text()
    price = soup.find(attrs={'-price'}).get_text()
    converted_price = float(price[-3:])
    if (converted_price < 45.0):
        send_mail()

    print(title.strip())
    print(converted_price)
def send_mail():
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.ehlo()
    server.starttls()
    server.ehlo()
    server.login('noahdabalboa@gmail.com', 'xlnntxentdqrmyll')

    subject = 'Price is down!'
    body = 'Check the link to buy: https://www.grailed.com/listings/13116372-fog-x-fear-of-god-x-pacsun-fear-of-god-essentials-graphic-mesh-drawstring-shorts-sz-s '

    msg = f"Subject: {subject}\n\n{body}"

    server.sendmail('noahdabalboa@gmail.com',
                    'noahjhein@gmail.com',
                    msg
                    )
    print('Email send successfully')
    server.quit()
check_price()

