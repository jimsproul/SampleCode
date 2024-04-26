import csv
#
# Looks like the file has fixed length records
# I converted to a semi-csv file. It works okay for the 
# first few hundred rows. 
# 
# My first step was to drop the file in a hex editor and look at it.
# Looked like a record number in first position
# The rest were simple displacements
#

#
# Looks like the file has fixed length records
# I converted to a semi-csv file. It works okay for the 
# first few hundred rows. 
# 
# My first step was to drop the file in a hex editor and look at it.
# Looked like a record number in first position
# The rest were simple displacements
#

with open('client_date_character.csv',"w") as outfile:
    with open('client_data.bin', 'rb') as file:
        for i in range(1,200):
            b = 0 
            last = b'\x99'
            byte = file.read(1)
            strings = str(int.from_bytes(byte, "big")) + ","
            for a in range(1, 165):
                if a == 4:
                    strings = strings + ","
                if a == 36:
                    strings = strings + ","
                if a == 68:
                    strings = strings + ","    
                if a == 78:
                    strings = strings + ","                    
                if a == 145:
                    strings = strings + "," + str(int.from_bytes(byte, "big")) + ","
                if a == 148:
                    strings = strings + ","      
                b = b+1   
                byte = file.read(1)
                if byte in (b'\x00',b'\xff'):
                    strings = strings + "" 
                else:
                    strings = strings + byte.decode('ascii')
                last = byte
            outfile.write(f"{strings}\n")
            strings = ""
# with open(client_date_character.csv,"rb") as csv_file:
#     csv_rdr = csv.reader(csv_file,delimiter=',')
#     for row in csv_rdr:
#         print(row)
     