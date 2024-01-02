import requests

url = "https://api.chucknorris.io/jokes/random"
response = requests.get(url)

if response.status_code == 200:
    data = response.json()
    joke = data['value']
    print("Random Chuck Norris joke:")
    print(joke)
else:
    print("Error.")

