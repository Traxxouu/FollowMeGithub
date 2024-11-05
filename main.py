import requests

#A remplacer
GITHUB_TOKEN = 'votre_token'

def get_github_data(endpoint):
    headers = {'sAuthorization': f'token {GITHUB_TOKEN}'}
    response = requests.get(f'https://api.github.com{endpoint}', headers=headers)
    response.raise_for_status()
    return response.json()

def main():
    followers = get_github_data('/user/followers')
    following = get_github_data('/user/following')
    
    followers_usernames = {user['login'] for user in followers}
    following_usernames = {user['login'] for user in following}
    
    not_following_back = following_usernames - followers_usernames
    
    print("Les utilisateurs que vous suivez mais qui ne vous suivent pas en retour :")
    for user in not_following_back:
        print(user)

if __name__ == "__main__":
    main()
