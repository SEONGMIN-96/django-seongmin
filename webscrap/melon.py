from bs4 import BeautifulSoup
import requests
import pandas as pd

class Melon(object):
    url = 'https://www.melon.com/chart/index.htm'
    headers = {'User-agent': 'Mozilla/5.0'}
    classname = []
    arist_list = []
    title_list = []
    song_dic = {}
    df = None

    def set_url(self):
        self.url = requests.get(self.url, headers=self.headers).text

    def get_ranking(self):
        soup = BeautifulSoup(self.url, "lxml")
        # 가수
        ls = soup.find_all(name="div", attrs={'class': self.classname[0]})
        for i in ls:
            self.arist_list.append(i.find('a').text)
        # 노래
        ls = soup.find_all(name="div", attrs={'class': self.classname[1]})
        for i in ls:
            self.title_list.append(i.find('a').text)

    def print_dic(self):
        for j in range(100):
            self.song_dic[f'{[j + 1]}위'] = self.title_list[j], self.arist_list[j]
        print(self.song_dic)

    def dic_to_dataframe(self):
        self.df = pd.DataFrame(data=self.song_dic, index=["가수", "노래"])
        self.df = self.df.transpose()
        print(self.df)

    def dataframe_to_csv(self):
        path = './data_melon/mel.csv'
        self.df.to_csv(path, sep=',', na_rep='NaN')

    def dataframe_to_excel(self):
        path = './data_melon/mel.xlsx'
        self.df.to_excel(path, na_rep='NaN')

    @staticmethod
    def main():
        melon = Melon()
        while 1:
            menu = input('0.break 1.Input 2.Output 3.')
            if menu == '0':
                pass
            elif menu == '1':
                melon.classname.append('ellipsis rank01')
                melon.classname.append('ellipsis rank02')
                melon.set_url()
            elif menu == '2':
                melon.get_ranking()
                melon.print_dic()
            elif menu == '3':
                melon.dic_to_dataframe()
                melon.dataframe_to_csv()
                melon.dataframe_to_excel()
            elif menu == '4':
                pass
            else:
                continue

Melon.main()

'''
https://www.melon.com/chart/index.htm
'''