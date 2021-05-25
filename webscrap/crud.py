class Crud(object):
    def __init__(self, id, pw, name, email):
        self.id = id
        self.pw = pw
        self.name = name
        self.email = email

    def to_string(self):
        return self.id, self.pw, self.name, self.email

    def join(self):
        pass

    def update(self):
        pass

    def login(self):
        pass

    @staticmethod
    def main():
        while 1:
            menu = input("0. 1. 2.")
            if menu == '0':
                break
            elif menu == '1':
                pass
            elif menu == '2':
                pass
            else :
                print('Wrong Number')
                continue


Crud.main()