import requests

url = "https://api.pwnedpasswords.com/range/"+ "password"
 request = requests.get(url)

 print(request)