from urllib.request import urlopen
from bs4 import BeautifulSoup
import os
import csv
import urllib
import re

# creating CSV file to be used
try:

    file = open(os.path.expanduser(r"~/Desktop/mannar.csv"), "wb")
    # file.write( b"hotel_name" + b"," + b"description"+ b"," + b"features" + b"," +b"price"+b"," +b"location" +b"\n")
    file.write(
        b"hotel_name" + b"," + b"description" + b"," + b"features" + b"," + b"room_type" + b"," + b"price" + b"," + b"price_description" + b"," + b"location" + b"," + b"location_description" + b"," + b"contact_no" + b"," + b"ratings" + b"," + b"reviews" + b"\n")

except:

    os.remove(os.path.expanduser(r"~/Desktop/mannar.csv"))
    file = open(os.path.expanduser(r"Desktop/mannar.csv"), "wb")
    # file.write(b"hotel_name" + b"," + b"description"+ b"," + b"features" + b"," +b"price"+b"," +b"location" +b"\n")
    file.write(
        b"hotel_name" + b"," + b"description" + b"," + b"features" + b"," + b"room_type" + b"," + b"price" + b"," + b"price_description" + b"," + b"location" + b"," + b"location_description" + b"," + b"contact_no" + b"," + b"ratings" + b"," + b"reviews" + b"\n")

# List the first page of sites - separate the websites with ,
WebSites = ["https://www.tripadvisor.com/Hotel_Review-g2435125-d3491989-Reviews-The_Palmyrah_House-Mannar_Northern_Province.html",
            "https://www.tripadvisor.com/Hotel_Review-g2435125-d7314099-Reviews-Hotel_Agape-Mannar_Northern_Province.html",
            "https://www.tripadvisor.com/Hotel_Review-g2435125-d2475717-Reviews-Mannar_Guest_House-Mannar_Northern_Province.html",
            "https://www.tripadvisor.com/Hotel_Review-g2435125-d4495262-Reviews-Shell_Coast_Resort-Mannar_Northern_Province.html",
            "https://www.tripadvisor.com/Hotel_Review-g2435125-d13491193-Reviews-El_Saddai-Mannar_Northern_Province.html",
            "https://www.tripadvisor.com/Hotel_Review-g2435125-d10023632-Reviews-Hotel_Juli_Reception-Mannar_Northern_Province.html",
            "https://www.tripadvisor.com/Hotel_Review-g2435125-d13817411-Reviews-Hotel_Flomingo-Mannar_Northern_Province.html",
            "https://www.tripadvisor.com/Hotel_Review-g303894-d7113450-Reviews-Jiwan_Residency-Rameswaram_Ramanathapuram_District_Tamil_Nadu.html",
            "https://www.tripadvisor.com/Hotel_Review-g303894-d3398159-Reviews-Hotel_Sri_Saravana_Rameshwaram-Rameswaram_Ramanathapuram_District_Tamil_Nadu.html",
            "https://www.tripadvisor.com/Hotel_Review-g303894-d12254073-Reviews-Hotel_Ashoka-Rameswaram_Ramanathapuram_District_Tamil_Nadu.html"]

# looping through each site until it hits a break
for theurl in WebSites:
    thepage = urllib.request.urlopen(theurl)
    soup = BeautifulSoup(thepage, "html.parser")

    #get hotel name
    hotel_name = soup.find(attrs={"class": "ui_header h1"}).text.replace('"', ' ').strip()
    print(hotel_name)

    #get description
    d_data = soup.find("div", {"class": "prw_rup prw_common_responsive_collapsible_text"})
    if d_data is None:
        description = " "

    else:
         description = soup.find(attrs={"class": 'prw_rup prw_common_responsive_collapsible_text'}).text.replace(',', ' ').replace('\n', '').strip()



    #get features
    f_data = soup.find("div", {"class": "sub_content ui_columns is-multiline is-gapless is-mobile"})
    if f_data is None:
       features = " "

    else:
         features = soup.find(attrs={"class": "sub_content ui_columns is-multiline is-gapless is-mobile"}).text.replace( ',', ' ').replace('\n', '|').strip()


    #get room type
    room_type = "Suites | Accessible rooms"

    #get price
    p_data = soup.find("div", {"class": "price"})
    if p_data is None:
        price = " "

    else:
        price = soup.find(attrs={"class": "price"}).text.replace(',', ' ').replace('\n', '').strip()


    #get price description
    pd_data = soup.find("span", {"class": "blOfferLink "})
    if pd_data is None:
        price_description = " "

    else:
        price_description = soup.find(attrs={"class": "blOfferLink "}).text.replace(',', ' ').replace('\n', '').strip()


    #get location
    l_data = soup.find("span", {"class": "detail"})
    if l_data is None:
        location = " "

    else:
        location = soup.find(attrs={"class": "detail"}).text.replace(',', ' ').replace('|', ' ').replace('\n','').strip()


    #get location description
    ld_data = soup.find("div", {"class": "nearbyListItem ui_icon flights"})
    if ld_data is None:
        location_description = " "

    else:
        location_description = soup.find(attrs={"class": "nearbyListItem ui_icon flights"}).text.replace('"', ' ').replace('\n','').strip()


    #get contact number
    c_data = soup.find("span", {"class": "is-hidden-mobile detail"})
    if c_data is None:
        contact_no = " "

    else:
        contact_no = soup.find(attrs={"class": "is-hidden-mobile detail"}).text.replace('"', ' ').replace('\n', '').strip()


    #get raing of the hotel
    r_data = soup.find("span", {"class": "overallRating"})
    if r_data is None:
        ratings = " "

    else:
        ratings = soup.find(attrs={"class": "overallRating"}).text.replace(',', ' ').replace('\n', '').strip()


    #get review of hotel
    rw_data = soup.find("div", {"class": "badgeText"})
    if rw_data is None:
        reviews = " "

    else:
        reviews = soup.find(attrs={"class": "badgeText"}).text.replace(',', ' ').replace('\n', '').strip()



    Record = hotel_name + "," + description + "," + features + "," + room_type + "," + price + "," + price_description + "," + location + "," + location_description + "," + contact_no + "," + ratings + "," + reviews
    file.write(bytes(Record, encoding="ascii", errors='ignore') + b"\n")

file.close()





