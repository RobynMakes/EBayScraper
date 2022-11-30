# scraper.py
import requests
import math_utils as maths
from bs4 import BeautifulSoup

SOLD = 0
UNSOLD = 1


class Scraper:
    scraped_array = []
    url = ""
    soup = BeautifulSoup()
    items = []
    prices = []
    listings = []

    def __init__(self, search: str, amount: int):
        """
        The constructor for the Scraper class. \n
        The search parameter must be a str. \n
        The amount parameter must be an int. \n

        Keyword Arguments:
            search: the search term used to build the webpage's URL
            amount: the number of listings to search
        """
        search = search.replace(' ', '+')
        self.url = "https://www.ebay.com/sch/i.html?_from=R40&_nkw=" + search + "&LH_Sold=1"
        response = requests.get(self.url)  # obtaining html code from the url

        self.soup = BeautifulSoup(response.text, 'html.parser')

        self.items = self.soup.findAll('div', 's-item__title')  # the items array holds each item's title
        self.prices = self.soup.findAll('span', 's-item__price')  # the prices array hold each item's price

        for i in range(len(self.items)):
            self.items[i] = self.items[i].text

        for i in range(len(self.prices)):
            self.prices[i] = self.prices[i].text

        for i in range(amount):  # for loop populates the listing array with listings
            self.items[i] = self.items[i].replace('<div class="s-item__title"><span aria-level="3" role="heading">', '')
            self.items[i] = self.items[i].replace('</span></div>', '')
            self.prices[i] = self.prices[i].replace('<span class="s-item__price"><span class="POSITIVE ITALIC">', '')
            self.prices[i] = self.prices[i].replace('</span></span>', '')
            self.listings.append([self.items[i], self.prices[i]])
            i += 1

        self.listings.pop(0)  # Removing the first item in the array as it isn't actually a listing

    def get_average(self):
        """Returns the average of the prices array"""
        array = []
        for price in self.listings:
            x = price[1].replace('$', '')
            try:
                array.append(float(x))
            except ValueError:
                print("Value Error: could not convert string to float: '" + str(price) + "'")
                continue
            else:
                array.append(float(x))
        return maths.average(array)

    def get_median(self):
        """Returns the median of the prices array"""
        array = []
        for price in self.listings:
            try:
                x = price[1].replace('$', '')
            except ValueError:
                print("Value Error: could not convert string to float: '" + str(price) + "'")
                continue
            else:
                array.append(float(x))
        return maths.median(array)

    def get_max(self):
        """Returns the maximum of the prices array"""
        array = []
        for price in self.listings:
            try:
                x = price[1].replace('$', '')
            except ValueError:
                print("Value Error: could not convert string to float: '" + str(price) + "'")
            else:
                array.append(float(x))
        return max(array)

    def get_min(self):
        """Returns the minimum of the prices array"""
        array = []
        for price in self.listings:
            try:
                x = price[1].replace('$', '')
            except ValueError:
                print("Value Error: could not convert string to float: '" + str(price) + "'")
            else:
                array.append(float(x))
        return min(array)

    def get_listings(self):
        """Returns the listing array"""
        return self.listings
