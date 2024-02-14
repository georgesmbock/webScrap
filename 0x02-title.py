# Objective:
#   --> recover title

# Import beautifulsoup librairi

from bs4 import BeautifulSoup as bs

html = " answer.text"
soup = bs(html,  "html.parser")

title = soup.find("h1").text