import requests
from bs4 import BeautifulSoup


class Bugsmusic(object):

    url = 'https://music.bugs.co.kr/chart/track/realtime/total'

    hdr = {'User-Agent': 'aaa'}

    class_name = []

    def set_url(self):
        self.url = requests.get(self.url, headers=self.hdr).text

    def get_ranking(self):
        soup = BeautifulSoup(self.url, "lxml")
        print('--------제목--------')
        ls = soup.find_all(name="class", attrs={"class": self.class_name})
        for i in ls:
            print(i.find("a").text)


    @staticmethod
    def main():
        bugs = Bugsmusic()
        while 1:
            m = input('0. 1. 2.')
            if m == '0':
                break
            elif m == '1':
                bugs.url = input('상세정보 입력')  # ?wl_ref=M_contents_03_01
            elif m == '2':
                bugs.class_name.append(input('artist'))
                bugs.class_name.append(input('title'))
                bugs.get_ranking()
            else:
                continue


Bugsmusic.main()