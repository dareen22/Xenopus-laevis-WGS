import pandas as pd
import numpy as np

### Reading Blue File and Removing unwanted Columns and Renaming the Fixed column
Blue = pd.read_csv('/Users/da2451/Documents/NYUAD/Dareen/NEW/AllelFreqWithScaf_Blue.FIXEDdif.csv')
Blue.drop(['Unnamed: 3'], axis = 1, inplace = True)
Blue.rename(columns={"Fixed": "Fixed_Blue"},inplace = True)
Blue


### Reading Green File and Removing unwanted Columns and Renaming the Fixed column

Green = pd.read_csv('/Users/da2451/Documents/NYUAD/Dareen/NEW/AllelFreqWithScaf_Green_FIXEDdif.csv')
Green.rename(columns={"Fixed": "Fixed_Green"},inplace = True)
Green


### Reading Purple File and Removing unwanted Columns and Renaming the Fixed column

Purple = pd.read_csv('/Users/da2451/Documents/NYUAD/Dareen/NEW/AllelFreqWithScaf_Purple.FIXEDdif.csv')
Purple.drop(['Unnamed: 3'], axis = 1, inplace = True)
Purple.rename(columns={"Fixed": "Fixed_Purple"},inplace = True)
Purple


### Reading Yellow File and Removing unwanted Columns and Renaming the Fixed column

Yellow = pd.read_csv('/Users/da2451/Documents/NYUAD/Dareen/NEW/AllelFreqWithScaf_Yellow.FIXEDdif.csv')
Yellow.drop(['Unnamed: 3'], axis = 1, inplace = True)
Yellow.rename(columns={"Fixed": "Fixed_Yellow"},inplace = True)
Yellow


#Combining the Data Frame one after the other and Placing Missing values as 'False'

Blue_Green = pd.merge(Blue, Green, on= ['CHROM', 'POS'], how = 'outer')
Blue_Green_Purple = pd.merge(Blue_Green, Purple, on= ['CHROM', 'POS'], how = 'outer')
Blue_Green_Purple_Yellow = pd.merge(Blue_Green_Purple, Yellow, on= ['CHROM', 'POS'], how = 'outer')
Blue_Green_Purple_Yellow.fillna('False',inplace=True)
Blue_Green_Purple_Yellow


###  Saving the output
Blue_Green_Purple_Yellow.to_csv('/Users/da2451/Documents/NYUAD/Dareen/NEW/Combined_Results.csv', index = False)

### Fixed the Unique Fixed allele in each of the Conditions in the merged data set and write output to seperate files
Blue_Green_Purple_Yellow_A=Blue_Green_Purple_Yellow.query('Fixed_Blue == "A"  & Fixed_Green == "A" & Fixed_Purple == "A" & Fixed_Yellow == "A"' )
Blue_Green_Purple_Yellow_T=Blue_Green_Purple_Yellow.query('Fixed_Blue == "T"  & Fixed_Green == "T" & Fixed_Purple == "T" & Fixed_Yellow == "T"' )
Blue_Green_Purple_Yellow_G=Blue_Green_Purple_Yellow.query('Fixed_Blue == "G"  & Fixed_Green == "G" & Fixed_Purple == "G" & Fixed_Yellow == "G"' )
Blue_Green_Purple_Yellow_C=Blue_Green_Purple_Yellow.query('Fixed_Blue == "C"  & Fixed_Green == "C" & Fixed_Purple == "C" & Fixed_Yellow == "C"' )

Blue_Green_Purple_Yellow_A.to_csv('/Users/da2451/Documents/NYUAD/Dareen/NEW/Only_A.csv', index = False)
Blue_Green_Purple_Yellow_T.to_csv('/Users/da2451/Documents/NYUAD/Dareen/NEW/Only_T.csv', index = False)
Blue_Green_Purple_Yellow_G.to_csv('/Users/da2451/Documents/NYUAD/Dareen/NEW/Only_G.csv', index = False)
Blue_Green_Purple_Yellow_C.to_csv('/Users/da2451/Documents/NYUAD/Dareen/NEW/Only_C.csv', index = False)

#Displaying Fixed allele A
Blue_Green_Purple_Yellow_A
