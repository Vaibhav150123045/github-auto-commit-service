To scrape headlines from Hacker News, we can use the `requests` and `BeautifulSoup` libraries in Python. Before you proceed, make sure you have these libraries installed. You can install them using pip:

```bash
pip install requests beautifulsoup4
```

Here is a simple Python script that scrapes headlines from the Hacker News front page:

```python
import requests
from bs4 import BeautifulSoup

def scrape_hacker_news():
    url = 'https://news.ycombinator.com/'
    response = requests.get(url)

    if response.status_code == 200:
        soup = BeautifulSoup(response.text, 'html.parser')
        # Find all the headline elements; in Hacker News, they are contained in <a> tags with the class 'storylink'
        headlines = soup.find_all('a', class_='storylink')

        # Print out the headlines
        for idx, headline in enumerate(headlines, start=1):
            print(f"{idx}. {headline.get_text()} - {headline['href']}")
    else:
        print(f"Failed to retrieve Hacker News: {response.status_code}")

if __name__ == "__main__":
    scrape_hacker_news()
```

### Explanation:
1. **Imports**: We import the necessary libraries: `requests` for making HTTP requests and `BeautifulSoup` from `bs4` for parsing HTML content.
2. **Function Definition**: We define the `scrape_hacker_news()` function to encapsulate our scraping logic.
3. **Make a Request**: We send a GET request to Hacker News and check if the request was successful (HTTP status code 200).
4. **Parse HTML**: We use BeautifulSoup to parse the HTML content from the response.
5. **Find Headlines**: We search for all anchor tags (`<a>`) with the class `storylink`, which contain the headlines.
6. **Output**: We loop through the found headlines, print the index and the headline text along with the link.
7. **Main Block**: The `if __name__ == "__main__":` block allows the script to be run directly.

### Run the Script
To run the script, save it to a file named `hacker_news_scraper.py` and execute it using:

```bash
python hacker_news_scraper.py
```

### Notes
- Make sure to abide by the terms of service for any website you scrape. If you plan to scrape frequently, consider adding delays to your requests to avoid overloading the server.
- The structure of the website may change over time, so if you find that the script stops working, you may need to adjust the selectors accordingly.