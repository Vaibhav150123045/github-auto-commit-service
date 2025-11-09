import os
from openai import OpenAI
import git
from dotenv import load_dotenv
import datetime

# Load environment variables
load_dotenv()

# Initialize OpenAI client
client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))
REPO_PATH = os.getenv("REPO_PATH")


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
    repo = git.Repo(REPO_PATH)
    repo.git.add(file)
    repo.index.commit(f"Auto commit {file}")
    origin = repo.remote(name="origin")
    origin.push()


if __name__ == "__main__":
    file = fetch_gpt_code()
    git_push(file)
    print(f"✅ {file} pushed to GitHub!")
