
import pprint
import requests


# url = 'http://185.185.143.231:5051/v1/account'
# headers = {
#     'accept': '*/*',
#     'Content-Type': 'application/json'
# }
# json = {
#     "login": "katya_test",
#     "email": "katya_test@mail.ru",
#     "password": "123456"
# }
#
# response = requests.post(
#     url=url,
#     headers=headers,
#     json=json
# )



# curl -X 'PUT' \
#   'http://185.185.143.231:5051/v1/account/5dd75b4e-808b-473d-bf32-834583d113b2' \
#   -H 'accept: text/plain'

url = 'http://185.185.143.231:5051/v1/account/5dd75b4e-808b-473d-bf32-834583d113b2'
headers = {
    'accept': 'text/plain'
}

response = requests.put(
    url=url,
    headers=headers
)

print(response.status_code)
pprint.pprint(response.json())
response_json = response.json()
print(response_json['resource']['rating']['quantity'])