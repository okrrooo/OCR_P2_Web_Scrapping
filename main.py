# Importing the libraries
import requests
import csv
from bs4 import BeautifulSoup

filename = "information.csv"
csv_writer = csv.writer(open(filename, 'w', encoding="utf-8"))


def scrapping_book_information(url):

    # where all the data will be listed
    headers = []
    info = []

    # Make a Get request to fetch the raw HTML content
    html_content = requests.get(url).text

    # Parse the html content
    soup = BeautifulSoup(html_content, "html.parser")

    # for loop to collect '<tr>' elements from the product information
    for tr in soup.find_all("tr"):
        th = tr.find('th')
        td = tr.find('td')
        headers.append(th.text)
        info.append(td.text)

    # extract book title
    title = soup.find("h1")
    info.append(title.text)
    headers.append('Title')

    # find the production description tag
    tag_product_description = soup.find('div', id='product_description')
    headers.append(tag_product_description.text)

    # find paragraph description
    product_description = soup.find('div', id='product_description').findNextSibling().text
    info.append(product_description)

    # find product category
    category = soup.find('ul', class_='breadcrumb')
    category = category.find_all('li')[2]
    category = category.find('a', href=True)
    headers.append('Product Category')
    info.append(category.text)

    # find the url of the product
    headers.append('url')
    info.append(url)

    # find the review rating
    review_rating = soup.find(class_='star-rating')
    rating = (review_rating['class'][1])
    headers.append('Review rating out of 5')
    info.append(rating)

    # find image url

    image_url = soup.findAll('img', limit=1)
    for i in image_url:

        result = ('https://books.toscrape.com/' + i['src'])
        headers.append('image_url')
        info.append(result)

    csv_writer.writerow(headers)
    csv_writer.writerow(info)


scrapping_book_information('https://books.toscrape.com/catalogue/its-only-the-himalayas_981/index.html')

