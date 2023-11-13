from pathlib import Path
import pandas as pd
import numpy as np

from utils_mtmc.compute_confidence_interval import get_weighted_avg_and_std
from utils_mtmc.get_mtmc_files import get_zp, get_etappen
from utils_mtmc.codage import *


def run_use_of_car_sharing():
    compute_mode_share(mtmc_year=2021, percentage=False)
    compute_mode_share(mtmc_year=2021, percentage=True)


def compute_mode_share(mtmc_year, percentage):
    if mtmc_year == 2021:
        folder_path_output = Path('output/2021/')
        identification_columns = ['HHNR']
    else:
        raise Exception('Year of the MTMC not well defined! It should be 2021. '
                        'Other years (e.g. 2010, 2015 are not yet coded...')
    list_of_modes = ['A pied', 'Vélo (incl. vélo électrique)', 'Deux-roues motorisé', 'Voiture (car sharing)',
                     'Voiture (autre)', 'Transports publics routiers', 'Train', 'Autres']
    if percentage:
        columns = ['Echantillon']
    else:
        columns = ['Echantillon', 'Total', 'Total (+/-)']
    for mode_simple in list_of_modes:
        columns.extend([mode_simple, mode_simple + ' (+/-)'])
    df_for_csv = pd.DataFrame(columns=columns)
    df_zp = get_zp(year=mtmc_year, selected_columns=identification_columns + ['WP'])  # Get the full list of HHNR
    if mtmc_year == 2021:
        df_etappen = get_etappen(mtmc_year,
                                 selected_columns=identification_columns + ['E_Ausland', 'pseudo', 'rdist',
                                                                            'f51300',  # Transport mode
                                                                            'f51310a'])  # Which car was used
    else:
        raise Exception('Year of the MTMC not well defined! It should be 2021. '
                        'Other years (e.g. 2010, 2015) are not coded yet...')
    df_etappen = df_etappen[df_etappen.E_Ausland == 2]  # Remove trips abroad
    del df_etappen['E_Ausland']
    df_etappen = df_etappen[df_etappen.pseudo == 1]  # Remove pseudo trip legs
    del df_etappen['pseudo']
    if mtmc_year == 2021:
        df_etappen['transport_mode'] = df_etappen['f51300'].map(dict_detailed_mode2main_mode_2021)
    else:
        raise Exception('Year of the MTMC not well defined! It should be 2021. '
                        'Other years (e.g. 2010, 2015) are not coded yet...')
    del df_etappen['f51300']
    df_etappen.rename(columns={'f51310a': 'car_used'}, inplace=True)

    ''' Decompose "car" into "car (car sharing)" and "car (other) '''
    df_etappen.loc[(df_etappen['transport_mode'] == 'Voiture') & (df_etappen['car_used'] == 4),
                   'transport_mode'] = 'Voiture (car sharing)'
    df_etappen.loc[(df_etappen['transport_mode'] == 'Voiture') & (df_etappen['car_used'] != 4), 'transport_mode'] = 'Voiture (autre)'

    ''' Add non-mobile HHNR/ZP '''
    df_etappen = pd.merge(df_etappen, df_zp[identification_columns],
                          left_on=identification_columns, right_on=identification_columns, how='right')
    df_etappen['rdist'].fillna(0, inplace=True)  # Replace NAN by 0
    df_etappen['transport_mode'].fillna('Autres', inplace=True)  # Replace NAN by 'Autres'

    # Results for Switzerland
    dict_total_km, sample = compute_distances_and_confidence_interval_total(df_etappen, df_zp,
                                                                            identification_columns)
    dict_km_per_mode = compute_distances_and_conf_interval_per_mode(df_etappen, df_zp,
                                                                    percentage=percentage,
                                                                    identification_columns=identification_columns,
                                                                    list_of_modes=list_of_modes)
    dict_km_per_mode['Echantillon'] = sample
    if percentage is False:
        dict_km_per_mode.update(dict_total_km)
    df_dict_km_per_mode = pd.DataFrame([dict_km_per_mode])  # Transform the dictionary into a dataframe for concatenate
    df_for_csv = pd.concat([df_for_csv, df_dict_km_per_mode], ignore_index=True)

    for mode_simple in list_of_modes:
        df_for_csv[mode_simple].fillna(0, inplace=True)
        df_for_csv[mode_simple + ' (+/-)'].fillna('-', inplace=True)

    # File names
    if percentage:
        new_file_name = 'Parts_moyen_de_transport_pourcentage_' + str(mtmc_year) + '.csv'
    else:
        new_file_name = 'Parts_moyen_de_transport_' + str(mtmc_year) + '.csv'
    # Save in folder output
    df_for_csv.to_csv(folder_path_output / new_file_name, index=False, sep=',', encoding='iso-8859-1')


def compute_distances_and_conf_interval_per_mode(df_etappen, df_zp, identification_columns, percentage, list_of_modes,
                                                 full_sample=False):
    if percentage and list_of_modes == []:  # Percentage, without definition of list of modes!
        raise Exception('Warning: Try to compute percentage without a clear definition of the list of modes!',
                        list_of_modes)
    dict_of_results = {}
    table = pd.pivot_table(df_etappen, values='rdist', index=identification_columns, columns=['transport_mode'],
                           aggfunc=np.sum)
    if full_sample:
        table = table.reindex(df_zp['HHNR'])
    table.fillna(0, inplace=True)
    # Add the weight to the pivot table
    result = pd.merge(table, df_zp, left_index=True, right_on=identification_columns, how='left')
    dict_column_weighted_avg_and_std, sample = get_weighted_avg_and_std(result, percentage=percentage, weights='WP',
                                                                        list_of_columns=list_of_modes)
    for mode_simple in list_of_modes:
        if mode_simple in dict_column_weighted_avg_and_std:
            dict_of_results[mode_simple] = dict_column_weighted_avg_and_std[mode_simple][0]
            dict_of_results[mode_simple + ' (+/-)'] = dict_column_weighted_avg_and_std[mode_simple][1]
    return dict_of_results


def compute_distances_and_confidence_interval_total(df_etappen, df_zp, identification_columns, full_sample=False):
    dict_results = {}
    # Get the distance (rdist) by person
    table = pd.pivot_table(df_etappen, values='rdist', index=identification_columns, aggfunc=np.sum)
    if full_sample:
        table = table.reindex(df_zp['HHNR'])
        table.fillna(0, inplace=True)
    # Add the weight to the pivot table
    result = pd.merge(table, df_zp, left_index=True, right_on=identification_columns)
    dict_column_weighted_avg_and_std, sample = get_weighted_avg_and_std(result, weights='WP')
    dict_results['Total'] = dict_column_weighted_avg_and_std['rdist'][0]
    dict_results['Total (+/-)'] = dict_column_weighted_avg_and_std['rdist'][1]
    return dict_results, sample


if __name__ == '__main__':
    run_use_of_car_sharing()
