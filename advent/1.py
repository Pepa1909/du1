import csv

with open("1.csv", encoding="utf-8") as csvfile:
    reader = csv.reader(csvfile)
    
    list=[]
    vyssi = 0
    for row in reader:
        list.append(int(row[0]))
        if len(list)>1:
            if list[-1] > list[-2]:
                vyssi += 1
    print(vyssi)
