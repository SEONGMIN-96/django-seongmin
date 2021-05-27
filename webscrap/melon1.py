from bs4 import BeautifulSoup
import requests


class Melon(object):
    url = 'https://www.melon.com/chart/index.htm'
    headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 6.3; Trident/7.0; rv:11.0) like Gecko'}

    def set_url(self):
        self.url = requests.get(self.url, headers=self.headers).text

    @staticmethod
    def main():
        while 1:
            menu = input('0. 1.Input 2.Output')
            if menu == '0':
                break
            elif menu == '1':
                pass
            elif menu == '1':
                pass
            else:
                continue


Melon.main()

'''
https://www.melon.com/chart/index.htm
'''