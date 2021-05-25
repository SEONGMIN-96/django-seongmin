from bs4 import BeautifulSoup
from urllib.request import urlopen


class Melon(object):

    url = ''

    def __str__(self):
        return self.url

    @staticmethod
    def main():
        melon = Melon()
        while 1:
            m = input('0.Exit 1.Input 2.Title 3.Artist')
            if m == '0':
                break
            elif m == '1':
                melon.url = input('Input URL')
            elif m == '2':
                print(f'Input URL: {melon}')
                soup = BeautifulSoup(urlopen(melon.url), 'lxml')
                for link1 in soup.find_all(name='div', attrs={"span"}):
                    print(f'NAME: {link1.find("a").text}')
            else:
                print('Wrong Number')
                continue


Melon.main()

'''
https://www.melon.com/chart/index.htm
'''