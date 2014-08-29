import csv
import codecs


def incrementCountByOccurrence(counterdict, rowdict, columname):
	# add to the dictionary so that each cin_nif holds the number of occurences of that cin_nif value
	keyToCount = rowdict[columname]
	if keyToCount not in counterdict:
		counterdict[keyToCount] = 0

	counterdict[keyToCount] = counterdict[keyToCount] + 1 

def addOccurrencesToList(collectormap, rowdict, keyname, keytoadd):
	# add to the dictionary so that each cin_nif has a list of fullnames

	if rowdict[keyname] not in collectormap:
		collectormap[rowdict[keyname]] = []

	if rowdict[keytoadd] not in collectormap[rowdict[keyname]]:
		# print collectormap[rowdict[keyname]] + ' is getting ' + rowdict[keytoadd]
		collectormap[rowdict[keyname]].append(rowdict[keytoadd])

def findDuplicates(infile, columnname, counterdict):
	# load the csv file into a collection of dictionaries

	with codecs.open(infile) as sibacsv:
		dictreader = csv.DictReader(sibacsv, dialect=csv.excel)
		for sibadict in dictreader:
			incrementCountByOccurrence(counterdict, sibadict, columnname)
			

def collectOccurrences(infile, columnname, collectormap, keytoadd):
	# load the csv file into a collection of dictionaries

	with codecs.open(infile) as sibacsv:
		dictreader = csv.DictReader(sibacsv, dialect=csv.excel)
		for sibadict in dictreader:
			addOccurrencesToList(collectormap,sibadict, columnname, keytoadd)

def writeReport(outfile, line, outtype):
	outhandle = open(outfile, outtype)
	outhandle.write(line + '\n')
	outhandle.close()

def examineCount(counterdict, outfile):
	writeReport(outfile,"cin_nif,fois", 'w')		
	for key in counterdict:
		if counterdict[key] > 1:
			line = "{0},{1}".format(key, counterdict[key])
			writeReport(outfile,line, 'a')

def examineCollections(collectormap, outfile):
	writeReport(outfile,"cin_nif,nom et prenom", 'w')		
	for key in collectormap:
		if len(collectormap[key]) > 1:		
			for item in collectormap[key]:
				line =  "{0},{1}".format(key, item)
				writeReport(outfile,line, 'a')

def runThings():
	counterdict = {}
	fullnamemap = {}
	ricesiba = "C:/Users/jderiggi/Documents/Haiti/SIBAAnalysis/csv/riz_siba_1_23_14.csv"
	cocoasiba = "C:/Users/jderiggi/Documents/Haiti/SIBAAnalysis/csv/cocao_siba_1-23-14.csv"
	bananasiba = "C:/Users/jderiggi/Documents/Haiti/SIBAAnalysis/csv/banana_siba_1_23_14.csv"

	findDuplicates(ricesiba, 'cin_nif', counterdict);
	findDuplicates(cocoasiba, 'cin_nif', counterdict)
	findDuplicates(bananasiba, 'cin_nif', counterdict)
	examineCount(counterdict, "C:/Users/jderiggi/Documents/Haiti/SIBAAnalysis/csv/ids_report.csv")
	
	collectOccurrences(ricesiba, 'cin_nif', fullnamemap, 'fullname')
	collectOccurrences(cocoasiba, 'cin_nif', fullnamemap, 'fullname')
	collectOccurrences(bananasiba, 'cin_nif', fullnamemap, 'fullname')
	examineCollections(fullnamemap, "C:/Users/jderiggi/Documents/Haiti/SIBAAnalysis/csv/names_report.csv");

runThings()