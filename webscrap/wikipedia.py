class Wikipedia(object):

    def __init__(self, url):
        self.url = url

    def __str__(self):
        return self.url

    @staticmethod
    def main():
        while 1:
            menu = input('0.Exit 1.Input URL 2.Print URL')
            if menu == '0':
                break
            elif menu == '1':
                wiki = Wikipedia(input('URL'))
            elif menu == '2':
                print(wiki)
            else :
                continue

Wikipedia.main()
