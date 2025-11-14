Scraping websites can be accomplished using libraries such as `requests` and `BeautifulSoup` in Python. Below is a simple Python script that scrapes the headlines from the Hacker News homepage.

Make sure you have the required libraries installed. You can install them via pip if you haven't done so already:

```sh
pip install requests beautifulsoup4
```

Here's a sample script to scrape headlines from Hacker News:

```python
import requests
from bs4 import BeautifulSoup

def scrape_hacker_news():
    # URL of Hacker News
    url = 'https://news.ycombinator.com/'

    # Send a GET request to the Hacker News page
    response = requests.get(url)

    # Check if the request was successful
    if response.status_code == 200:
        # Parse the HTML content of the page
        soup = BeautifulSoup(response.text, 'html.parser')

        # Find all the story links in the page
        headlines = []
        for item in soup.select('.storylink'):
            headlines.append(item.get_text())
        
        return headlines
    else:
        print(f"Failed to retrieve Hacker News. Status code: {response.status_code}")
        return []

if __name__ == '__main__':
    headlines = scrape_hacker_news()
    if headlines:
        print("Hacker News Headlines:")
        for index, headline in enumerate(headlines, start=1):
            print(f"{index}. {headline}")
```

### Explanation:

1. **Import Libraries**: The script imports `requests` for sending HTTP requests and `BeautifulSoup` from `bs4` for parsing HTML content.

2. **Function Definition**: The `scrape_hacker_news` function is defined to encapsulate the scraping logic.

3. **GET Request**: A GET request is made to Hacker News using `requests.get()`. The response is checked for a successful HTTP status.

4. **Parsing Content**: If the request is successful (`status_code` 200), the content is parsed using BeautifulSoup.

5. **Extracting Headlines**: The script searches for all elements with the class `storylink`, which contains the headlines, and collects the text of those elements.

6. **Output**: Finally, the headlines are printed to the console.

### Running the Script
To run the script, save it to a file, for example `hacker_news_scraper.py`, and execute it using Python:

```sh
python hacker_news_scraper.py
```

This will fetch and print the headlines from Hacker News to your console.

### Note
- Always be considerate when scraping websites; they have terms of service concerning bots and scrapers. This script is designed for educational purposes, so use it responsibly.
- The structure of the site can change, which may break the script. Adjust your selectors based on the current website structure if necessary.