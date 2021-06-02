import pandas as pd
from selenium import webdriver
from bs4 import BeautifulSoup


class NaverStockSamsung(object):

    url = 'https://m.stock.naver.com/index.html#/domestic/capitalization/KOSPI'
    driver = 'C:/Program Files/Google/Chrome/chromedriver'
    class_name = ['VTableComm_name__GNwO8', 'VTableComm_code__3xLPv']
    code_number = []
    code_name = []
    code_dic = {}
    df = None

    def scrap(self):
        chromedriver = webdriver.Chrome(self.driver)
        chromedriver.get(self.url)
        soup = BeautifulSoup(chromedriver.page_source, 'lxml')
        all_span = soup.find_all('span', {'class': self.class_name[0]})
        for i in all_span:
            self.code_name.append(i.text)
        all_span = soup.find_all('span', {'class': self.class_name[1]})
        for i in all_span:
            self.code_number.append(i.text)
        chromedriver.quit()

    def to_dic(self):
        for i in range(len(self.code_number)):
            self.code_dic[f'{i + 1}위'] = self.code_name[i], self.code_number[i]

    def to_dataframe(self):
        self.df = pd.DataFrame(data=self.code_dic, index=['종목', '코드'])
        self.df = self.df.transpose()

    def to_csv(self):
        path = 'data_m_naver_stock/stock.csv'
        self.df.to_csv(path, na_rep='NaN')

    def to_excel(self):
        path = 'data_m_naver_stock/stock.xlsx'
        self.df.to_excel(path, na_rep='NaN')


if __name__ == '__main__':
    nss = NaverStockSamsung()
    nss.scrap()
    nss.to_dic()
    nss.to_dataframe()
    nss.to_csv()
    nss.to_excel()