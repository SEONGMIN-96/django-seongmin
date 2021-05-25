from bs4 import BeautifulSoup
import requests


class Melon(object):

    url = ''

    hdr = {'User-Agent': 'Mozilla/5.0 (Windows NT 6.3; Trident/7.0; rv:11.0) like Gecko'}

    @staticmethod
    def main():
        melon = Melon()
        while 1:
            menu = input('0. 1.Input URL 2.READ')
            if menu == '1':
                melon.url = requests.get(input('Input URL'), headers=melon.hdr).text
            elif menu == '2':
                soup = BeautifulSoup(melon.url, "lxml")
                for i in soup.find_all(name="div", attrs={"class": "ellipsis rank01"}):
                    print(i.find("a").text)
            else :
                continue


Melon.main()

'''
https://www.melon.com/chart/index.htm
'''