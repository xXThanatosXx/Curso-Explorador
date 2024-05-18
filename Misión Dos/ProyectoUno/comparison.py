import pandas as pd

def compare_prices(data):
    df = pd.DataFrame(data)
    price_comparison = df.pivot(index='Product', columns='Store', values='Price')
    return price_comparison
