# Author Murtadha Marzouq
# Desc: This program is fetching data from a weather service and extracting the data and formatting it
import requests
from bs4 import BeautifulSoup
import pandas as pd

# Fetching the webpages
page = requests.get("https://forecast.weather.gov/MapClick.php?lat=37.7772&lon=-122.4168");

# Starting the parsing process using B.S
soup = BeautifulSoup(page.content, 'html.parser')
seven_day = soup.find(id="seven-day-forecast")
# GET THE WEEK's DATA
forecast_items = seven_day.find_all(class_="tombstone-container")

# ASSIGNING THE VARIABLES TO BE USED BY THE PD
seven_day = soup.find(id="seven-day-forecast")
period_tags = seven_day.select(".tombstone-container .period-name")
periods = [pt.get_text() for pt in period_tags]
short_descs = [sd.get_text() for sd in seven_day.select(".tombstone-container .short-desc")]
temps = [t.get_text() for t in seven_day.select(".tombstone-container .temp")]
descs = [d["title"] for d in seven_day.select(".tombstone-container img")]

# Creating THE TABLE AND FORMATTING IT
weather = pd.DataFrame({
    "desc": descs,
    "period": periods,
    "short_desc": short_descs,
    "temp": temps,

})
# to format the view to show all the columns
pd.set_option('display.max_rows', 500)
pd.set_option('display.max_columns', 500)
pd.set_option('display.width', 1000)

temp_nums = weather["temp"].str.extract('(\d+)')
weather["temp_num"] = temp_nums
is_night = weather["temp"].str.contains("Low")
weather["is_night"] = is_night

# PRINTING THE TABLE
print(weather)

# THE OUTPUT MATCHES THE ARTICLE'S
