Certainly! Below is a simple Python script that uses the `requests` library to fetch the HTML content from the Hacker News website and the `BeautifulSoup` library to parse the HTML and extract the headlines.

Before running the script, make sure you have installed the required libraries. You can do this using pip:

```bash
pip install requests beautifulsoup4
```

Here is the Python script:

```python
import requests
from bs4 import BeautifulSoup

def scrape_hacker_news_headlines():
    # URL of the Hacker News front page
    url = 'https://news.ycombinator.com/'

    # Send an HTTP GET request to the URL
    response = requests.get(url)
    # Check if the request was successful
    if response.status_code == 200:
        # Parse the HTML content using BeautifulSoup
        soup = BeautifulSoup(response.text, 'html.parser')
        
        # Find all the headline elements
        headlines = soup.find_all('a', class_='storylink')
        
        # Extract and print the headlines
        print("Hacker News Headlines:")
        for index, headline in enumerate(headlines, start=1):
            print(f"{index}. {headline.get_text()}")
    else:
        print(f"Failed to retrieve news. Status code: {response.status_code}")

if __name__ == '__main__':
    scrape_hacker_news_headlines()
```

### How to Run the Script

1. Make sure you have Python installed on your machine (Python 3.x is recommended).
2. Save the script in a file named `hacker_news_scraper.py`.
3. Run the script using the command:

    ```bash
    python hacker_news_scraper.py
    ```

### Output

The script will print a list of the current headlines from Hacker News to the console.

### Note

- Be mindful of web scraping policies. Always check the website’s `robots.txt` file and terms of service to ensure you are allowed to scrape it.
- Hacker News is constantly updating, so the output may change every time you run the script.