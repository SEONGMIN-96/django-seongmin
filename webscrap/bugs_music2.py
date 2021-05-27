import pandas as pd
from bs4 import BeautifulSoup
import requests

class BugsMusic(object):

    url = 'https://music.bugs.co.kr/chart/track/realtime/total?'

    headers = {'User-Agent': 'Mozilla/5.0'}

    class_name = []

    title_list = []

    artist_list = []

    song_dic = {}

    df = None


    def set_url(self, detail):
        self.url = requests.get(f'{self.url}{detail}', headers=self.headers).text

    def get_ranking(self):
        soup = BeautifulSoup(self.url, 'lxml')
        ls = soup.find_all(name='p', attrs=({"class": self.class_name[1]}))
        for i in ls:
            self.title_list.append(i.find("a").text)
        ls = soup.find_all(name='p', attrs=({"class": self.class_name[0]}))
        for i in ls:
            self.artist_list.append(i.find("a").text)

    def print_dic(self):
        for j in range(100):
            self.song_dic[f'{j + 1}위'] = self.artist_list[j], self.title_list[j]
        print(self.song_dic)

    def dic_to_dataframe(self):
        self.df = pd.DataFrame(data=self.song_dic, index=["가수", "노래"])
        self.df = self.df.transpose()
        print(self.df)

    def dataframe_to_csv(self):
        path = './data/bugs.csv'
        self.df.to_csv(path, sep=',', na_rep='NaN')

    def dataframe_to_excel(self):
        path = './data/bugs1.xlsx'
        self.df.to_excel(path, na_rep='NaN')


    @staticmethod
    def main():
        bugs = BugsMusic()
        while 1:
            menu = input('0-exit, 1-input ex, 2-input stuff 3-to_dic')
            if menu == '0':
                break
            elif menu == '1':
                bugs.set_url(input('상세정보 입력')) # wl_ref=M_contents_03_01
            elif menu == '2':
                bugs.class_name.append("artist")
                bugs.class_name.append("title")
                bugs.get_ranking()
            elif menu == '3':
                bugs.print_dic()
            elif menu == '4':
                bugs.dic_to_dataframe()
            elif menu == '5':
                bugs.dataframe_to_csv()
            elif menu == '6':
                bugs.dataframe_to_excel()
            else:
                print('Wrong Number')
                continue


BugsMusic.main()