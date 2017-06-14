#Import packages
import pandas as pd
import datetime
import numpy as np

#Import Data
df1 = pd.read_excel('Tab_Villages_Mapping.xlsx','Sheet1',dtypes=['int','int','str','str','str','str'])
df2 = pd.read_excel('Tab_Villages_Mapping.xlsx','Sheet2',dtypes=['str','str','str','int','str','str'])

#Change Data Types
df2['Survey Start Date'] = df2['Survey Start Date'].apply(lambda x: datetime.datetime.strptime(str(x),'%d-%b-%Y'))
df2['Survey End Date'] = df2['Survey End Date'].apply(lambda x: datetime.datetime.strptime(str(x),'%d-%b-%Y'))

#Fill in the missing data
#df2 contains missing data that which will be inserted in df1
print("Starting Line-by-Line processing....")
print("\nLines Processed ....")

for i in range(len(df1)):
    
    print(i+1)
    
    #initialize useful strings
    ac = np.nan
    mandal = np.nan
    village = np.nan
    
    #Define the costraints
    tab_no = df1['Tab No'][i]
    date = df1['Survey Date'][i]
    
    #Extract relevant values using the constraints of tab number and dates.
    
    try:
        df = df2.loc[df2['Tab No'] == tab_no].loc[df2['Survey Start Date'] <= date].loc[df2['Survey End Date'] >= date]
        #print (df)
        #AC Name
        ac = df['AC Name'].values[0]
        #print (ac)
        #Mandal Name
        mandal = df['Mandal Name'].values[0]
        #Village Name
        village = df['Village Name'].values[0]
    except:
        pass
    
    #Insert the values in the first dataset
    
    df1['AC Name'].loc[i] = ac
    df1['Mandal Name'].loc[i] = mandal
    df1['Village Name'].loc[i] = village

#Print total number of rows processed to the console    
print("Total number of rows processed - " +str(i))

df1.to_excel('Tab_Villages_Mapping.xlsx',sheet_name='CompleteData')