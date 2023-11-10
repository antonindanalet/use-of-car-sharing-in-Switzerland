import pandas as pd
from pathlib import Path
import yaml

config_path = Path('config.yml')
CONFIG = yaml.safe_load(open(config_path))


def get_zp(year, selected_columns=None):
    if year == 2021:
        with open(Path(CONFIG["path_to_2021_zielpersonen"]), 'r', encoding='latin1') as zielpersonen_file:
            if selected_columns is None:
                df_zp = pd.read_csv(zielpersonen_file, delimiter=';')
            else:
                df_zp = pd.read_csv(zielpersonen_file,
                                    delimiter=';',
                                    dtype={'HHNR': int},
                                    usecols=selected_columns)
    else:
        raise Exception("Cannot get data for other years than 2021! (zp)")
    return df_zp


def get_etappen(year, selected_columns=None):
    if year == 2021:
        with open(Path(CONFIG['path_to_2021_etappen']), 'r', encoding='latin1') as etappen_file:
            df_etappen = pd.read_csv(etappen_file,
                                     sep=';',
                                     dtype={'HHNR': int,
                                            'W_AGGLO_GROESSE2012': int},
                                     usecols=selected_columns)
    else:
        raise Exception("Cannot get data for other years than 2021! (etappen)")
    return df_etappen
