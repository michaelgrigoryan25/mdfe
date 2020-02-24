import requests
from bs4 import BeautifulSoup
import smtplib
import time

URL = "https://theskylive.com/mars-tracker"


#SEARCH THE INTERNET FOR "MY USER AGENT COPY AND PASTE IT IN "YOUR USER AGENT(line 11)""
headers = {
    "User-Agent": 'YOUR USER AGENT'}


#YOU'LL NEED TO CHANGE TARGET AND STARTING DISTANCE IF YOU WOULD LIKE TO.(line 23, 24)
def check_distance():
    page = requests.get(URL, headers=headers)

    soup = BeautifulSoup(page.content, 'html.parser')

    title = soup.find(id="disearth").get_text()
    mars_distance = soup.find(id="disearth").get_text()
    converted_dist = float(mars_distance)
    target_distance = float(200000000)
    starting_distance = float(293500000)
    distance_from_earth = str(starting_distance - converted_dist)

    while ():
        if (converted_dist < target_distance):
            send_mail()
            print("The Mars just got closer by " + distance_from_earth + "km!")
            print(converted_dist)
            print("The operation has been completed successfully!")
            break
    if (converted_dist > target_distance):
        print("Waiting for target distance.")
        print(mars_distance + "km")


##########################
def send_mail():
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.ehlo()
    server.starttls()
    server.ehlo()

    server.login('YOUR GMAIL', "YOUR GMAIL PRIVATE KEY")

    page = requests.get(URL, headers=headers)
    soup = BeautifulSoup(page.content, 'html.parser')
    title = soup.find(id="disearth").get_text()
    mars_distance = soup.find(id="disearth").get_text()
    converted_dist = float(mars_distance)
    starting_distance = float(293500000)
    distance_from_earth = str(starting_distance - converted_dist)
    subject = 'The Mars Is Closer!'
    body = "The Mars just got closer to Earth by " + distance_from_earth + "km!"

    msg = f"Subject: {subject}\n\n{body}"
    server.sendmail(
        "from E-MAIL(example@gmail.com)",
        "TO E-MAIL(example@gmail.com)",
        msg
    )
    print("Email has been sent.")
    server.quit()


while True:
    check_distance()
    time.sleep(0.1)
