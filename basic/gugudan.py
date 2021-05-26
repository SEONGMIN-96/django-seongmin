'''
구구단 프로그램은 단을 입력받아서, 입력받은 단의  1 ~ 9의 곱을 출력하는 어플리케이션이다.
단, 단은 정수이다.
'''


class Gugudan(object):
    dan = 0
    dic = {}

    def dan_dan(self):
        for i in range(1, 10):
            print(f'{self.dan} * {i} = {self.dan * i}')


    def all_dan(self):
        for i in range(2, 10):
            for j in range(1, 10):
                print(f'{i} * {j} = {i * j}')

    def dic_dan(self):
        d = self.dic
        for i in range(1, 10):
            d[i] = self.dan * i
        print('딕셔너리 출력')
        print(d)
        for k in d.keys():
            print(f'{self.dan} * {k} = {d.get(k)}')
    @staticmethod
    def main():
        gu_gu = Gugudan()
        while 1:
            m = input('0.break 1.input 2.all 3.input dan with dict')
            if m == '0':
                break
            elif m == '1':
                gu_gu.dan = int(input('단입력: '))
                gu_gu.dan_dan()
            elif m == '2':
                gu_gu.all_dan()
            elif m == '3':
                gu_gu.dan = int(input('단 입력'))
                gu_gu.dic_dan()
            else :
                continue


Gugudan.main()
