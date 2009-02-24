from BeautifulSoup import BeautifulSoup
import urllib2
import re

def clean(dotted_string):
    return int(re.sub(r'\D', '', dotted_string))

def read_data(row):
    items = row.strip().split()
    unprocessed = items[3], items[6], items[9]
    return map(clean, unprocessed)

def stdout_fmt(seeds, leechers, torrents):
   data = (seeds, leechers, seeds+leechers, torrents)
   return "%d seeds, %d leechers (%d total) and %d torrents" % data

# TODO SQL

def main():
    page = urllib2.urlopen("http://thepiratebay.org/")
    soup = BeautifulSoup(page)
    footer_rows = soup.find('p', id='footer').findAll(text=True)
    ip_rows = footer_rows[1], footer_rows[2]
    ip4, ip6 = map(read_data, ip_rows)
    print "IPv4:", stdout_fmt(*ip4)
    print "IPv6:", stdout_fmt(*ip6)

if __name__ == '__main__':
    main()
