import store
from xml.dom import minidom
import requests
from urllib.parse import urlparse
from bs4 import BeautifulSoup

class Crawler():
    def __init__(self):
        self.searchresults = {}
        self.uriqueue = []
        self.urivisited = []
        self.store = {}


    def fetch(self,dom,uri):
        page = "http://"+dom+uri
        x = requests.get(page)
        if x.status_code == 200:
            self.extract_links(dom,uri)
        else:
            return None

    def domain_check(self,domain,page):
        new_dom = urlparse(page).netloc
        #print(dom1,dom2)
        if domain == new_dom:
            return True
        else:
            return False

    def extract_links(self,domain,uri):
        page = "http://"+domain+uri
        self.urivisited.append(uri)
        try:
            dom = minidom.parseString(requests.get(page).text)
            x = dom.getElementsByTagName("a")
            for i in x:
                crawled = str(i.getAttribute("href"))
                self.store[domain].add_link(str(i.firstChild.data), crawled)  # link_text, site
                if self.domain_check(domain, crawled):
                    if self.urivisited != crawled:
                        self.uriqueue.append(urlparse(crawled).path)

        except:
            soup = BeautifulSoup(requests.get(page).text, 'html.parser')
            for link in soup.find_all('a'):
                path = str(link.get('href'))
                url = page[:page.rfind('/')]
                if path.startswith('.'):
                    crawled = "http://"+domain + path[path.find('/'):]
                else:
                    crawled = url + "/"+ path
                self.store[domain].add_link(str(link.text), crawled)  # link_text, site
                if self.domain_check(domain, crawled) == True and self.urivisited != crawled:
                    self.uriqueue.append(urlparse(crawled).path)
                    #print(len(self.urivisited))




    def crawl(self,page):
        dom = urlparse(page).netloc
        if dom not in self.store.keys():
            self.store[dom] = store.Store(dom)
        uri = urlparse(page).path
        self.fetch(dom,uri)
        while len(self.uriqueue) != 0:    #change this
            for i in self.uriqueue:
                if len(self.urivisited) < 20:
                    self.fetch(dom,i)
                    self.uriqueue.remove(i)

            else:
                break



c = Crawler()
c.crawl("http://info.cern.ch/")
#print(c.store)
print(c.store['info.cern.ch'].terms)
print(c.store['info.cern.ch'].search("website"))

