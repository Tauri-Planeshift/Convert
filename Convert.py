import json
import sys
import os
from scipy.io import arff
import pandas as pd

if len(sys.argv) != 2:
    print('Error need the file')
    sys.exit(1)

try:
        
        with open(sys.argv[1], "r") as file:
            data = file.readlines()
            name,ext = os.path.splitext(file.name)
            
            csvSwitch = False
            header = ""
            newCsv = []
            newJson = {}
            
            
            for line in data:
                if not csvSwitch:
                    if "@attribute" in line:
                        attri = line.split()
                        column = attri[attri.index("@attribute")+1]
                        header = header + column + ","
                    elif "@data" in line:
                        csvSwitch = True
                        header = header[:-1]
                        header += '\n'
                        newCsv.append(header)            
                else:
                    newCsv.append(line)

                    
            
            i = 0
            
            i = len(newCsv)
            
            
            txt = "hello, my name is Peter, I am 26 years old"

            x = txt.split(",")

            print(x[0])
            
            
            
            
            with open(name + ".csv", "w") as filecsv:
                filecsv.writelines(newCsv)
                
               


            with open(name + ".json", 'w') as filejson:  
                json.dump(dataJson, filejson)
            
        
         
       
        




except FileNotFoundError:
            print('404 FILE NOT FOUND')
            exit(1)
            
            
            
         
