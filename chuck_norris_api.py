import requests
ENDPOINT = 'https://api.chucknorris.io/jokes/random'
response = requests.get(f'{ENDPOINT}').json()
joke = response['value']

answer = input("Want to hear a Chuck Norris joke? ")
if answer == 'y':
  print(joke)