import csv
import codecs
import os
# -*- coding: utf-8 -*-



def testRead():
	with codecs.open("C:/Users/jderiggi/Documents/AVANSEDb/menage2.csv") as csvfile:

		linereader = csv.DictReader(csvfile, dialect=csv.excel)
		badVals = loadSynos('C:/Users/jderiggi/Documents/AVANSEDb/communesynonyms/')
		allRows = []
		for row in linereader:
			found = False
			if 'Commune' in row:
				commune = row['Commune'].lower().strip()
				for pair in badVals:
					if commune == pair[0]:
						commune = pair[1]

			# print row
			newRow = []
			avid = row['ID']
			dateEnquette = row['surveydate']
			habitation = row['localite']	
			section = row['section']	
			department = row['department']	
			chefmenage = row['Nom Chef de Menage']	
			bassin = row['Bassin Versant']	
			
			newRow.append(avid)
			newRow.append(dateEnquette)
			newRow.append(habitation)
			newRow.append(section)
			newRow.append(department)
			newRow.append(chefmenage)
			newRow.append(bassin)
			newRow.append(commune)
			
			allRows.append(newRow)

	return allRows;

def loadRiverName():
	
	with open('C:/Users/jderiggi/Documents/AVANSEDb/communesynonyms/a5.csv','r') as riverfile:
		best = riverfile.read().splitlines()[0]
		
	riverfile.close();

	return best;

def cleanCommuneRules(commune):
	allCommunes =  loadCommuneList()
	grand = allCommunes[1]
	troudunord = allCommunes[11]
	oua = allCommunes[9]
	aculdunord = allCommunes[6]
	baslimbe = allCommunes[13]
	fortliberte = allCommunes[0]
	grisongarde = allCommunes[19]
	limbe = allCommunes[14]
	caracol = allCommunes[15]
	labrueyere = allCommunes[20]
	

	if commune.strip().replace(' ','').rfind('ac') == 0:
		commune = aculdunord

	elif commune.rfind('tro') == 0:
		commune = troudunord

	elif commune.rfind('fort') == 0:
		commune = fortliberte

	elif commune.rfind('bas') == 0:
		commune = baslimbe

	elif commune.rfind('ba-lim') == 0:
		commune = baslimbe

	elif commune.rfind('cara') == 0:
		commune = caracol

	elif commune.rfind('oua') == 0:
		commune = oua

	elif commune.rfind('oun') == 0:
		commune = oua

	elif commune.rfind('oan') == 0:
		commune = oua

	elif commune.rfind('labru') == 0:
		commune = labrueyere

	elif commune.rfind('lim') == 0:
		commune = limbe

	elif commune.rfind('gris') == 0:
		commune = grisongarde

	elif commune.rfind('griz') == 0:
		commune = grisongarde

	elif commune.rfind('grand') == 0:
		commune = grand
	
	elif commune.rfind('grande-r') == 0:
		commune = grand

	elif commune.rfind('grnde') == 0:
		commune = grand

	elif commune.rfind('gde-r') == 0:
		commune = grand

	elif commune.rfind('gde r') == 0:
		commune = grand
	
	elif commune.rfind('gde_r') == 0:
		commune = grand


	elif commune.rfind('g-riv') == 0:
		commune = grand

	elif commune.rfind('grane') == 0:
		commune = grand

	elif commune.rfind('grnade') == 0:
		commune = grand
		

	return commune


def cleanDistroList2():
	with open("C:/Users/jderiggi/Documents/AVANSEDb/distributionlist/distribution.csv" , 'r') as dirtydistro:
		lines = dirtydistro.read().splitlines()
		outfile = codecs.open('C:/Users/jderiggi/Documents/AVANSEDb/output/homegrowndistro.csv', 'a', 'utf-8-sig')
		for line in lines:
			# print line.split(',')[7].decode('utf-8')
			name = line.split(',')[7].decode('utf-8')
			outfile.write(name + '\n')

		outfile.close()	
		dirtydistro.close()
	

def loadCommuneList():
	with codecs.open("C:/Users/jderiggi/Documents/AVANSEDb/communesynonyms/allCommunes.csv" , 'r') as csvfile:
		lines=  csvfile.read().splitlines()
	csvfile.close()
	return lines;



def cleanDistroList():
	with codecs.open("C:/Users/jderiggi/Documents/AVANSEDb/distributionlist/distribution.csv" , 'r') as csvfile:

		linereader = csv.DictReader(csvfile, dialect=csv.excel)
		badVals = loadSynos('C:/Users/jderiggi/Documents/AVANSEDb/communesynonyms/')
		allRows = []
		for row in linereader:
			found = False
			if 'Commune' in row:
				
				commune = row['Commune'].lower().strip()
				# todo fix the other synonym files by saving them with bom
				# for pair in badVals:
				# 	if commune == pair[0]:
				# 		commune = pair[1]

				commune = cleanCommuneRules(commune)

			# print row
			newRow = []
			# avid = row['ID']
			distributionDate = row['distributiondate']
			nom = row['completename']	
				
			
			newRow.append(distributionDate)
			newRow.append(nom)
			newRow.append(commune)
						
			allRows.append(newRow)

	return allRows;

def writeCsv(outpath, rows):
	outfile = codecs.open(outpath, 'a', 'utf-8-sig')
	for row in rows:
		index = 0
		for item in row:
						
			try:
				item = item.decode('utf-8-sig')
				outfile.write(item)
			except UnicodeEncodeError:
				print item + ' Encode effed it up'
				outfile.write('')
			except UnicodeDecodeError:
				print item + 'Decode effed it up'
				outfile.write('')

			index = index + 1
			if index < len(row):
				outfile.write(',')

		outfile.write('\n')

	outfile.close()

def createSynomapFromCsv(csvPath, badVals):
	
	
	# first row is true val for other bad vals
	with codecs.open(csvPath) as csvfile:
		linereader = csv.reader(csvfile, dialect=csv.excel)
		counter = 0;
		goodVal = ''
		for line in linereader:
			if counter == 0:
				goodVal = line[0].lower().strip();
				counter = counter + 1
			else:
				badVals.append([line[0].lower().strip(),goodVal.lower().strip()])
	return badVals;

def writeValMap(valsArray):
	outFile = open("C:/Users/jderiggi/Documents/AVANSEDb/testout.csv", 'a')
	for vals in valsArray:
		outFile.write(vals[0]  +'\n');

	outFile.close()

def loadSynos(syonymsfolder):
	
	# path = 'C:/Users/jderiggi/Documents/AVANSEDb/communesynonyms'
	
	children = os.listdir(syonymsfolder)
	badVals = []
	
	for child in children:
		if child.endswith(".csv"):
			badVals = createSynomapFromCsv(syonymsfolder + child, badVals)
	
	return badVals;		

# writeValMap(loadSynos('C:/Users/jderiggi/Documents/AVANSEDb/communesynonyms/'))


cleanedList = cleanDistroList();
writeCsv('C:/Users/jderiggi/Documents/AVANSEDb/output/distroout.csv', cleanedList)

# cleanedRows = testRead()
# writeCsv('C:/Users/jderiggi/Documents/AVANSEDb/output/firstOut.csv', cleanedRows)