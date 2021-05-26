from bs4 import BeautifulSoup
import requests


class Melon(object):

    url = 'https://www.melon.com/chart/index.htm'
    hdr = {'User-Agent': 'Mozilla/5.0 (Windows NT 6.3; Trident/7.0; rv:11.0) like Gecko'}
    classname = []
    title_list = []
    artist_list = []

    def set_url(self):
        self.url = requests.get(self.url, headers=self.hdr).text

    def get_ranking(self):
        soup = BeautifulSoup(self.url, "lxml")
        for i in soup.find_all(name="div", attrs={"class": self.classname[0]}):
            self.title_list.append(i.find("a").text)
        for i in soup.find_all(name="div", attrs={"class": self.classname[1]}):
            self.artist_list.append(i.find("a").text)

    def chart_dic(self):
        for i, j in zip(self.title_list, self.artist_list):
            self.chart_dic[i] = j
        rank = 0
        for i in self.chart_dic.keys():
            rank += 1
            print(f'{rank}\ {i} - {self.chart_dic[i]}')

    @staticmethod
    def main():
        melon = Melon()
        while 1:
            menu = input('0. 1.Input URL 2.Output')
            if menu == '1':
                melon.set_url()
            elif menu == '2':
                melon.classname.append("ellipsis rank01")
                melon.classname.append("ellipsis rank02")
                melon.get_ranking()
            elif menu == '3':
                melon.chart_dic()
            else :
                continue


Melon.main()

'''
https://www.melon.com/chart/index.htm
'''