import csv
dataset1=[]
dataset2=[]
with open ("final.csv","r") as f:
    csvreader=csv.reader(f)
    for row in csvreader:
        dataset1.append(row)
with open ("archive_dataset_sorted1.csv","r") as f:  
    csvreader=csv.reader(f)
    for row in csvreader:
        dataset2.append(row)      
header1=dataset1[0]
planet_data1=dataset1[1:]
header2=dataset2[0]
planet_data2=dataset2[1:]
headers=header1+header2
planet_data=[]
for index,row in enumerate (planet_data1):
    planet_data.append(planet_data1[index]+planet_data2[index])
with open("mergeddata.csv","a+") as f:
    csvwriter=csv.writer(f)
    csvwriter.writerow(headers)
    csvwriter.writerows(planet_data)
