"""Wikipedia library
"""
import requests
import yake
from bs4 import BeautifulSoup

# def get_page(url):
#     """Use requests to get the page content from url"""
#     response = requests.get(url)
#     return response.text

# use beautiful soup to get the text from the page url
def get_page(url):
    """Use beautiful soup to get the page content from url"""
    response = requests.get(url, timeout=5)
    soup = BeautifulSoup(response.text, "html.parser")
    return soup.get_text()


def get_url_keywords(url):
    """Get keywords from url page"""
    content = get_page(url)
    kw_extractor = yake.KeywordExtractor()
    keywords = kw_extractor.extract_keywords(content)  # list of tuples
    keywords_list = []
    for kwd in keywords:
        kwd_clean = kwd[0].strip().title()
        if kwd_clean not in keywords_list:
            keywords_list.append(kwd[0])
    return keywords_list


def main(url):
    """Testing"""
    keywords = get_url_keywords(url)
    print(keywords)


if __name__ == "__main__":
    target_url = input("Enter URL: ")
    main(target_url)
