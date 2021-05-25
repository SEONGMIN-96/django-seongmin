from bs4 import BeautifulSoup
from urllib.request import urlopen


class BugsMusic(object):

    url = ''

    def __str__(self):
        return self.url

    @staticmethod
    
    def count(bugs, aaa):
        print(f'Input URL: {bugs}')
        soup = BeautifulSoup(urlopen(bugs.url), 'html.parser')
        count = 0
        for link1 in soup.find_all(name='p', attrs=aaa):
            count += 1
            print(f'RANK: {str(count)}')
            print(f'NAME: {link1.find("a").text}')

    @staticmethod
    def main():
        bugs = BugsMusic()
        while 1:
            menu = input('0.Exit 1.Input URL 2.Get Ranking 3.GET ARTIST')
            if menu == '0':
                print('exit')
                break
            elif menu == '1':
                bugs.url = input('Input URL')
            elif menu == '2':

                aaa = {"class": "title"}
                bugs.count(bugs, aaa)
            elif menu == '3':

                aaa = {"class": "artist"}
                bugs.count(bugs, aaa)
            else:
                print('Wrong Number')
                continue

# bugs.url = 'https://music.bugs.co.kr/chart/track/realtime/total?wl_ref=M_contents_03_01'
BugsMusic.main()