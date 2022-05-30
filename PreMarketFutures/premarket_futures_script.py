from bs4 import BeautifulSoup
from urllib.request import urlopen as uReq 
import pandas as pd
from pretty_html_table import build_table
from email_script import send_mail

page_url = "https://markets.businessinsider.com/premarket"
uClient = uReq(page_url)
page_source_code = uClient.read()
uClient.close()

page_soup = BeautifulSoup(page_source_code, "html.parser")
futures_classes = page_soup.findAll("div", {"class": "markets-now__values"})

order_of_futures = ["DOW Futures", "S & P 500 Futures", "Nasdaq Futures", "Gold Futures", "Crude Oil Futures", "EUR/USD"]
form_json = []

i = 0
for futures_fetch in futures_classes:
    all_divs = futures_fetch.findAll('div')
    percent_value = all_divs[0].text
    change_value = all_divs[1].text
    current_value = all_divs[2].text

    form_json.append({'Commodity': order_of_futures[i], 'Current_value' : current_value, 'Change_value' : change_value, 'Percent_Value': percent_value})
    i += 1

tabular_panda = pd.json_normalize(form_json)
output = build_table(tabular_panda, 'blue_light')
send_mail(output)

print("E-Mail sent successfully.")


  
    