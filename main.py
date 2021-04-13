# Importing the libraries
import requests
import csv
from bs4 import BeautifulSoup

filename = "information.csv"
csv_writer = csv.writer(open(filename, 'w+', newline='', encoding="UTF-8"))


def writing_headers_in_csv():

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

    csv_writer.writerow(headers)


writing_headers_in_csv()

# this fonction will gather information we need from a book we have chosen


def book_information(book_url):

    # Make a Get request to fetch the raw HTML content
    html_content = requests.get(book_url).text

    # Parse the html content
    soup = BeautifulSoup(html_content, "html.parser")

    # data from the book is listed here
    data = []

    # Extracting URL of the book
    data.append(book_url)

    # Extracting the UPC (universal product code)
    upc = soup.find(class_='table')
    # Looking for the UPC in the TD list
    upc = upc.find_all('td')[0].text
    data.append(upc)

    # extract book title
    title = soup.find("h1")
    data.append(title.text)

    # Extracting the price without taxes
    price_no_tax = soup.find(class_='table')
    # Looking for the price_no_tax in the TD list
    price_no_tax = price_no_tax.find_all('td')[2].text
    data.append(price_no_tax)

    # Extracting the price with taxes
    price_with_tax = soup.find(class_='table')
    # Looking for the price with tax in the TD list
    price_with_tax = price_with_tax.find_all('td')[3].text
    data.append(price_with_tax)

    # Extracting the number of books available
    availability = soup.find(class_='table')
    # Looking for the availability in the TD list
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

    csv_writer.writerow(data)


# this fonction will gather all the urls from a book category we have chosen


def gathering_links_from_category(links_from_category):

    # Make a Get request to fetch the raw HTML content
    html_content = requests.get(links_from_category).text

    # Parse the html content
    soup = BeautifulSoup(html_content, "html.parser")

    # Extracting the name of the category
    category_name = soup.find('h1').text

    # Extracting all products url from a category
    for i in soup.find_all('div', {'class': 'image_container'}):
        # Finding all the links from the html
        book_link = i.find('a', href=True)
        # Getting the list of url and getting rid of the relative url with .replace
        book_link = book_link['href'].replace('../../..', '')
        # Adding the base URL with the relative url to bring together the full url
        book_link = 'https://books.toscrape.com/catalogue' + book_link
        # calling book_information on our links
        book_information(book_link)
        print(book_link)

    # checking if there is multiple pages:

    # finding the next button on the html code
    next_url = soup.find('li', class_='next')
    if next_url is not None:
        # finding the link 'next'
        next_url = next_url.find('a', href=True)
        # targeting the end of the ur
        next_url = next_url['href']
        # keeping the base url and adding our next url representing the next button
        next_url = links_from_category[:69] + next_url
        # gathering links from the new page
        gathering_links_from_category(next_url)


gathering_links_from_category('https://books.toscrape.com/catalogue/category/books/travel_2/index.html')


def gathering_all_category(book_to_scrape_index):

    # Make a Get request to fetch the raw HTML content
    html_content = requests.get(book_to_scrape_index).text

    # Parse the html content
    soup = BeautifulSoup(html_content, "html.parser")

    # Gathering links from the index
    for a in soup.select('.nav li a'):   # looking for all link in list from the class nav
        categories = ('https://books.toscrape.com/' + (a['href']))  # completing the base url with the relative links
        print(categories)







gathering_all_category('https://books.toscrape.com/index.html')

    #recuperer toutes les catégories possibles du site



# category_url[:category_url.rfind('/')+1]