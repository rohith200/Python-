import requests

response = requests.get("https://api.github.com/repos/rohith200/Python-/pulls")
complete_file = response.json()

for i in range(len(complete_file)):
    print(complete_file[i]["user"]["login"])