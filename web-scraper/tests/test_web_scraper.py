import pytest

from web_scraper.scraper import get_citations_needed_report ,get_citations_needed_count,BeautifulSoup

def test_get_citations_needed_count():
    
    actual=  get_citations_needed_count("https://en.wikipedia.org/wiki/History_of_Mexico")
    expected =5
    assert actual == expected


def test_get_citations_needed_report():
     
    actual = get_citations_needed_report("https://en.wikipedia.org/wiki/History_of_Mexico").strip().startswith("Citation needed pqragraph")
    expected = True
   
    assert actual == expected