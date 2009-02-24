from BeautifulSoup import BeautifulSoup
import urllib2

def main():
    page = urllib2.urlopen("http://thepiratebay.org/")
    soup = BeautifulSoup(page)
    footer = soup.find('p', id='footer')
    print footer

if __name__ == '__main__':
    main()

    <p id="footer" style="color:#666; font-size:0.9em; ">
            3.451.108 registered users. Last updated 20:32:04.<br />
            IPv4 22.641.835 peers (10.558.456 seeders + 12.083.379 leechers) in 1.696.749 torrents on tracker.<br />
            IPv6 22.663 peers (9.603 seeders + 13.060 leechers) in 21.763 torrents on tracker.<br />
    </p>
