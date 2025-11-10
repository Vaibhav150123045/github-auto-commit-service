To scrape headlines from Hacker News, you can use the `requests` library to fetch the HTML content and the `BeautifulSoup` library from `bs4` to parse it. Below is a sample Python script that demonstrates how to do this:

```python
import requests
from bs4 import BeautifulSoup

def scrape_hacker_news():
    # URL of Hacker News
    url = 'https://news.ycombinator.com/'
    
    # Send a GET request to the website
    response = requests.get(url)
    
    # Check if the request was successful
    if response.status_code == 200:
        # Parse the HTML content using BeautifulSoup
        soup = BeautifulSoup(response.text, 'html.parser')
        
        # Find all the story titles
        headlines = soup.find_all('a', class_='storylink')
        
        # Extract the text from each headline
        for index, headline in enumerate(headlines, start=1):
            print(f"{index}: {headline.get_text()}")
    else:
        print(f"Failed to retrieve data. Status code: {response.status_code}")

if __name__ == '__main__':
    scrape_hacker_news()
```

### Instructions to Run the Script

1. **Install the Required Libraries**:
   Make sure you have `requests` and `beautifulsoup4` libraries installed. You can do this using pip:
   ```bash
   pip install requests beautifulsoup4
   ```

2. **Run the Script**:
   Save the script into a file named `scrape_hacker_news.py` and run it:
   ```bash
   python scrape_hacker_news.py
   ```

3. **Output**:
   The script will print the current headlines from Hacker News.

### Notes
- Make sure to follow the website's `robots.txt` and terms of service when scraping.
- This script simply fetches the titles and should be modified or expanded if you wish to collect more information (e.g., links to the articles).
- The structure of the website may change over time, which could break the scraping functionality. Adjust the selectors in the BeautifulSoup parsing logic as necessary.