from pip._vendor import requests



req_url = "http://www.memrise.com/api/user/get/?username="
print(requests.get(req_url))
# req_json = requests.get(req_url).json()
# print(req_json)