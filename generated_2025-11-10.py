You can scrape headlines from Hacker News using the `requests` library to fetch the web page and `BeautifulSoup` from the `bs4` library to parse the HTML. Below is a simple Python script that does exactly that. Before running the script, make sure you have both libraries installed. You can install them using pip:

```bash
pip install requests beautifulsoup4
```

Here's the script:

```python
import requests
from bs4 import BeautifulSoup

def scrape_hacker_news():
    url = 'https://news.ycombinator.com/'
    response = requests.get(url)

    if response.status_code == 200:
        # Parse the HTML content
        soup = BeautifulSoup(response.text, 'html.parser')
        
        # Find all the story links on the page
        stories = soup.find_all('a', class_='storylink')

        headlines = []
        for story in stories:
            title = story.get_text()
            link = story['href']
            headlines.append((title, link))

        return headlines
    else:
        print(f'Failed to retrieve news: {response.status_code}')
        return []

if __name__ == '__main__':
    headlines = scrape_hacker_news()
    print("Hacker News Headlines:")
    for title, link in headlines:
        print(f'{title} - {link}')
```

### How to Run the Script

1. Copy the code above and save it to a file named `scrape_hacker_news.py`.
2. Ensure you have Python installed on your machine.
3. Open your terminal (Command Prompt, PowerShell, or a terminal session).
4. Navigate to the directory where the `scrape_hacker_news.py` file is saved.
5. Run the script using the command:

   ```bash
   python scrape_hacker_news.py
   ```

### What the Script Does
- It makes an HTTP GET request to the Hacker News homepage.
- It checks the response status to ensure the page was retrieved successfully (HTTP status code 200).
- It parses the HTML to extract the headlines (title and link) of the stories.
- It prints the headlines and their corresponding links in a readable format.

### Note
- Be mindful of Hacker News' crawling policies and avoid making frequent requests to their server.
- For larger-scale scraping, consider using scraping libraries like `Scrapy`, which manage requests and data extraction more robustly.