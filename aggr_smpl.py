import beautifulsoup
import notify2
import json

urlclient = urlreq(fullscrapadr)

urlpg = urlclient.read()

urlclient.close()

urldata = bs4.BeautifulSoup(urlpg, 'html.parser')

tagbreakdown = str(urldata.find(scrtagcapture).text.strip())
