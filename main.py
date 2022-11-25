import scraper
import argparse
if __name__ == '__main__':
    search = input("Search Term: ")
    amount = int(input("Amount: "))

    scrape = scraper.Scraper(search, amount)

    print(scrape.get_listings())
