from BeautifulSoup import BeautifulSoup
import urllib2

def main():
    page = urllib2.urlopen("http://thepiratebay.org/")
    soup = BeautifulSoup(page)
    footer = soup.find('p', id='footer')
    print footer

if __name__ == '__main__':
    main()
