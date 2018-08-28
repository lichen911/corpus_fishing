import urllib.request
from bs4 import BeautifulSoup

input_file = 'master_list.txt'
output_file = 'image_list.txt'

fdout = open(output_file, 'w')

with open(input_file, 'r') as fd:
    for post_url in fd:
        # post_url = "http://www.corpusfishing.com/messageboard/phpBB2/viewtopic.php?p=279250&highlight=&sid=457cafe0e159318758abcc36e7223287#279250"
        # print(post_url)

        with urllib.request.urlopen(post_url) as response:
            html = response.read()

        soup = BeautifulSoup(html, features='html.parser')

        # for link in soup.find_all(attrs={'class': 'postbody'}):
        #     print(link)

        # for img in soup.find_all('img'):
        #     print(img.get('src'))

        for item in soup.find_all('b', string='ironmanstan'):
            cur_item = item

            # move 15 elements past username to find body of message
            for i in range(15):
                cur_item = cur_item.next_element

            # extract img src from body of msg
            for img in cur_item('img'):
                img_url = img.get('src')
                # print(img_url)

                # only grab the image if it's hosted on tinypic or photobucket
                if any(img_host in img_url for img_host in ['photobucket', 'tinypic']):
                    print(img_url)
                    fdout.write(img_url + '\n')

            fdout.flush()
fdout.close()
