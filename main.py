import requests

from send_email import send_email

url = "https://newsapi.org/v2/everything?q=tesla&from=2023-11-03&sortBy=publishedAt&apiKey=0251d59d30084966987c3833adf218b6"

request = requests.get(url)

content = request.json()

send_email(content['articles'][0]['title'].encode('utf-8'))
