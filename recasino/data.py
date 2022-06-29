"""Data loading functionality."""

import os
from typing import List, Optional

import pandas as pd
import pdpipe as pdp


# --- Schema ---

class Col:
    DATE = 'dt_date_ID'
    USER = 'CID'
    COUNTRY = 'Country_ID'
    GAME = 'GameType_ID'
    VENDOR = 'VendorID'
    BETS = 'Bets'
    WEEK = 'week'
    RATING = 'rating'


# --- paths ---

DATA_DPATH = None


def set_data_dpath(dpath: str) -> None:
    global DATA_DPATH
    DATA_DPATH = dpath


FNAMES = [
    'mayh1.csv',
    'mayh2.csv',
    'juneh1.csv',
    'juneh2.csv',
    'jul2days.csv',
]


def get_raw_dataframe() -> pd.DataFrame:
    """Returns the entire two months dataset as a single dataframe."""
    df = pd.concat([
        pd.read_csv(os.path.join(DATA_DPATH, fname))
        for fname in FNAMES
    ]).sort_values(by=Col.DATE).reset_index(drop=True)
    df[Col.DATE] = pd.to_datetime(df[Col.DATE], format="%Y%m%d")
    return df


