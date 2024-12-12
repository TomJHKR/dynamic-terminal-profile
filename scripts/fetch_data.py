import requests

def fetch_github_stats(username):
    url = f"https://api.github.com/users/{username}"
    response = requests.get(url)
    if response.status_code == 200:
        return response.json()
    else:
        raise Exception(f"Error fetching data: {response.status_code}")

if __name__ == "__main__":
    username = "TomJHKR"
    data = fetch_github_stats(username)
    with open("data/stats.json", "w") as file:
        json.dump(data, file)

