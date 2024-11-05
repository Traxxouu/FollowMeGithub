# GitHub Follower Check Script

This Python script allows you to check which GitHub users you follow but who do not follow you back. It utilizes the GitHub API to retrieve follower and following data for your account.

## How It Works

The script:
1. Retrieves the list of users you follow.
2. Retrieves the list of users who follow you.
3. Compares both lists to identify users who do not follow you back.
4. Displays the usernames of those users.

## Prerequisites

Before using this script, ensure you have:
- Python 3.x installed.
- A personal access token (PAT) from GitHub with the necessary permissions.

## Setup

1. **Clone the repository**:
   ```bash
   git clone https://github.com/your-username/your-repo-name.git
   cd your-repo-name## Install Required Libraries
   ```

2. The script uses the `requests` library. If not already installed, you can install it via:

    ```bash
    pip install requests
    ```

## Set Up Your GitHub Token

1. Open the `main.py` file.
2. Replace `votre_token` in `GITHUB_TOKEN = 'votre_token'` with your actual GitHub personal access token.

## Usage

Run the script using Python:

```bash
python main.py
```

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

