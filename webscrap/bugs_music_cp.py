from bs4 import BeautifulSoup
import requests




class Melon(object):
    url = ''
    headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 6.3; Trident/7.0; rv:11.0) like Gecko'}

    @staticmethod
    def main():
        melon = Melon()
        while 1:
            menu = int(input('0.Exit  1.Input URL 2.Title Ranking 3.Artist Ranking'))
            if menu == 0:
                break
            elif menu == 1:
                melon.url = requests.get(input('URL 입력'), headers=melon.headers).text
            elif menu == 2:
                soup = BeautifulSoup(melon.url, 'lxml')
                count = 0
                for i in soup.find_all("div", {"class":"ellipsis rank01"}):
                    count += 1
                    print(f'{str(count)} 위')
                    print(f' Title: {i.find("a").text}')
            elif menu == 3:
                soup = BeautifulSoup(melon.url, 'lxml')
                count = 0
                for i in soup.find_all("div", {"class":"ellipsis rank02"}):
                    count += 1
                    print(f'{str(count)} 위')
                    print(f'Artist: {i.find("a").text}')
            else:
                print('다시 입력하세요')
                continue


                # https://www.melon.com/chart/index.htm
Melon.main()