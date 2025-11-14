Certainly! To create a Python script that scrapes headlines from Hacker News, we can use the `requests` library to fetch the page content and the `BeautifulSoup` library to parse the HTML.

First, make sure that you have the necessary libraries installed. You can install them using pip if you don't have them yet:

```bash
pip install requests beautifulsoup4
```

Here’s a simple script that scrapes the headlines from the front page of Hacker News:

```python
import requests
from bs4 import BeautifulSoup

def fetch_hn_headlines():
    # URL for Hacker News front page
    url = 'https://news.ycombinator.com/'
    
    # Send a GET request to the URL
    response = requests.get(url)
    
    # Check if the request was successful
    if response.status_code == 200:
        # Parse the page content
        soup = BeautifulSoup(response.text, 'html.parser')
        
        # Find all articles
        titles = soup.find_all('a', class_='storylink')
        
        # Print the headlines and their URLs
        headlines = []
        for title in titles:
            headlines.append({
                'headline': title.text,
                'url': title['href']
            })
        
        return headlines
    else:
        print(f"Failed to retrieve content: {response.status_code}")
        return []

if __name__ == "__main__":
    headlines = fetch_hn_headlines()
    if headlines:
        print("Hacker News Headlines:")
        for idx, headline in enumerate(headlines, start=1):
            print(f"{idx}. {headline['headline']} ({headline['url']})")
```

### How the Script Works

1. **Requests Module**: It sends an HTTP GET request to the Hacker News front page.

2. **BeautifulSoup**: It parses the HTML response to extract the headlines. It specifically looks for all `<a>` tags with a class of `storylink`, which is the class used for the news story links.

3. **Storing Headlines**: It collects the text and URL of each headline into a list of dictionaries.

4. **Output**: Finally, it prints each headline with its corresponding URL.

### Running the Script

Save the script in a file named `hn_scraper.py` and run it:

```bash
python hn_scraper.py
```

### Note

When scraping websites, always ensure you respect the site's `robots.txt` and terms of service. Use scraping responsibly and avoid sending too many requests in a short period.