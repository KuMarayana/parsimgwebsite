from anonBrowser import *
from BeautifulSoup import BeautifulSoup
import os
import optparse
import re

def printLinks(url):
    ab = anonBrowser()
    ab.anonymize()
    page = ab.open(url)
    html = page.read()
    try:
        print '[*] printing links dari regex.'
        link_finder = re.compile('herf="(.*?)"')
        links = link_finder.findall(html)
        for link in links:
            print link
    except:
        pass
    try:
        print '\n[*] printing linknya dari Beautifulsoup'
        soup = BeautifulSoup(html)
        links = soup.findAll(name='a')
        for link in links:
            if link.has_key('herf'):
                print link['herf']
    except:
        pass

def main():
    parser = optparse.OptionParser('usage prog ' +\
        '-u <target>')
    parser.add_option('-u', dest='tgURL', type='string',\
       help='specify target url')
    (options, args) = parser.parse_args()
    url = options.tgURL
    if url == None:
        print parser.usage
        exit(0)
    else:
        printLinks(url)

if __name__ == '__main__':
    main()