from bs4 import BeautifulSoup
import requests


class Melon(object):
    url = ''

    headers = {'User-agent': 'zzzz'}

    classname = []

    @staticmethod
    def scrap(melon, classname):
        soup = BeautifulSoup(melon.url, 'lxml')
        count = 0
        for i in soup.find_all(name="div", attrs={"class": classname}):
            count += 1
            print(f'{str(count)}위')
            print(i.find("a").text)

    @staticmethod
    def main():
        melon = Melon()
        while 1:
            m = input('0.Exit 1.Input URL 2.Distribute Info')
            if m == '0':
                break
            elif m == '1':
                melon.url = requests.get(input('URL 입력'), headers=melon.headers).text
            elif m == '2':
                melon.classname.append("ellipsis rank01")
                melon.scrap(melon, melon.classname)
            else:
                continue


Melon.main()

'''
https://www.melon.com/chart/index.htm
'''