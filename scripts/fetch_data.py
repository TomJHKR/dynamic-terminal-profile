import requests
import json
import pprint
import config

def fetch_github_stats(username):
    url = f"https://api.github.com/users/{username}"
    headers = {'User-Agent': 'request'}
    response = requests.get(url, headers=headers)
    if response.status_code == 200:
        return response.json()
    else:
        raise Exception(f"Error fetching data: {response.status_code}")

def fetch_github_repositories(username):
    url = f"https://api.github.com/users/{username}/repos"
    headers = {'User-Agent': 'request'}
    response = requests.get(url, headers=headers)
    if response.status_code == 200:
        return {"repos":[repo["name"] for repo in response.json()]}
    else:
        raise Exception(f"Error fetching repositories: {response.status_code}")

def fetch_repository_languages(username, repository):
    url = f"https://api.github.com/repos/{username}/{repository}/languages"
    headers = {'User-Agent': 'request'}
    response = requests.get(url, headers=headers)
    if response.status_code == 200:
        return response.json()
    else:
        raise Exception(f"Error fetching languages for {repository}: {response.status_code}")

def calculate_language_percentages(languages):
    # Filter out the excluded languages
    filtered_languages = {language: bytes for language, bytes in languages.items() if language not in config.EXCLUDED_LANGS}
    total_bytes = sum(filtered_languages.values())
    language_percentages = {
        language: round((bytes / total_bytes) * 100, 2)
        for language, bytes in filtered_languages.items()
    }
    return language_percentages

def calculate_total_language_percentages(all_repo_languages):
    total_languages = {}
    total_bytes = 0
    
    # Aggregate the bytes across all repositories
    for repo_languages in all_repo_languages.values():
        for language, percentage in repo_languages.items():
            total_languages[language] = total_languages.get(language, 0) + percentage
            total_bytes += percentage
    
    # Calculate the overall percentage for each language
    total_language_percentages = {
        language: round((bytes / total_bytes) * 100, 2)
        for language, bytes in total_languages.items()
    }
    
    return total_language_percentages

if __name__ == "__main__":
    username = "TomJHKR"
    data = fetch_github_repositories(username)
    repos_stats = {}

    for repo in data["repos"]:
        print(repo)
        languages = fetch_repository_languages(username, repo)
        # Calculate language percentages
        language_percentages = calculate_language_percentages(languages)
        repos_stats[repo] = language_percentages
    print(language_percentages)
     # Calculate total language percentages across all repositories
    total_language_percentages = calculate_total_language_percentages(repos_stats)

    total_data = {
            "repository_stats" : data,
            "total_language_percentages": total_language_percentages
    }
    with open("data/stats.json", "w") as file:
        json.dump(total_data, file)

