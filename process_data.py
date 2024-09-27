from typing import List, Tuple
import pandas as pd
from datetime import datetime
from dateutil.relativedelta import relativedelta
from config import COLUMNS, KEEP_COLUMNS

def process_data(li: List[Tuple]):

    df = pd.DataFrame(li, columns=COLUMNS)[KEEP_COLUMNS]
    df['dob'] = df['дата рождения'].map(lambda x: "01.01."+x if len(x) < 5 else x)
    df['dob'] = df.dob.map(lambda x: datetime.strptime(x, '%d.%m.%Y').date())
    df['date_of_demise'] = df['расстрел'].map(lambda x: datetime.strptime(x, '%d.%m.%Y').date())
    df['age'] = df.apply(lambda x: relativedelta(x['date_of_demise'], x['dob']).years,axis=1)
    df['gender'] = df['пол'].map(lambda x: 1
                                 if x.upper() in ['женщина', 'мженщина', 'женщина; вариант: мужчина']
                                 else 0
                                 ) 
    df['gender_dob'] = df['gender'].map(lambda x: 'Родилась' if x == 1 else 'Родился')
    df['gender_demise'] = df['gender'].map(lambda x: 'Расстреляна' if x == 1 else 'Расстрелян')

    return df
