class Conversion(object):
    i = 0
    f = 0.0
    s = ''
    ls = []
    t = ()
    d = {}
    f_ls = []
    int_ls = []
    hello = 'hello'
    hello_t = ()
    hello_ls = []

    def ten_t(self):
        self.ls = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
        self.t = tuple(self.ls)
        return self.t

    def ten_ls(self):
        self.ls = list(self.t)
        return self.ls

    def ten_f(self):
        for i in range(10):
            self.f_ls.append(float(self.ls[i]))
        return self.f_ls

    def ten_int(self):
        for i in range(10):
            self.int_ls.append(int(self.f_ls[i]))
        return self.int_ls

    def ten_d(self):
        for i in range(10):
            self.d[str(i)] = self.int_ls[i]
        return self.d

    def hello_tu(self):
        self.hello_t = tuple(list(self.hello))
        return self.hello_t

    def hello_to_ls(self):
        self.hello_ls = (list(self.hello_t))
        return self.hello_ls

    @staticmethod
    def main():
        c = Conversion()
        while 1:
            m = input('0-exit 1-create tuple\n'
                      '2-convert list\n'
                      '3-convert float-list\n'
                      '4-convert int-list\n'
                      '5-list convert dictionary\n'
                      '6-str convert tuple\n'
                      '7-str tuple convert list')
            if m == '0':
                break
            # 1부터 10까지 요소를 가진 튜플을 생성하시오 (return)
            elif m == '1':
                print(c.ten_t())
            # 1번 튜플을 리스트로 전환하시오 (return)
            elif m == '2':
                print(c.ten_ls())
            # 2번 리스트를 실수(float) 리스트 바꾸시오  (return)
            elif m == '3':
                print(c.ten_f())
            # 3번 실수(float) 리스트을, 정수 리스트로 바꾸시오  (return)
            elif m == '4':
                print(c.ten_int())
            # 4번 리스트를 딕셔너리로 전환하시오. 단 키는 리스트의 인덱스인데 str 로 전환하시오 (return)
            elif m == '5':
                print(c.ten_d())
            # 'hello' 를 튜플로 전환하시오
            elif m == '6':
                print(c.hello_tu())
            # 6번 튜플을 리스트로 전환하시오
            elif m == '7':
                print(c.hello_to_ls())
            else:
                continue


Conversion.main()