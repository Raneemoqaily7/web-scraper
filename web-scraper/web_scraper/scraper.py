#1st : install and import modules
#pip install requests
#pip install bs4
import requests
from bs4 import BeautifulSoup
import re


#2nd : used request to fetch the url 

def get_citations_needed_count(url):
        """
        function that report the number of citations needed.
        argument: url
        return:  integer
        """
        list1=[]
        #2nd : used request to fetch the url 
        response =requests.get(url)

        #3rd :save page content/markub
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
        return len(list1)


def  get_citations_needed_report(url) :
        """
        extract the pargraph that contain a "citation need"
        argument: takes in a url 
        returns: a string
        """

        res = ""
        response =requests.get(url)
        src = response.content
        soup =BeautifulSoup (src ,"html.parser")
        for ele in soup.find_all("a" ,{"title":"Wikipedia:Citation needed"}):
            paragraph =ele.find_parent("p")
            res+=f'Citation needed pqragraph : {paragraph.text}' +"\n"
        return  res
           
            
   









if __name__=='__main__':
    
    print(get_citations_needed_count("https://en.wikipedia.org/wiki/History_of_Mexico"))
    print(get_citations_needed_report("https://en.wikipedia.org/wiki/History_of_Mexico"))
  


















