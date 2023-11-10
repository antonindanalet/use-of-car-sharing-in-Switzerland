# Use of car sharing in Switzerland

This code computes the modal shares in Switzerland, in particular the share of car sharing, based on 2021 data. The modal shares are defined as daily *distances*.

## Getting Started
These instructions will get you a copy of the project up and running on your local machine for reproducing the result and understanding how it has been generated.

### Prerequisites
To run the code itself, you need python 3 and pandas.

For it to produce the results, you also need the raw data of the Transport and Mobility Microcensus (MTMC) 2021, not included on GitHub. These data are individual data and therefore not open. You can however get them by filling in this form in <a href="https://www.are.admin.ch/are/de/home/verkehr-und-infrastruktur/grundlagen-und-daten/mzmv/datenzugang.html">German</a>, <a href="https://www.are.admin.ch/are/fr/home/mobilite/bases-et-donnees/mrmt/accesauxdonnees.html">French</a> or <a href="https://www.are.admin.ch/are/it/home/mobilita/basi-e-dati/mcmt/accessoaidati.html">Italian</a>. The cost of the data is available in the document "<a href="https://www.are.admin.ch/are/de/home/medien-und-publikationen/publikationen/grundlagen/mikrozensus-mobilitat-und-verkehr-2015-mogliche-zusatzauswertung.html">Mikrozensus Mobilität und Verkehr 2015: Mögliche Zusatzauswertungen</a>"/"<a href="https://www.are.admin.ch/are/fr/home/media-et-publications/publications/bases/mikrozensus-mobilitat-und-verkehr-2015-mogliche-zusatzauswertung.html">Microrecensement mobilité et transports 2015: Analyses supplémentaires possibles</a>".

### Run the code
Please copy the paths to the files etappen.csv and zielpersonen.csv from the Federal Statistical Office in the file 'config.yml' <a href="https://github.com/antonindanalet/modal-split-in-Switzerland/tree/master/data/input/2005/mtmc05">data/input/2005/mtmc05</a>, <a href="https://github.com/antonindanalet/modal-split-in-Switzerland/tree/master/data/input/2010/mtmc10">data/input/2010/mtmc10</a> and <a href="https://github.com/antonindanalet/modal-split-in-Switzerland/tree/master/data/input/2015/mtmc15">data/input/2015/mtmc15</a>. Then run <a href="https://github.com/antonindanalet/modal-split-in-Switzerland/blob/master/src/run_modal_split_in_Switzerland.py">run_modal_split_in_Switzerland.py</a>.

DO NOT commit or share in any way the CSV files etappen.dat, Haushalte.dat, zielpersonen.dat, etappen.csv, haushalte.csv or zielpersonen.csv! These are personal data.
