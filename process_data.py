from typing import List, Tuple
import pandas as pd
from datetime import datetime
import re
import locale
from dateutil.relativedelta import relativedelta
from config import COLUMNS, KEEP_COLUMNS

def clean_date(x):
    if len(x) < 5:
        x = '01.01.' + x
    return datetime.strptime(x, '%d.%m.%Y').date()

def convert_to_rus_datetime(x):
    locale.setlocale(locale.LC_TIME, 'ru_RU.UTF-8')
    return x.strftime('%d %B %Y')

def create_age(x):
    return str(relativedelta(x['date_of_demise'], x['dob']).years) + ' лет'

def clean_profession(x):
    x = re.sub('по месту рождения,', '', x)
    return x

def process_data(li: List[Tuple]):

    df = pd.DataFrame(li, columns=COLUMNS)[KEEP_COLUMNS]

    df.fillna("неизвестно", inplace=True)
    df['dob'] = df['дата рождения'].map(clean_date)
    df['date_of_demise'] = df['расстрел'].map(clean_date)
    df['rus_demise'] = df['date_of_demise'].map(convert_to_rus_datetime)
    df['age'] = df.apply(lambda x: create_age(x), axis=1)
    df['gender'] = df['пол'].map(lambda x: 1
                                 if x.lower() in ['женщина', 'мженщина', 'женщина; вариант: мужчина']
                                 else 0
                                 ) 
    df['gender_dob'] = df['gender'].map(lambda x: 'Родилась' if x == 1 else 'Родился')
    df['birth_info'] = df.apply(lambda x: x['gender_dob'] + " в " + x['место рождения'],axis=1)
    df['gender_demise'] = df['gender'].map(lambda x: 'Расстреляна' if x == 1 else 'Расстрелян')
    df['demise_info'] = df.apply(lambda x: x['gender_demise'] + ' ' + x['rus_demise'] + " в " + x['место смерти'],axis=1)
    df['профессия / место работы'] = df['профессия / место работы'].map(clean_profession)

    return df
