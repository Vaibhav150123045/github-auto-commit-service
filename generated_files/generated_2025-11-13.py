To scrape headlines from Hacker News, we can use Python along with the BeautifulSoup and Requests libraries. Below is a Python script that accomplishes this task:

```python
import requests
from bs4 import BeautifulSoup

def scrape_hacker_news():
    # URL of Hacker News
    url = 'https://news.ycombinator.com/'

    # Send a GET request to the Hacker News website
    response = requests.get(url)

    # Check if the request was successful
    if response.status_code == 200:
        # Parse the HTML content using BeautifulSoup
        soup = BeautifulSoup(response.text, 'html.parser')

        # Find all the titles on the page
        titles = soup.select('.storylink')
        
        # Print the headlines
        for index, title in enumerate(titles, start=1):
            print(f"{index}. {title.get_text()}")

    else:
        print(f"Failed to retrieve the page. Status code: {response.status_code}")

if __name__ == "__main__":
    scrape_hacker_news()
```

### Instructions:

1. **Install Required Libraries:**
   You need to have `requests` and `beautifulsoup4` installed. You can install them using pip:

   ```bash
   pip install requests beautifulsoup4
   ```

2. **Run the Script:**
   Save the script in a file named `hacker_news_scraper.py` and execute it:

   ```bash
   python hacker_news_scraper.py
   ```

### Explanation of the Code:

- **requests.get(url)**: Sends a GET request to the specified URL and retrieves the HTML content of the page.
- **BeautifulSoup**: Parses the HTML content. We use the 'html.parser' to interpret the HTML file.
- **soup.select('.storylink')**: Selects all elements with the class `storylink`, which contains the headlines of the articles.
- The script prints each headline along with its index.

This will give you a simple console output of the latest headlines from Hacker News. You can modify or extend the script for additional features, such as saving the headlines to a file or filtering them based on certain criteria.