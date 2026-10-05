import requests
url = "https://jsonplaceholder.typicode.com/posts"
response = requests.get(url)
print("Status:", response.status_code)
print("Number of posts:", len(response.json()))
print("First Title:", response.json()[0]['title'])
print("Second Title:", response.json()[1]['title'])