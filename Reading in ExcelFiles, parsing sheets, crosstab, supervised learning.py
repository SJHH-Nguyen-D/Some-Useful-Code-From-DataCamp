#import dependencies
import pandas as pd
import numpy as np

#import dataset
data = pd.ExcelFile('ED data for Strat Info Analyst Exercise_DN_Edit.xlsx')

#figure out the sheet names from the ExcelFile
print(data.sheet_names)

#parse the sheet in the dataframe by the sheet index number
data_s1 = data.parse(0)

#series into object
ed_dep = data_s1['ED Departure Disposition']
hosp = data_s1['Hospital']

#cross tab
ct = pd.crosstab(hosp, ed_dep)
print(ct)
