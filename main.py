# Importing the libraries
import requests
import csv
from bs4 import BeautifulSoup

filename = "information.csv"
csv_writer = csv.writer(open(filename, 'w+', newline='', encoding="UTF-8"))


# this fonction will gather information we need from a book we have chosen

def book_information(book_url):

    # Make a Get request to fetch the raw HTML content
    html_content = requests.get(book_url).text

    # Parse the html content
    soup = BeautifulSoup(html_content, "html.parser")

    # where all the csv headers will be listed
    headers = [
        'product_page_url',
        'universal_ product_code (upc)',
        'title',
        'price_excluding_tax',
        'price_including_tax',
        'number_available',
        'product_description',
        'category',
        'review_rating',
        'image_url',
    ]

    # data from the book is listed here
    data = []

    # Extracting URL of the book
    book_url = 'https://books.toscrape.com/catalogue/its-only-the-himalayas_981/index.html'
    data.append(book_url)

    # Extracting the UPC (universal product code)
    upc = soup.find(class_='table')
    # The UPC is always the first item from the td list
    upc = upc.find_all('td')[0].text
    data.append(upc)

    # extract book title
    title = soup.find("h1")
    data.append(title.text)

    # Extracting the price without taxes
    price_no_tax = soup.find(class_='table')
    # The price_no_tax is always the third item from the td list
    price_no_tax = price_no_tax.find_all('td')[2].text
    data.append(price_no_tax)

    # Extracting the price with taxes
    price_with_tax = soup.find(class_='table')
    # The price_with_tax is always the fourth item from the td list
    price_with_tax = price_with_tax.find_all('td')[3].text
    data.append(price_with_tax)

    # Extracting the number of books available
    availability = soup.find(class_='table')
    # The availability is always the fifth item from the td list
    availability = availability.find_all('td')[5].text
    data.append(availability)

    # find product description
    product_description = soup.find('div', id='product_description').findNextSibling().text
    data.append(product_description)

    # find product category
    category = soup.find('ul', class_='breadcrumb')
    # listing all the ' li ' and looking for the one we are interested in, in this case, the third
    category = category.find_all('li')[2]
    category = category.find('a', href=True)
    data.append(category.text)

    # find the review rating
    review_rating = soup.find(class_='star-rating')
    rating = (review_rating['class'][1])
    data.append(rating)

    # find image url
    image_url = soup.findAll('img', limit=1)
    for i in image_url:
        result = ('https://books.toscrape.com/' + i['src'])
        data.append(result)

    # Using csv to extract information into a csv file
    csv_writer.writerow(headers)
    csv_writer.writerow(data)


book_information('https://books.toscrape.com/catalogue/its-only-the-himalayas_981/index.html')

# this fonction will gather all the urls from a book category we have chosen


def gathering_links_from_category(url_from_category):

    # Make a Get request to fetch the raw HTML content
    html_content = requests.get(url_from_category).text

    # Parse the html content
    soup = BeautifulSoup(html_content, "html.parser")

    # Extracting the name of the category
    category_name = soup.find('h1').text
    print(category_name)

    # Extracting all products url from a category
    for i in soup.find_all('div', {'class': 'image_container'}):
        # Finding all the links from the html
        book_link = i.find('a', href=True)
        # Getting the list of url and getting rid of the relative url with .replace
        book_link = book_link['href'].replace('../../..', '')
        # Adding the base URL with the relative url to bring together the full url
        book_link = 'https://books.toscrape.com/catalogue' + book_link
        book_information(book_link)


gathering_links_from_category('https://books.toscrape.com/catalogue/category/books/travel_2/index.html')



