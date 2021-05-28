from selenium import webdriver
from bs4 import BeautifulSoup
import pandas as pd

class Naver(object):

    url = 'https://movie.naver.com/movie/sdb/rank/rmovie.nhn'
    driver = 'C:/Program Files/Google/Chrome/chromedriver'
    class_name = []
    title_list = []
    movie_dic = {}
    df = None

    def scrap(self):
        chromedriver = webdriver.Chrome(self.driver)
        chromedriver.get(self.url)
        soup = BeautifulSoup(chromedriver.page_source, 'html.parser')
        all_div = soup.find_all('div', {'class': self.class_name[0]})
        for i in all_div:
            self.title_list.append(i.find('a').text)
        chromedriver.quit()

    def to_dic(self):
        for i in range(50):
            self.movie_dic[f'{i + 1}위'] = self.title_list[i]
        print(self.movie_dic)

    def to_dataframe(self):
        self.df = pd.DataFrame(data=self.movie_dic, index=['제목'])
        self.df = self.df.transpose()

    def to_csv(self):
        path = './data_naver_movie/naver.csv'
        self.df.to_csv(path, sep=',', na_rep="NaN")

    def to_excel(self):
        path = './data_naver_movie/naver.xlsx'
        self.df.to_excel(path, na_rep="NaN")


if __name__ == '__main__':
    n = Naver()
    n.class_name.append(input('class 값'))
    n.scrap()
    n.to_dic()
    n.to_dataframe()
    n.to_csv()
    n.to_excel()

    #classname: tit3