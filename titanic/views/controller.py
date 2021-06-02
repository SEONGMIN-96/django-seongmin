from titanic.models.service import Service
from titanic.models.dataset import Dataset


class Controller(object):

    dataset = Dataset()
    service = Service()

    def modeling(self, train, test) -> object:

        this = self.preprocess(train, test)
        return this

    def preprocess(self, train, test) -> object:
        service = self.service
        this = self.dataset
        this.train = service.new_model(train)
        this.test = service.new_model(test)
        this = service.embarked_nominal(this)
        this = service.title_nominal(this)
        this = service.gender_nominal(this)
        this = service.age_ordinal(this)
        this = service.fare_band_fill_na(this)
        this = service.drop_feature(this, 'Sex', 'Name', 'Fare', 'Ticket', 'Cabin')
        self.print_this(this)
        return this

    @staticmethod
    def print_this(this):
        print('<type check>')
        print(f'Train 의 Type 은 {type(this.train)} 이다.')
        print(f'Train 의 상위 5개 행은 {this.train.head()}이다')
        print(f'Train 의 columns 은 {this.train.columns} 이다.')
        print(f'Train 의 null 의 갯수\n {this.train.isnull().sum()}개')
        print('*' * 100)
        print(f'Test 의 Type 은 {type(this.test)} 이다.')
        print(f'Test 의 상위 5개 행은 {this.test.head()}이다')
        print(f'Test 의 columns 은 {this.test.columns} 이다.')
        print(f'Test 의 null 의 갯수\n {this.test.isnull().sum()}개')