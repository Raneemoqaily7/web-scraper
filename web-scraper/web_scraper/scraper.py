#1st : install and import modules
#pip install requests
#pip install bs4
import requests
from bs4 import BeautifulSoup
import re


#2nd : used request to fetch the url 
class Scraper :
    def __init__(self , url =None) :
        self.url =url

def get_citations_needed_count(url):
        """
        function that report the number of citations needed.
        argument: url
        return:  integer
        """
        list1=[]
        #3rd :save page content/markub
        response =requests.get(url)
        src = response.content
        # print (src)


        #create soup object to parse content
        soup =BeautifulSoup (src ,"html.parser")
        # print (soup)

        citation_needed = soup.find_all("a" ,{"title":"Wikipedia:Citation needed"})
        
        # print (citation_needed) 
        
        for citation in citation_needed:
            list1.append(citation)
        # print(list1)
        print(len(list1))


def  get_citations_needed_report(url) :


        response =requests.get(url)
        src = response.content
        soup =BeautifulSoup (src ,"html.parser")
        for ele in soup.find_all("a" ,{"title":"Wikipedia:Citation needed"}):
            paragraph =ele.find_parent("p")
            print (paragraph)
            
           
    #    aragraph.rsplit('.com', 1)
        # test = "This is a test...we should not be able to see this"
        # res = re.sub(r'Citation_needed',"",paragraph)
        # print(res)
        # new_url = paragraph[:paragraph.rfind("Citation needed")]
        # new_new =new_url.replace(" ")
        # print (new_new)










if __name__=='__main__':
    scrap = Scraper()
    scrap=get_citations_needed_count("https://en.wikipedia.org/wiki/History_of_Mexico")
    scrap =get_citations_needed_report("https://en.wikipedia.org/wiki/History_of_Mexico")
  


















