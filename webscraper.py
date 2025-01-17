from bs4 import BeautifulSoup
import requests
import pandas as pd
import csv
import json

def scrape_website(url, output_format='csv'):
    try:
        # Fetch the webpage
        response = requests.get(url)
        response.raise_for_status()
        soup = BeautifulSoup(response.text, 'html.parser')

        # Extract headlines and links as an example
        data = []
        for item in soup.find_all('h2'):
            title = item.get_text(strip=True)
            link = item.find('a')['href'] if item.find('a') else 'No link'
            data.append({'title': title, 'link': link})

        # Save to file
        if output_format == 'csv':
            with open('scraped_data.csv', 'w', newline='') as file:
                writer = csv.DictWriter(file, fieldnames=['title', 'link'])
                writer.writeheader()
                writer.writerows(data)
        elif output_format == 'json':
            with open('scraped_data.json', 'w') as file:
                json.dump(data, file, indent=4)

        print(f"Data successfully saved to scraped_data.{output_format}")
    except Exception as e:
        print(f"Error: {e}")

# Example usage
url = input("Enter the URL to scrape: ")
output_format = input("Enter output format (csv/json): ")
scrape_website(url, output_format)
