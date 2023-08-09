from xml.dom import minidom
import requests

class Store():
    def __init__(self, searchresults:str=None):
        self.__domain = None
        self.__terms = {}
        self.__pages = {}
        self.searchresults = searchresults

    @property
    def domain(self):
        return self.__domain

    @property
    def terms(self):
        return self.__terms

    @property
    def pages(self):
        return self.__pages

    def add_link(self,link_text,url):
        self.pages[url] = link_text
        for i in link_text.split():
            if i not in self.terms:
                self.terms[i] = [url]
            else:
                self.terms[i].append(url)



    def search(self,keyword):
        results = []
        url = self.terms[keyword]
        for i in url:
            link_name = self.pages[i]
            results.append((i,link_name))
        return results

