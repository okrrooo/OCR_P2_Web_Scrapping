# Importing the libraries
import requests
import csv
from bs4 import BeautifulSoup


def scrapping_book_information(url):

    # Make a Get request to fetch the raw HTML content
    html_content = requests.get(url).text

    # Parse the html content
    soup = BeautifulSoup(html_content, "html.parser")

    # for loop to collect '<tr>' elements from the product information
    for tr in soup.find_all("tr"):
        th = tr.find('th')
        td = tr.find('td')
        print(th.text, td.text)

    # print to extract book title
    title = soup.find("h1")
    print(title.text)

    # find the production description tag
    tag_product_description = soup.find('div', id='product_description')
    print(tag_product_description.text)

    # find paragraph description
    product_description = soup.find('div', id='product_description').findNextSibling().text
    print(product_description)

    # find product category
    category = soup.find('ul', class_='breadcrumb')
    category = category.find_all('li')[2]
    category = category.find('a', href=True)

    print(category.text)

    # print for the book's url

    print(url)

    # find the review rating
    review_rating = soup.find(class_='star-rating')

    print(review_rating['class'][1])

    # find image url

    image_url = soup.findAll('img', limit=1)
    for i in image_url:

        print('https://books.toscrape.com/' + i['src'])













scrapping_book_information('https://books.toscrape.com/catalogue/its-only-the-himalayas_981/index.html')





# info a extraire :
# product_page_url                          X
# universal_ product_code (upc)             X
# title                                     X
# price_including_tax                       X
# price_excluding_tax                       X
# number_available                          X
# product_description                       X
# category                                  X
# review_rating
# image_url                                 x