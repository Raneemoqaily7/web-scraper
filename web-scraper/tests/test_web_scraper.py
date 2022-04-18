from web_scraper.scraper import get_citations_needed_report ,get_citations_needed_count,BeautifulSoup,requests

def test_get_citations_needed_count():
    url = "https://en.wikipedia.org/wiki/History_of_Mexico"
    response =requests.get(url)
    src = response.content
    soup =BeautifulSoup (src ,"html.parser")
    scrap =get_citations_needed_count()
    
    actual= get_citations_needed_count("https://en.wikipedia.org/wiki/History_of_Mexico")
    expected = 5
    assert actual ==expected