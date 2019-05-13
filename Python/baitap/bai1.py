import requests
from bs4 import BeautifulSoup
import re
url = "http://actvn.edu.vn/"
req = requests.get(url)
page_link = []
soup = BeautifulSoup(req.text, "lxml")
for link in soup.findAll('a', attrs={'href': re.compile("^http://")}):
    print(link.get('href'))
# for sub_heading in soup.find_all('link'):
#     print(sub_heading.text)
