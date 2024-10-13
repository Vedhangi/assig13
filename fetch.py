import requests


repo_owner = "Vedhangi"
repo_name = "assig13"


url = f"https://api.github.com/repos/Vedhangi/assig13/contributors"

response = requests.get(url)  # , headers=headers if token provided


if response.status_code == 200:
    contributors = response.json()
    
   
    for contributor in contributors:
        print(f"Username: {contributor['login']}")
       
        # typically you'd fetch the full name from a user's profile if needed
        print(f"Contributions: {contributor['contributions']}")
else:
    print(f"Failed to fetch contributors. Status code: {response.status_code}")
