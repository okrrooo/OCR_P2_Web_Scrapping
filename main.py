# Importing the libraries
import requests
import csv
from bs4 import BeautifulSoup
import urllib.parse

filename = "information.csv"
csv_writer = csv.writer(open(filename, 'w+', newline='', encoding="utf-8"))


def scrapping_book_information(url):

    # where all the csv data will be listed
    row1 = []
    row2 = []

    # Make a Get request to fetch the raw HTML content
    html_content = requests.get(url).text

    # Parse the html content
    soup = BeautifulSoup(html_content, "html.parser")

    # for loop to collect '<tr>' elements from the product information
    for tr in soup.find_all("tr"):
        th = tr.find('th')
        td = tr.find('td')
        row1.append(th.text)
        row2.append(td.text)

    # extract book title
    title = soup.find("h1")
    row2.append(title.text)
    row1.append('Title')

    # find the production description tag
    tag_product_description = soup.find('div', id='product_description')
    row1.append(tag_product_description.text)

    # find paragraph description
    product_description = soup.find('div', id='product_description').findNextSibling().text
    row2.append(product_description)

    # find product category
    category = soup.find('ul', class_='breadcrumb')
    category = category.find_all('li')[2]
    category = category.find('a', href=True)
    row1.append('Product Category')
    row2.append(category.text)

    # find the url of the product
    row1.append('url')
    row2.append(url)

    # find the review rating
    review_rating = soup.find(class_='star-rating')
    rating = (review_rating['class'][1])
    row1.append('Review rating out of 5')
    row2.append(rating)

    # find image url
    image_url = soup.findAll('img', limit=1)
    for i in image_url:

        result = ('https://books.toscrape.com/' + i['src'])
        row1.append('image_url')
        row2.append(result)

    # Using csv to extract information into a csv file
    csv_writer.writerow(row1)
    csv_writer.writerow(row2)


scrapping_book_information('https://books.toscrape.com/catalogue/its-only-the-himalayas_981/index.html')


def travel_category_books_url(url):

    # Make a Get request to fetch the raw HTML content
    html_content = requests.get(url).text

    # Parse the html content
    soup = BeautifulSoup(html_content, "html.parser")

    # Extracting the name of the category
    category_name = soup.find('h1').text

    # Extracting all products url from a category
    for i in soup.find_all('div', {'class': 'image_container'}):
        links = i.find('a', href=True)
        links = links['href'].replace('../../..', '')
        print('https://books.toscrape.com/catalogue' + links)


travel_category_books_url('https://books.toscrape.com/catalogue/category/books/travel_2/index.html')

# def scrapping_books_information_from_url():
#
#
#
#
# #QUESTIONS:
#
# # COMMENT COMBINER LES DEUX FONCTIONS???
# # COMMENT LE PRINT EN CSV ?
## passer en parametre de la premiere fonction, le ' links ' ?




