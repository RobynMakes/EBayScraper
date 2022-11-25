import scraper
import math_utils as maths

# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    url = input("URL: ")
    amount = int(input("Amount: "))

    scraped_array = scraper.scrape(url, amount)

    for item in scraped_array:
      print(item)

    print('Average: ' + str(scraper.get_average(prices=scraper.get_prices(scraped_array))))
    print('Median: ' + str(scraper.get_median(prices=scraper.get_prices(scraped_array))))
    print('Max: ' + str(scraper.get_max(prices=scraper.get_prices(scraped_array))))
    print('Min: ' + str(scraper.get_min(prices=scraper.get_prices(scraped_array))))

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
