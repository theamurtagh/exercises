#Thea Murtagh Irish Dataset format#

with open("irisf.csv") as f: 
    for line in f:
        line = line.rstrip('\n')

        col1 = (line.split(',')[2:4])
        col2 = (line.split(',')[0:2]) 
        print ( col1 + col2 )
