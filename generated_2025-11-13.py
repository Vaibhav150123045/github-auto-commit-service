Certainly! Below is a Python script that uses the `requests` and `BeautifulSoup` libraries to scrape the top headlines from the Hacker News website.

Before running the script, make sure you have the `requests` and `beautifulsoup4` libraries installed. You can install them using pip if you haven't already:

```bash
pip install requests beautifulsoup4
```

Here's the script:

```python
import requests
from bs4 import BeautifulSoup

def scrape_hacker_news():
    # URL of Hacker News
    url = 'https://news.ycombinator.com/'
    
    # Sending a request to the website
    response = requests.get(url)
    
    if response.status_code == 200:
        # Parse the HTML content
        soup = BeautifulSoup(response.text, 'html.parser')
        
        # Find all the headline elements
        headlines = soup.find_all('a', class_='storylink')
        
        # Print the headlines
        print("Top Hacker News Headlines:\n")
        for i, headline in enumerate(headlines, start=1):
            print(f"{i}. {headline.text} ({headline['href']})")
    else:
        print("Failed to retrieve the page")

if __name__ == '__main__':
    scrape_hacker_news()
```

### How It Works
1. The script sends an HTTP GET request to the Hacker News homepage.
2. It checks the response status to ensure the request was successful.
3. It uses BeautifulSoup to parse the HTML content of the page.
4. It locates headline elements by their class (`storylink`).
5. Finally, it prints out each headline along with its corresponding link.

### Running the Script
- Save the script to a file, for example, `hacker_news_scraper.py`.
- Open your terminal and navigate to the directory where you saved the file.
- Run the script using Python:

```bash
python hacker_news_scraper.py
```

You should see the top headlines from Hacker News printed in your terminal.

### Note
Web scraping should be done responsibly. Please check the terms of service of the website before scraping, and ensure you’re not overwhelming the server with requests. This script fetches the data in a single request, which is a good practice for low-impact scraping.