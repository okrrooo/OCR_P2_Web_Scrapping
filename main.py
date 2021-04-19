# Importing the libraries
import requests
import csv
from bs4 import BeautifulSoup


# This function will write the headers in our information.csv file


def writing_headers_in_csv(csv_writer):

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

# this fonction will gather information we need from a book we have chosen


def book_information(book_url, csv_writer):

    # Make a Get request to fetch the raw HTML content
    html_content = requests.get(book_url).text

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
    title = soup.find("h1").text
    data.append(title)

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
    product_description = soup.find('div', id='product_description')
    if product_description is not None:
        product_description = product_description.findNextSibling().text
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
    image_url = soup.find('img')
    # cutting the relative url
    image_url = image_url['src'][5:]
    # reconstructing the full url
    image_url = ('https://books.toscrape.com/' + image_url)
    # appending the image url to the list
    data.append(image_url)
    print('image url', image_url)

    # Downloading and saving the images
    image = image_url
    # the filename is related to the title of the book, using .replace remove special character
    filename = title.replace('#', '')
    filename = filename.replace('\\', '')
    filename = filename.replace('!', '')
    filename = filename.replace(')', '')
    filename = filename.replace('(', '')
    filename = filename.replace('"', '')
    filename = filename.replace(':', '')
    filename = filename.replace('/', '')
    filename = filename.replace('*', '')
    filename = filename.replace('?', '')
    # adding .png to the filename to create png files
    filename = filename + '.png'

    # using requests.get to get the image
    r = requests.get(image)
    # checking if status_code is 200, meaning the requests has no problem
    if r.status_code == 200:
        with open(filename, 'wb') as f:
            f.write(r.content)

    # Using csv to write information into  csv file

    csv_writer.writerow(data)

# this fonction will gather all the urls from a book category we have chosen


def gathering_links_from_category(links_from_category, csv_writer):

    # Make a Get request to fetch the raw HTML content
    html_content = requests.get(links_from_category).text

    # Parse the html content
    soup = BeautifulSoup(html_content, "html.parser")

    # Extracting the name of the category
    category_name = soup.find('h1').text

    # Extracting all products url from a category
    for i in soup.find_all('div', {'class': 'image_container'}):
        # Finding all the links from the html
        book_url = i.find('a', href=True)
        # Getting the list of url and getting rid of the relative url with .replace
        book_url = book_url['href'].replace('../../..', '')
        # Adding the base URL with the relative url to bring together the full url
        book_url = 'https://books.toscrape.com/catalogue' + book_url
        # calling book_information on our links
        print('book_url', book_url)
        book_information(book_url, csv_writer)

    # checking if there is multiple pages:

    # finding the next button on the html code
    relative_url = soup.find('li', class_='next')
    if relative_url is not None:
        # finding the link 'next'
        relative_url = relative_url.find('a', href=True)
        # targeting the end of the url
        relative_url = relative_url['href']
        # keeping the base url and adding our next url representing the next button
        # using the .split method to gather the base url in list form
        base_url = links_from_category.split('/')[:7]
        # using the .join method to transform the list to a string and adding our dynamique relative url
        base_url = '/'.join(base_url) + '/'  # adding '/' to complete our url (books/)
        # gathering links from the new page
        # print(base_url + relative_url)
        gathering_links_from_category(base_url + relative_url, csv_writer)

# This function will make a list of all the books category on books.toscrape.com


def gathering_all_categories_links(book_to_scrape_index):

    # Make a Get request to fetch the raw HTML content
    html_content = requests.get(book_to_scrape_index).text

    # Parse the html content
    soup = BeautifulSoup(html_content, "html.parser")

    # Gathering links from the index
    for a in soup.select('ul.nav li ul li a'):   # looking for all link in list from the class nav
        categories = 'https://books.toscrape.com/' + a['href']  # completing the base url with the relative links
        print('Category', categories)

        category_name = a.text.strip()     # using strip to remove whitespaces

        filename = category_name + '.csv'
        file = open(filename, 'w', newline='', encoding='UTF8')
        csv_writer = csv.writer(file)
        writing_headers_in_csv(csv_writer)

        gathering_links_from_category(categories, csv_writer)
        # closing the csv file
        file.close()


gathering_all_categories_links('https://books.toscrape.com/index.html')

