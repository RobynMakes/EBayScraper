import requests
import math_utils as maths
from bs4 import BeautifulSoup


class Scraper:
    scraped_array = []
    url = ""
    soup = BeautifulSoup()
    items = []
    prices = []
    listings = []

    def __init__(self, search, amount):
        search = search.replace(' ', '+')
        self.url = "https://www.ebay.com/sch/i.html?_from=R40&_nkw=" + search + "&LH_Sold=1"
        response = requests.get(self.url)                               # obtaining html code from the url

        self.soup = BeautifulSoup(response.text, 'html.parser')

        self.items = self.soup.findAll('div', 's-item__title')          # the items array holds each item's title
        self.prices = self.soup.findAll('span', 's-item__price')        # the prices array hold each item's price

        i = 0
        while i < amount:                                               # while loop populates the listing array with listings
            self.listings.append([self.items[i], self.prices[i]])
            i += 1

        self.listings.pop(0)                                            # Removing the first item in the array as it isn't actually a listing

    def get_average(self):
        array = []
        for price in self.prices:
            x = price.replace('$', '')
            array.append(float(x))
        return maths.average(array)

    def get_median(self):
        array = []
        for price in self.prices:
            x = price.replace('$', '')
            array.append(float(x))
        return maths.median(array)

    def get_max(self):
        array = []
        for price in self.prices:
            x = price.replace('$', '')
            array.append(float(x))
        return max(array)

    def get_min(self):
        array = []
        for price in self.prices:
            x = price.replace('$', '')
            array.append(x)
        return min(array)

    def get_prices(self):
        return self.prices

    def get_items(self):
        return self.items

    def get_listings(self):
        return self.listings
