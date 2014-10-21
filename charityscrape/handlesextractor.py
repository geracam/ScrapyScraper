import csv
import re

duplicates= open("twitterhandles.csv")

csv_duplicates = csv.reader(duplicates)

"""
extracts the handles from long links

"""
handles= []
for row in csv_duplicates:
	if len(row) > 0:

		
		handles.append([re.search("[^/]*$", row[0]).group(0)])

print handles

duplicates.close()
fileObj= open("/Users/geracam/chrtwtscraper/charityscrape/twitter_handles.csv", "wb")
csv_file= csv.writer(fileObj)
csv_file.writerows(handles)


		


