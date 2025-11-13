Certainly! Below is a simple Python script that scrapes the headlines from the Hacker News website using the `requests` library to fetch the page content and the `BeautifulSoup` library to parse the HTML. Make sure you have both libraries installed. You can install them using pip if you don't have them yet:

```bash
pip install requests beautifulsoup4
```

Here's the Python script:

```python
import requests
from bs4 import BeautifulSoup

# Function to scrape Hacker News headlines
def scrape_hacker_news():
    # URL for Hacker News
    url = 'https://news.ycombinator.com/'
    
    # Send a GET request to the Hacker News URL
    response = requests.get(url)
    
    # Check if the request was successful
    if response.status_code == 200:
        # Parse the webpage content with BeautifulSoup
        soup = BeautifulSoup(response.text, 'html.parser')
        
        # Find all the article titles
        titles = soup.select('.storylink')

        # Print the headlines
        print("Hacker News Headlines:")
        for idx, title in enumerate(titles, start=1):
            print(f"{idx}. {title.get_text()} ({title['href']})")
    else:
        print(f"Failed to retrieve Hacker News. Status code: {response.status_code}")

# Call the function to scrape the headlines
if __name__ == "__main__":
    scrape_hacker_news()
```

### How to Run the Script

1. **Save the script** to a file named `hacker_news_scraper.py`.

2. **Run the script** using Python:

   ```bash
   python hacker_news_scraper.py
   ```

### What the Script Does

- It sends a GET request to the Hacker News homepage.
- If the request is successful, it parses the HTML using BeautifulSoup.
- It selects elements with the CSS class `storylink`, which corresponds to the headlines of the articles.
- It prints each headline along with its link in a numbered list.

### Note

- Scraping websites may be against their terms of service; you should check Hacker News' terms and scrape responsibly.
- The structure of websites may change over time, so this script might require updates if Hacker News changes its HTML layout.