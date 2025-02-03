import requests, json

url = "https://api.chucknorris.io/jokes/random"
response = requests.get(url)
response_json = response.json()

with open(r"6ICT_PROG_2024_2025\hfst_4 API\oefenmee\chucknorris_data.json", "w") as fp:
    # json.dump(response_json, fp)
    print("Data gedumpt!")
