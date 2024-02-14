# Objective:
#   - Make https request on an url

url = "https://codeavecjonathan.com/scraping/recette"

# step:
#   --> import requests librairi python
#   --> Use get method of request to getting response

import requests as rq

answer = rq.get(url)
