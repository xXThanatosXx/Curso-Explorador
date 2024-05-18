from scraper import scrape_product_prices
from comparison import compare_prices
import config
import scheduler

def main():
    data = scrape_product_prices(config.products)
    price_comparison = compare_prices(data)
    print(price_comparison)

if __name__ == "__main__":
    main()
    scheduler.schedule_job(main)
