import beautifulsoup
import notify2
import json

from urllib.request import urlopen as urlreq

scrapadrescapture = input('  ' + colorsfunc['fadebluecl'] + 'lk: ')

fullscrapadr = 'https://' + scrapadrescapture

try:
    adrip = colorsfunc['redcl'] + socket.gethostbyname(str(scrapadrescapture)) + colorsfunc['endcl']
except:
    adrip = colorsfunc['redcl'] + '0.0.0.0' + colorsfunc['endcl']
print('  ' + colorsfunc['fadebluecl'] + 'ip: ' + colorsfunc['endcl'] + adrip)
try:
    adrmac = re.search(r"(([a-f\d]{1,2}\:){5}[a-f\d]{1,2})", Popen(["arp", "-n", IP], stdout = PIPE).communicate()[0]).groups()[0].decode('ISO-8859-1')
except:
    adrmac = 'mc'
print('  ' + colorsfunc['fadebluecl'] + 'mc: ' + colorsfunc['endcl'] + colorsfunc['whitecl2'] + adrmac)
print('  ' + colorsfunc['fadebluecl'] + 'pt: ' + colorsfunc['endcl'] + colorsfunc['whitecl2'] + '')
print('  ' + colorsfunc['fadebluecl'] + 'ph: ' + colorsfunc['endcl'] + colorsfunc['whitecl2'] + '/')
print('  ' + colorsfunc['fadebluecl'] + 'gc: ' + colorsfunc['endcl'] + colorsfunc['whitecl2'] + '')
try:
    scrapobjid = random.randint(1, 1000)
    newhkrpyldcode = datacore['scrpyldidhdr'] + str(scrapobjid)
    if newhkrpyldcode in datacore['scrpyldsinfos']:
        scrapobjid = random.randint(1, 1000)
        newhkrpyldcode = datacore['scrpyldidhdr'] + str(scrapobjid)
        datacore['scrpyldsinfos'].append(newhkrpyldcode)
    else:
        newhkrpyldcode = datacore['scrpyldidhdr'] + str(scrapobjid)
        datacore['scrpyldsinfos'].append(newhkrpyldcode)
except:
    pass
print('  ' + colorsfunc['fadebluecl'] + 'id: ' + colorsfunc['endcl'] + colorsfunc['whitecl2'] + newhkrpyldcode + colorsfunc['endcl'])
print('  ' + datacore['donecaption'] + ' :' + 'set url to scrp')
try:
    urlclient = urlreq(fullscrapadr)
    print('  ' + datacore['donecaption'] + ' :' + 'request client')
except:
    print('  ' + datacore['errorcaption'] + ' :' + 'request client')
try:
    urlpg = urlclient.read()
    print('  ' + datacore['donecaption'] + ' :' + 'read from client to pg')
except:
    print('  ' + datacore['errorcaption'] + ' :' + 'read from client to pg')
try:
    urlclient.close()
    print('  ' + datacore['donecaption'] + ' :' + 'close client')
except:
    print('  ' + datacore['errorcaption'] + ' :' + 'close client')
try:
    urldata = bs4.BeautifulSoup(urlpg, 'html.parser')
    print('  ' + datacore['donecaption'] + ' :' + 'parse cnts to bs4 ' + '\n  ' + colorsfunc['greenbgcl'] + colorsfunc['blackcl'] + ' done ' + colorsfunc['endcl'])
except:
    print('  ' + datacore['errorcaption'] + ' :' + 'parse cnts to bs4\n  ' + colorsfunc['redcl'] + 'no connection' + colorsfunc['endcl'])
    scrapfunction()
def scrfindtagfunction():
    scrtagcapture = input('  >> scr.tg.')
    if scrtagcapture == '':
        scrapfunction()
    else:
        try:
            tagbreakdown = str(urldata.find(scrtagcapture).text.strip())
            if len(str(tagbreakdown)) == 0:
                tagattributes = 'no text'
            else:
                tagattributes = tagbreakdown
            print('  :: ' + '<' + scrtagcapture + '/> in ' + str(scrapadrescapture) + '\n  :: ' + str(tagattributes))
            scrfindtagfunction()
        except:
            scrfindtagfunction()
scrfindtagfunction()
