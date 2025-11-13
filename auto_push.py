import os
from openai import OpenAI
from dotenv import load_dotenv
import datetime
import subprocess
import constants

# Load environment variables
load_dotenv()

# Initialize OpenAI client
client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))
REPO_PATH = constants.REPO_PATH


def fetch_gpt_code():
    prompt = "Generate a Python script that scrapes headlines from Hacker News."

    # Call the GPT-4o-mini model
    response = client.chat.completions.create(
        model="gpt-4o-mini",
        messages=[{"role": "user", "content": prompt}],
    )

    # Extract the code text
    code = response.choices[0].message.content

    # Save to a file
    filename = f"generated_{datetime.date.today()}.py"
    filepath = os.path.join(REPO_PATH, filename)
    with open(filepath, "w", encoding="utf-8") as f:
        f.write(code)

    return filename


def git_push(file):
    # This assumes your repo is already checked out
    if not os.getenv("GITHUB_TOKEN"):
        print("❌ GITHUB_TOKEN not found")
    else:
        print("✅ GITHUB_TOKEN is available")
    GITHUB_TOKEN = os.getenv("GITHUB_TOKEN")
    print(GITHUB_TOKEN)

    # replace with your repo
    REPO = "github.com/Vaibhav150123045/github-auto-commit-service.git"

    # Configure git
    subprocess.run(["git", "config", "--global",
                   "user.name", "Vaibhav Motwani"])
    subprocess.run(["git", "config", "--global",
                   "user.email", "motwani777@gmail.com"])

    # Commit changes
    subprocess.run(["git", "add", "."])
    subprocess.run(
        ["git", "commit", "-m", "Auto commit by GitHub Action"], check=False)

    # Push using token authentication
    subprocess.run(
        ["git", "push", f"https://x-access-token:{GITHUB_TOKEN}@{REPO}", "main"])


if __name__ == "__main__":
    file = fetch_gpt_code()
    git_push(file)
    print(f"✅ {file} pushed to GitHub!")
