# *****************
# --- Data Type ---
# *****************
'''
Python has Five standard types
scalar
    Numbers : int, float, complex
    String : str
vector : List, Tuple, Dictionary, Set
hello = 'hello'
print(hello)
print(hello[0])
print(hello[2:5])
print(hello[2:])


# List CRUD Example
ls = ['abcd', 786, 2.23, 'john', 70.2]
tinyls = [123, 'john']
# Create: ls 에 '100'을 추가 Create
ls.append('100')
# Read: ls 의 목록을 출력
print(ls)
# Update: ls와 tinyls 의 결합
ls = ls + tinyls
print(ls)
# Delete: ls 에서 786을 제거
del ls[1]
print(ls)
# Tuple CRUD Example
tp = ('abcd', 786, 2.23, 'john', 70.2)
tinytp = (123, 'john')
# Create: tp 에 '100'을 추가 Create
tp = ('abcd', 786, 2.23, 'john', 70.2, '100')
# Read: tp 의 목록을 출력
print(tp)
# Update: tp와 tinytp 의 결합
tp = tp + tinytp
print(tp)
# Delete: tp 에서 786을 제거
tp = {'abcd', 2.23, 'john', 70.2, '100', 123, 'john'}
# dictionary CRUD Example
dt = {'abcd': 786, 'john': 70.2}
tinydt = {'홍': '30세'}
# Create: dt 에 키값으로 'tom', 밸류로 '100'을 추가 Create
dt['tom'] = '100'
# Read: dt 의 목록을 출력
print(dt)
# Update: dt와 tinydt 의 결합
dt.update(tinydt)
print(dt)
# Delete: dt 에서 'abcd' 제거
dt.pop('abcd')
print(dt)
'''


class Vectortest(object):
    ls = ['abcd', 786, 2.23, 'john', 70.2]

    tiny_ls = [123, 'john']

    tp = ('abcd', 786, 2.23, 'john', 70.2)

    tiny_tp = (123, 'john')

    dt = {'abcd': 786, 'john': 70.2}

    tiny_dt = {'홍': '30세'}

    def create_list(self):
        self.ls.append('100')

    def read_list(self):
        print(self.ls)

    def update_list(self):
        ls = self.ls + self.tiny_ls
        print(ls)

    def delete_list(self, aa):
        self.ls.remove(aa)
        print(self.ls)

    def create_tuple(self):
        self.tp = ('abcd', 786, 2.23, 'john', 70.2, '100')

    def read_tuple(self):
        print(self.tp)

    def merge_tuple(self):
        self.tp = self.tp + self.tiny_tp
        print(self.tp)

    def delete_tuple(self):
        self.tp = {'abcd', 2.23, 'john', 70.2, '100', 123, 'john'}
        print(self.tp)

    def create_dic(self):
        self.dt['tom'] = 100

    def read_dic(self):
        print(self.dt)

    def update_dic(self):
        self.dt.update(self.tiny_dt)
        print(self.dt)

    def delete_dic(self, delete):
        self.dt.pop(delete)
        print(self.dt)

    @staticmethod
    def main():
        v = Vectortest()
        while 1:
            m = input('0.break 1.c_l 2.r_l 3.u_l 4.d_l 5.c_t 6.r_t 7.u_t 8.d_t 9.c_d 10.r_d 11.u_d 12.d_d')
            if m == '0':
                break
            elif m == '1':
                v.create_list()
            elif m == '2':
                v.read_list()
            elif m == '3':
                v.update_list()
            elif m == '4':
                print(v.ls)
                aa = input('삭제값')
                v.delete_list(aa)
            elif m == '5':
                v.create_tuple()
            elif m == '6':
                v.read_tuple()
            elif m == '7':
                v.merge_tuple()
            elif m == '8':
                v.delete_tuple()
            elif m == '9':
                v.create_dic()
            elif m == '10':
                v.read_dic()
            elif m == '11':
                v.update_dic()
            elif m == '12':
                print(v.dt)
                dic = input('삭제값')
                v.delete_dic(dic)
            else:
                continue


Vectortest.main()

