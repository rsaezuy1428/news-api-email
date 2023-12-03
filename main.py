import requests

from send_email import send_email

topic = "Amazon"
country = "us"
category = "business"
api_key = "0251d59d30084966987c3833adf218b6"
url = "https://newsapi.org/v2/top-headlines?" \
    f"country={country}&" \
    f"category={category}&" \
    f"topic={topic}&" \
    f"apiKey={api_key}&" \
    "language=en"

request = requests.get(url)

content = request.json()

subject = "Subject: Today's news" + "\n"
body = ""
for article in content['articles'][:10]:
    if article['title'] is not None and article['description'] is not None:
        body = body + article['title'] + "\n" + article['description'] + "\n" + article['url'] + 2*"\n"

send_email(subject.encode('utf-8') + body.encode('utf-8'))
