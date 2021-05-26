from bs4 import BeautifulSoup
import requests


class Bugsmusic(object):

    url = 'https://music.bugs.co.kr/chart/track/realtime/total?'

    hdr = {'User-Agent': 'Mozilla/5.0'}

    class_name = []

    title_list = []

    artist_list = []

    chart_dic = {}

    def set_url(self):
        self.url = requests.get(self.url, header=self.hdr).text

    def get_ranking(self):
        soup = BeautifulSoup(self.url, "lxml")
        ls = soup.find_all(name='p', attrs=({"class": self.class_name[0]}))
        for i in ls:
            self.title_list.append(i.find("a").text)
        ls = soup.find_all(name='p', attrs=({"class": self.class_name[1]}))
        for i in ls:
            self.artist_list.append(i.find("a").text)

    def print_dic(self):
        for j in range(100):
            self.chart_dic[self.title_list[j]] = self.artist_list[j]
        print(self.chart_dic)


    @staticmethod
    def main():
        bugs = Bugsmusic()
        while 1:
            m = input('0.e 1.i 2.o')
            if m == '0':
                break
            elif m == '1':
                bugs.url = input('추가입력') # wl_ref=M_contents_03_01
            elif m == '2':
                bugs.class_name.append('title')
                bugs.class_name.append('artist')
                bugs.get_ranking()
            elif m == '3':
                bugs.print_dic()
            else:
                continue


Bugsmusic.main()