from typing import List, Tuple
import pandas as pd
from config import COLUMNS


def process_data(li: List[Tuple]):

    df = pd.DataFrame(li, columns=COLUMNS)
    
    return df
