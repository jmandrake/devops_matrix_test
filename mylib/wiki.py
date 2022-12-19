"""Wikipedia library
"""
import wikipedia
import yake


def get_page(search):
    """use the wikipedia.suggest() function to get a suggested page
    based on the search term, which may be more accurate than simply
    retrieving the first item in the search results."""

    # Search for pages that match the search term
    results = wikipedia.search(search)

    # Get the best page from the search results
    page = wikipedia.page(results[0])

    # Print the page's title and summary
    print(page.title)
    print(page.summary)
    return page.content


def get_wiki_keywords(keyword):
    """Get keywords from wiki page"""
    content = get_page(keyword)
    kw_extractor = yake.KeywordExtractor()
    keywords = kw_extractor.extract_keywords(content)
    # print(keywords)
    return keywords


def main(keyword):
    """Testing"""
    keywords = get_wiki_keywords(keyword)
    print(keywords)


if __name__ == "__main__":
    search_term = input("Enter search term: ")
    main(search_term)
