import scraper
import argparse

if __name__ == '__main__':
    search = input("Search Term: ")
    amount = int(input("Amount: "))

    scrape = scraper.Scraper(search, amount)

    for listing in scrape.get_listings():
        print(listing)

    print("Average: " + str(scrape.get_average()))
    print("Median: " + str(scrape.get_median()))
    print("Max: " + str(scrape.get_max()))
    print("Min: " + str(scrape.get_min()))
