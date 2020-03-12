import requests

page = requests.get('https://www.bbc.co.uk/news')

print(page.content)
