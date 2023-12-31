# Use of car sharing in Switzerland

This code computes the modal shares in Switzerland, in particular the share of car sharing, based on 2021 data. The modal shares are defined as daily *distances*.

Results can be found as CSV files in the folder '<a href="https://github.com/antonindanalet/use-of-car-sharing-in-Switzerland/tree/master/output/2021">output/2021</a>':
- as <a href="https://github.com/antonindanalet/use-of-car-sharing-in-Switzerland/blob/master/output/2021/Parts_moyen_de_transport_2021.csv">absolute distances</a> or 
- as <a href="https://github.com/antonindanalet/use-of-car-sharing-in-Switzerland/blob/master/output/2021/Parts_moyen_de_transport_pourcentage_2021.csv">relative percentages</a>.

Car sharing represents 0.11% of the average daily distance within Switzerland made by the resident population (33 meters out of 30 kilometers). It corresponds to 0.16% of the distance covered by car (33 meters out of 21 kilometers).

## Getting Started
These instructions will get you a copy of the project up and running on your local machine for reproducing the result and understanding how it has been generated.

### Prerequisites
To run the code itself, you need python 3 and pandas.

For it to produce the results, you also need the raw data of the Transport and Mobility Microcensus (MTMC) 2021, not included on GitHub. These data are individual data and therefore not open. You can however get them by filling in this form in <a href="https://www.are.admin.ch/are/de/home/verkehr-und-infrastruktur/grundlagen-und-daten/mzmv/datenzugang.html">German</a>, <a href="https://www.are.admin.ch/are/fr/home/mobilite/bases-et-donnees/mrmt/accesauxdonnees.html">French</a> or <a href="https://www.are.admin.ch/are/it/home/mobilita/basi-e-dati/mcmt/accessoaidati.html">Italian</a>. The cost of the data is available in the document "<a href="https://www.are.admin.ch/dam/are/de/dokumente/verkehr/dokumente/mikrozensus/mzmv-zusatzauswertungen2021.pdf.download.pdf/Zusatzauswertungen%20MZMV%202021%20DE.pdf">Mikrozensus Mobilität und Verkehr - Mögliche Zusatzauswertungen</a>"/"<a href="https://www.are.admin.ch/dam/are/fr/dokumente/verkehr/dokumente/mikrozensus/mzmv-zusatzauswertungen2021.pdf.download.pdf/Zusatzauswertungen%20MZMV%202021%20FR.pdf">Microrecensement mobilité et transports - Analyses supplémentaires possibles</a>".

### Run the code
Please copy the paths to the files etappen.csv and zielpersonen.csv from the Federal Statistical Office in the file <a href="https://github.com/antonindanalet/use-of-car-sharing-in-Switzerland/blob/master/config.yml">config.yml</a> located in the root directory. Then run <a href="https://github.com/antonindanalet/use-of-car-sharing-in-Switzerland/blob/master/src/run_use_of_car_sharing.py">run_use_of_car_sharing.py</a> in the 'src' folder.

DO NOT commit or share in any way the CSV files etappen.csv or zielpersonen.csv! These are personal data.
