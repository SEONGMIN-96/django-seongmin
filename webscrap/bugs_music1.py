from bs4 import BeautifulSoup
import requests


class BugsMusic(object):

    url = '' 

    hdr = {'User-agent': ''}

    @staticmethod
    def main():
        bugs = BugsMusic()
        while 1:
            menu = input('0. 1. 2.')
            if menu == '0':
                break
            elif menu == '1':
                bugs.url = requests.get(input('Input URL'), headers=bugs.hdr).text
            elif menu == '2':
                soup = BeautifulSoup(bugs.url, "lxml")
                for i in soup(name="p", attrs={'class': 'artist'}):
                    print(i.find("a").text)
            else:
                continue


BugsMusic.main()

'''
https://music.bugs.co.kr/chart/track/realtime/total?wl_ref=M_contents_03_01
'''