import requests
import math_utils as maths
from bs4 import BeautifulSoup


def scrape(search, amount):
    url = "http://www.ebay.com/sch/i.html?_from=R40&_nkw=" + search + "&LH_Sold=1"
    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'html.parser')

    items = soup.findAll('div', 's-item__title')
    prices = soup.findAll('span', 's-item__price')

    titles = []
    costs = []

    for item in items:
        titles.append(item.get_text())

    for price in prices:
        costs.append(price.get_text())

    i = 0
    final_array = []

    while i < amount:
        final_array.append([titles[i], costs[i]])
        i += 1

    final_array.pop(0)
    return final_array


def get_average(prices):
    array = []
    for price in prices:
        x = price.replace('$', '')
        array.append(float(x))
    return maths.average(array)


def get_median(prices):
    array = []
    for price in prices:
        x = price.replace('$', '')
        array.append(float(x))
    return maths.median(array)


def get_max(prices):
    array = []
    for price in prices:
        x = price.replace('$', '')
        array.append(float(x))
    return max(array)


def get_min(prices):
    array = []
    for price in prices:
        x = price.replace('$', '')
        array.append(x)
    return min(array)


def get_prices(data):
    prices = []

    for x in data:
        prices.append(x[1])

    return prices
