from bs4 import BeautifulSoup
from urllib.request import urlopen


class BugsMusic(object):

    url = ''

    aaa = "artist", "title"

    def __str__(self):
        return self.url

    def count(self):
        print(f'Input URL: {self.url}')
        soup = BeautifulSoup(urlopen(self.url), 'html.parser')
        count = 0
        for link1 in soup.find_all(name='p', attrs={"class": self.aaa}):
            count += 1
            print(f'RANK: {str(count)}')
            print(f'NAME: {link1.find("a").text}')

    @staticmethod
    def main():
        bugs = BugsMusic()
        while 1:
            menu = input('0.Exit 1.Input URL 2.Get Ranking, GET ARTIST')
            if menu == '0':
                print('exit')
                break
            elif menu == '1':
                bugs.url = input('Input URL')
            elif menu == '2':
                bugs.count()
            else:
                print('Wrong Number')
                continue

# bugs.url = 'https://music.bugs.co.kr/chart/track/realtime/total?wl_ref=M_contents_03_01'
BugsMusic.main()

