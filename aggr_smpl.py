import json
import notify2
import beautifulsoup

urlclient = urlreq(fullscrapadr)
urlpg = urlclient.read()

urlclient.close()
urldata = bs4.BeautifulSoup(urlpg, 'html.parser')
urldata.find(scrtagcapture).text.strip()
