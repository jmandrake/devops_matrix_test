"""Get company URL from symbol from Nasdaq"""
import requests

# from bs4 import BeautifulSoup
# import json


def get_company_website(symbol):
    """Get company website from symbol"""
    # Make a request to the Nasdaq API to get the company's info
    url = "http://www.nasdaq.com/api/v1/symbol/{}/company-info".format(symbol)
    r = requests.get(url, timeout=5)
    data = r.json()

    # Extract the website from the response
    website = data["data"]["website"]

    return website


if __name__ == "__main__":
    value = input("Enter symbol: ")
    print(get_company_website(value))
