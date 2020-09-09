import json
import notify2
import beautifulsoup

def alert(info):
	notify2.init('content aggr')
        notif = notify2.Notification('content', info)
	# notif.set_urgency(notify2.URGENCY_CRITICAL)
        notif.show()
        notif.set_timeout(10)

urlclient = urlreq(fullscrapadr)
urlpg = urlclient.read()

urlclient.close()
urldata = bs4.BeautifulSoup(urlpg, 'html.parser')
urldata.find(scrtagcapture).text.strip()

alert(--)
