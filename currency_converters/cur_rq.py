from bs4 import BeautifulSoup
import urllib.request

# get info from site

EUR_get = urllib.request.urlopen('https://www.xe.com/currencyconverter/convert/?Amount=1&From=USD&To=EUR')
GBP_get = urllib.request.urlopen('https://www.xe.com/currencyconverter/convert/?Amount=1&From=USD&To=GBP')
DKK_get = urllib.request.urlopen('https://www.xe.com/currencyconverter/convert/?Amount=1&From=USD&To=DKK')
SEK_get = urllib.request.urlopen('https://www.xe.com/currencyconverter/convert/?Amount=1&From=USD&To=SEK')

read_content1 = EUR_get.read()
read_content2 = GBP_get.read()
read_content3 = DKK_get.read()
read_content4 = SEK_get.read()

# Make info readable

soup1 = BeautifulSoup(read_content1,'html.parser')
soup2 = BeautifulSoup(read_content2,'html.parser')
soup3 = BeautifulSoup(read_content3,'html.parser')
soup4 = BeautifulSoup(read_content4,'html.parser')

EURtext = soup1.find_all('p')
GBPtext = soup2.find_all('p')
DKKtext = soup3.find_all('p')
SEKtext = soup4.find_all('p')

EUR = EURtext[3].text
GBP = GBPtext[3].text
DKK = DKKtext[3].text
SEK = SEKtext[3].text

# Telling where to read

beginning1 = EUR.index("1")
end1 = EUR.index("U") - 1
et1 = EUR.index("USD")
bt1 = EUR.index("=") + 2

ex_rate_EUR = EUR[bt1:et1]
ex_rate_GBP = GBP[bt1:et1]
ex_rate_DKK = DKK[bt1:et1]
ex_rate_SEK = SEK[bt1:et1]
