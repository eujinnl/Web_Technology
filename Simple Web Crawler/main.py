import crawler
import store
o1 = crawler.Crawler()
o1.crawl("http://info.cern.ch")
print(o1.store['info.cern.ch'].search("website"))
