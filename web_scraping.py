# Web scraping with Python

# Import libraries
import requests
from bs4 import BeautifulSoup
import csv

# Define the URL to scrape
url = "https://www.bbc.com/news"

# Get the HTML content of the page
response = requests.get(url)
html = response.text

# Parse the HTML with BeautifulSoup
soup = BeautifulSoup(html, "html.parser")

# Find all the headlines and links
headlines = soup.find_all("h3", class_="gs-c-promo-heading__title")
links = soup.find_all("a", class_="gs-c-promo-heading")

# Create a list of tuples with headline and link
data = []
for headline, link in zip(headlines, links):
    title = headline.text.strip()
    url = link["href"]
    if not url.startswith("http"):
        url = "https://www.bbc.com" + url
    data.append((title, url))

# Write the data to a CSV file
with open("news.csv", "w", newline="", encoding="utf-8") as f:
    writer = csv.writer(f)
    writer.writerow(["Title", "URL"])
    writer.writerows(data)

# Print a message
print("Web scraping done. Check the news.csv file.")
