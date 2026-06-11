from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
import pandas as pd
import time

driver = webdriver.Chrome(
    service=Service(ChromeDriverManager().install())
)

driver.get("https://coinmarketcap.com")

time.sleep(15)

rows = driver.find_elements("xpath", "//tbody/tr")

data = []

for row in rows[:10]:
    cols = row.find_elements("tag name", "td")

    coin = cols[2].text
    price = cols[3].text
    change_24h = cols[4].text
    market_cap = cols[7].text

    data.append([coin, price, change_24h, market_cap])

df = pd.DataFrame(
    data,
    columns=["Coin Name", "Price", "24h Change", "Market Cap"]
)

df.to_csv("crypto_prices.csv", index=False)

print("Data saved successfully!")

driver.quit()