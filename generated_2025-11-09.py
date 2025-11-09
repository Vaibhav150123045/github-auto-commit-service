Certainly! Below is a simple Python script that uses the `requests` and `BeautifulSoup` libraries to scrape the latest headlines from Hacker News.

Make sure you have both libraries installed. You can install them using pip if you haven't done so:

```bash
pip install requests beautifulsoup4
```

Here is the script:

```python
import requests
from bs4 import BeautifulSoup

def scrape_hacker_news():
    # URL of Hacker News
    url = 'https://news.ycombinator.com/'
    
    # Send a GET request to the Hacker News homepage
    response = requests.get(url)
    
    # Check if the request was successful
    if response.status_code == 200:
        # Parse the page content
        soup = BeautifulSoup(response.text, 'html.parser')
        
        # Find all the article titles
        headlines = soup.find_all('a', class_='storylink')
        
        # Print out the headlines
        for index, headline in enumerate(headlines):
            print(f"{index + 1}. {headline.text}")
    else:
        print(f"Failed to retrieve page: {response.status_code}")

if __name__ == '__main__':
    scrape_hacker_news()
```

### How It Works:
1. **Send a Request**: The script sends a HTTP GET request to the Hacker News homepage.
2. **Parse the Content**: It uses `BeautifulSoup` to parse the HTML content of the response.
3. **Find Headlines**: The script searches for all links that contain the class `storylink`, which corresponds to the article headlines.
4. **Print the Headlines**: Finally, it enumerates through the headlines and prints them.

### Running the Script:
1. Save the script to a file, for instance, `hacker_news_scraper.py`.
2. Run the script from the command line:

```bash
python hacker_news_scraper.py
```

### Note:
- Always be polite when scraping websites. Check their `robots.txt` file and terms of service to ensure you're allowed to scrape their content.
- This script will output the latest headlines on the Hacker News front page at the time of execution.