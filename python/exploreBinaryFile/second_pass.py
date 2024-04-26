import numpy as np
import pandas as pd
#
# ----- Build a data type list from prior exploration
# 
dt = np.dtype([('ID','<u4'),
               ('Last Name',('S32')),
               ('First Name',('S32')),
               ('Date of Birth',('S10')),
               ('Email',('S66')),
               ('Is Active',('<u4')),
                ('Phone Number',('S12')),
                ('Postal Code',('S5')),
               ])
with open('client_data.bin', 'rb') as file:
    buff = file.read()
#
# ----- Buffer the binary file  NOTE: This solution has limited scaling ability
#       and build a dataframe
#     
np_data = np.frombuffer(buff,dt)
df = pd.DataFrame(np_data)
print(df.tail())
#
# ----- Reformat the string columns
#
for col, dtype in df.dtypes.items():
        if dtype == object: 
            df[col] = df[col].str.decode('utf-8').fillna(df[col]) 
#
# ----- The 'Is Active' column(s) need more review. This is a hack
#       to get to binary values. Might be losing data
#
df.loc[df['Is Active'] > 1,'Is Active'] = ' '      
# 
# ----- Reorder the columns to meet the spec
#
df.loc[:,['ID','Email','Date of Birth','Is Active','Phone Number','First Name','Last Name','Postal Code']]
print(df.tail())
#
# ----- Create the csv file output
#
hdr = ['ID','Email','Date of Birth','Is Active','Phone Number','First Name','Last Name','Postal Code']
df.to_csv('client_data.csv', columns = hdr, index = False)
