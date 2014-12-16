import csv
import codecs
import os
 # -*- coding: utf-8 -*-

def testRead():
	with codecs.open("C:/Users/jderiggi/Documents/AVANSEDb/Production_Agricole_feb-aug-2013.csv") as csvfile:
		cropset = []
		linereader = csv.DictReader(csvfile, dialect=csv.excel)
		for row in linereader:
			croprow = row['Parcelle.1_Cultures']
			crops = croprow.split(',')
			
			for crop in crops:
				cleancrop = crop.lower().strip()
				if cleancrop not in cropset:
					cropset.append(cleancrop)

		print cropset



testRead()
