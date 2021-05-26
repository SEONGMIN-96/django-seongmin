from bs4 import BeautifulSoup
import requests


class BugsMusic(object):

    url = 'https://music.bugs.co.kr/chart/track/realtime/total?'

    headers = {'User-Agent': 'Mozilla/5.0'}

    class_name = []

    title_list = []

    artist_list = []

    song_dic = {}

    key = 0

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
            self.song_dic[self.artist_list[j]] = self.title_list[j]
        print(self.song_dic)


    @staticmethod
    def main():
        bugs = BugsMusic()
        while 1:
            menu = input('0-exit, 1-input time, 2-output 3-to_dic')
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
            else:
                print('Wrong Number')
                continue


BugsMusic.main()