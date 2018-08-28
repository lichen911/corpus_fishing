import urllib.request
from bs4 import BeautifulSoup
import re
import time

base_url = "http://www.corpusfishing.com/messageboard/phpBB2/"
search_url = "http://www.corpusfishing.com/messageboard/phpBB2/search.php?search_author=ironmanstan&start="
output_file = "output.txt"

post_start = 1

fd = open(output_file, 'w')

while True:
    with urllib.request.urlopen(search_url + str(post_start)) as response:
        html = response.read()

    soup = BeautifulSoup(html, features='html.parser')

    for link in soup.find_all(attrs={'href': re.compile('highlight'), 'class': ''}):
        full_url = base_url + link.get('href')
        # print(full_url)
        fd.write(full_url + '\n')

    post_start += 15
    fd.flush()
    if post_start > 12252:
        break
    time.sleep(5)

fd.close()
