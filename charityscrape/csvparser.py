import csv
import re

duplicates= open("duplicates3.csv")

csv_duplicates = csv.reader(duplicates)

"""
row[0]= Charity Name

"""
information = []
charityDict = {}
row_number = 0
for row in csv_duplicates:
	print row
	if row[5] in charityDict.keys():
		position_list= charityDict[row[5]]
		if information[position_list][2] == '':
			information[position_list][2] = row[2]
		else:
			pass



	else:
		information.append(row)
		charityDict[row[5]] = row_number
		row_number += 1
duplicates.close()
fileObj= open("/Users/geracam/chrtwtscraper/charityscrape/noduplicates2.csv", "wb")
csv_file= csv.writer(fileObj)
csv_file.writerows(information)


		


