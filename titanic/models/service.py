from titanic.models.dataset import Dataset
import pandas as pd
import numpy as np
from sklearn.svm import SVC
from sklearn.model_selection import KFold
from sklearn.model_selection import cross_val_score
from sklearn.ensemble import RandomForestClassifier

class Service(object):

    dataset = Dataset()

    def new_model(self, payload) -> object:
        this = self.dataset
        this.context = './data/'
        this.fname = payload
        return pd.read_csv(this.context + this.fname)

    @staticmethod
    def create_train(this) -> object:
        return this.train.drop('Survived', axis=1)

    @staticmethod
    def create_label(this) -> object:
        return this.train['Survived']

    @staticmethod
    def drop_feature(this, *feature) -> object:
        for these in feature:
            this.train = this.train.drop([these], axis=1)
            this.test = this.test.drop([these], axis=1)
        return this

    @staticmethod
    def title_nominal(this) -> object:
        combine = [this.train, this.test]
        for i in combine:
            i['Title'] = i.Name.str.extract('([A-Za-z]+)\.', expand=False)
            i['Title'] = i['Title'].replace(['Capt', 'Col', 'Don', 'Dr', 'Major', 'Rev', 'Jonkheer', 'Dona'], 'Rare')
            i['Title'] = i['Title'].replace(['Countess', 'Lady', 'Sir'], 'Royal')
            i['Title'] = i['Title'].replace('Mlle', 'Mr')
            i['Title'] = i['Title'].replace('Ms', 'Miss')
            i['Title'] = i['Title'].replace('Mme', 'Rare')
            title_mapping = {'Mr': 1, 'Miss': 2, 'Mrs': 3, 'Master': 4, 'Royal': 5, 'Rare': 6}
            i['Title'] = i['Title'].fillna(0)
            i['Title'] = i['Title'].map(title_mapping)
        return this

    @staticmethod
    def embarked_nominal(this) -> object:
        this.train = this.train.fillna({'Embarked':'S'})
        this.test = this.test.fillna({'Embarked':'S'})
        embarked_mapping = {'S': 1, 'C': 2, 'Q': 3}
        print(f'타입체크 {type(this.train["Embarked"])}')
        this.train['Embarked'] = this.train['Embarked'].map(embarked_mapping)
        this.test['Embarked'] = this.test['Embarked'].map(embarked_mapping)
        # map 함수를 사용하여 S:1, C:2, Q:3
        return this

        # print(this.test[this.test.isna().any(axis=1)]) null값 찾기
    @staticmethod
    def fare_band_fill_na(this) -> object:
        this.test['Fare'] = this.test['Fare'].fillna(1)

        this.train['FareBand'] = pd.qcut(this.train['Fare'], 4, [1, 2, 3, 4])
        bins = [-1, 8, 15, 31, np.inf]
        this.test['FareBand'] = pd.cut(this.test['Fare'], bins, labels=[1, 2, 3, 4])
        return this

    @staticmethod
    def gender_nominal(this) -> object:
        combine = [this.train, this.test]
        for i in combine:
            gender_mapping = {'male': 0, 'female': 1}
            i['Gender'] = i['Sex'].map(gender_mapping)
        return this

    @staticmethod
    def age_ordinal(this) -> object:
        train = this.train
        test = this.test
        combine = [train, test]
        for i in combine:
            i['Age'] = i['Age'].fillna(-0.5)
            bins = [-1, 0, 5, 12, 18, 24, 35, 60, np.inf]
            labels = ['Unknown', 'Baby', 'Child', 'Teenager', 'Student', 'Young Adult', 'Adult', 'Senior']
            i['AgeGroup'] = pd.cut(i['Age'], bins=bins, labels=labels)
            age_title_mapping = {'Unknown': 0, 'Baby': 1, 'Child': 2, 'Teenager': 3, 'Student': 4, 'Young Adult': 5,
                                 'Adult': 6, 'Senior': 7}
            i['AgeGroup'] = i['AgeGroup'].map(age_title_mapping)
        return this

    @staticmethod
    def create_k_fold() -> object:
        return KFold(n_splits=10, shuffle=True, random_state=0)

    @staticmethod
    def accuracy_by_svm(this):
        score = cross_val_score(RandomForestClassifier(),
                                this.train,
                                this.label,
                                cv=KFold(n_splits=10,
                                         shuffle=True,
                                         random_state=0),
                                n_jobs=1,
                                scoring='accuracy')
        return round(np.mean(score) * 100, 2)