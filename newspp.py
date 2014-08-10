import newspaper
import time

sites = """
http://www.wired.com/
http://www.theguardian.com
http://news.discovery.com/
http://www.sciencedaily.com/
http://phys.org/
http://nautil.us/
http://www.npr.org/
http://www.slate.com/
http://www.theatlantic.com/
http://io9.com/
http://www.smithsonianmag.com/
http://www.nationalgeographic.com/
http://www.livescience.com/
http://www.popsci.com/
http://www.newscientist.com/
http://arstechnica.com/
http://www.bbc.com/news/
http://www.nature.com/news/
"""

site_list = sites.split("\n")[1:-1]

for site in site_list:
    try:
        paper = newspaper.build(site, memoize_articles=False)
    except:
        continue

    for article in paper.articles[0:50]:
        article.download()
        try:
            article.parse()
        except: continue

        """
        time.sleep(2)  # fixed an error
        article.nlp()
        """

        # print article.keywords
        planet = 'noaa'
        # if planet in article.keywords or planet in article.title.lower():
        if planet in article.title.lower():
            print "%s: %s" % (str(article.title), str(article.url))
