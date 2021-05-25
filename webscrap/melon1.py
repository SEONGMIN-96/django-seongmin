from bs4 import BeautifulSoup
import requests


class Melon(object):
    url = ''

    value = []

    headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 6.3; Trident/7.0; rv:11.0) like Gecko'}

    def count(self):
        soup = BeautifulSoup(self.url, 'lxml')
        count = 0
        for i in soup.find_all("div", {"class": self.value}):
            count += 1
            print(f'{str(count)}위')
            print(f' TITLE: {i.find("a").text}')


    @staticmethod
    def main():
        melon = Melon()
        while 1:
            menu = int(input('0.Exit  1.Input URL 2.Title,Artist Ranking'))
            if menu == 0:
                break
            elif menu == 1:
                melon.url = requests.get(input('URL 입력'), headers=melon.headers).text
            elif menu == 2:
                melon.value.append("ellipsis rank01")
                melon.value.append("ellipsis rank02")
                melon.count()
            else:
                print('다시 입력하세요')
                continue


Melon.main()

'''
https://www.melon.com/chart/index.htm
'''