import requests
from bs4 import BeautifulSoup

#URL of the webpage to scrape
url='https://www.geeksforgeeks.org/what-is-web-scraping-and-how-to-use-it/' #Replace with the URL of the web page you want to scrape

# Send a GET request to the web page 
response = requests.get(url)

# Check if the request was successful
if response.status_code == 200:
    # parse the HTML content of the page
    soup = BeautifulSoup(response.text, 'html.parser')

    # Extract all the text from the page
    page_text = soup.get_text()

    # Extract all the links from the page 
    links = [a['href'] for a in soup.find_all('a',href=True)]

    # Extract all the images from the page 
    images = [img['src'] for img in soup.find_all('img', src=True)]

    # Print the extracted data
    print("Page Text:")
    print(page_text)

    print("\nLinks:")
    for link in links:
        print(link)

    print("\nImages:")
    for image in images:
        print(image)
else:
    print(f"Faileed to retrieve the web page. Status code:{response.status_code}")        

