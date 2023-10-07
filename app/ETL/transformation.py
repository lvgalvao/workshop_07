import pandas as pd
from typing import List

"""vou criar uma função que consolida uma lista de datraframes em um único dataframe"""

def consolidate_dataframes(dataframes: List[pd.DataFrame]) -> pd.DataFrame:
    """o objetivo dessa função é consolidar uma lista de dataframes em um único dataframe"""
    return pd.concat(dataframes, ignore_index=True)

