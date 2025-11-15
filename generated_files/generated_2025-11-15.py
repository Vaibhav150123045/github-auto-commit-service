Certainly! Below is a simple Python script that uses the `requests` and `BeautifulSoup` libraries to scrape headlines from Hacker News:

```python
import requests
from bs4 import BeautifulSoup

def scrape_hacker_news():
    # URL of the Hacker News main page
    url = 'https://news.ycombinator.com/'

    # Send a request to the webpage
    response = requests.get(url)

    # Check if the request was successful
    if response.status_code == 200:
        # Parse the HTML content
        soup = BeautifulSoup(response.text, 'html.parser')

        # Find all the headlines
        headlines = soup.find_all('a', class_='storylink')

        # Print each headline
        for index, headline in enumerate(headlines):
            print(f"{index + 1}: {headline.get_text()} (Link: {headline['href']})")
    else:
        print(f"Failed to retrieve data from Hacker News. Status code: {response.status_code}")

if __name__ == "__main__":
    scrape_hacker_news()
```

### Requirements
Before running the script, ensure you have the following Python packages installed:

1. `requests`
2. `beautifulsoup4`

You can install them using pip:

```bash
pip install requests beautifulsoup4
```

### Running the Script
1. Save the script in a file named, for instance, `hackers_news_scraper.py`.
2. Run the script using Python:

```bash
python hackers_news_scraper.py
```

### Output
The script prints the list of the top headlines from Hacker News along with their links.

### Note
- Be sure to abide by Hacker News' [Terms of Service](https://news.ycombinator.com/newsfaq.html) when scraping their content.
- If you plan to scrape the site frequently, consider implementing polite scraping practices, such as adding delays between requests and making sure not to overload their servers.