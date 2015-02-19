# def testRead():
# 	with codecs.open("C:/Users/jderiggi/Documents/AVANSEDb/menage2.csv") as csvfile:

#''' 		linereader = csv.DictReader(csvfile, dialect=csv.excel)

# count bad codes
# fix bad codes
# count by crop
# count by crop and commune
<<<<<<< HEAD

import re

# def badCodeFixer():
	# test for missing me and fix

	# test for missing letter, if missing, check for the culture here : sectionA[1]/culture_cible and add

	# check for NA and try to derive from a unique number

def testMissingME(inword):
	print inword.upper().rfind('ME')

def testMissingCropCode(inword):
	regex = "ME\d+$"
	missingcodepattern = re.compile(regex)
	matchobj = missingcodepattern.match(inword)
	if matchobj != None and matchobj.start() == 0:
		# is missing code so fetch from other part on file


	print 
=======
# TODO find duplicates
# with cin_nif as primary we had 3847 records
# with locationname as primary we had 4106 records
# with cinname as primary 745 duplicates for cin 4060 valid

import re
import codecs, csv


CODE_MENAGE ='code_menage'
CODE_PRODUCER = 'Code_Producteur'
CODE_CULTURE = 'sectionA[1]/culture_cible'
BASSIN_VERSANT = 'Bassin versant'
COMMUNE = 'sectionA[1]/commune'
LATITUDE = '_gps_latitude'
LONGITUDE = '_gps_longitude'
PRODUCER_NAME = 'nom_producteur'
TELEPHONE = 'telephone'
SEX = 'sexe'
CHEF_MENAGE = 'chef_menage'
CIN_NIF = 'cin_nif'


def fixBadCodes(row):
	
	upperAndStrip(row)

	# fix blank or missing code
	fixBlankOrMissingCode(row)

	# test for missing me and fix
	fixMissingME(row)

	# test for missing letter, if missing, check for the culture here : sectionA[1]/culture_cible and add
	fixMissingCropCode(row)

	# check for NA and try to derive from a unique number
	fixMissingProducerCode(row)

def upperAndStrip(row):
	row[CODE_MENAGE] = row[CODE_MENAGE].upper().strip().replace(' ','')

def isNa(code):

	if code != None and code == 'NA' or code == 'N/A':
		return True

	return False

def fixBlankOrMissingCode(row):
	# if the code is NA or blank see if we can get it from code_producer and code culture
	menagecode = row[CODE_MENAGE]
	producercode = row[CODE_PRODUCER].upper().strip().replace(' ','')
	culturecode = row[CODE_CULTURE].upper().strip().replace(' ','')

	if len(menagecode) != 0 and not isNa(menagecode):
		# no need for fixing
		return

	if len(producercode) != 0 and not isNa(producercode):
		menagecode = 'ME' + producercode
		row[CODE_MENAGE] = menagecode




def fixMissingME(row):

	menagecode = row[CODE_MENAGE].upper().strip().replace(' ','')
	if len(menagecode) == 0 or isNa(menagecode):
		return None

	if menagecode.rfind('ME') != 0:
		menagecode = 'ME' + menagecode
		row[CODE_MENAGE] = menagecode
	
	
	return menagecode


def fixMissingCropCode(row):
	
	menagecode = row[CODE_MENAGE]
	culturecode = row[CODE_CULTURE].upper().strip().replace(' ','')
	
	regex = "ME\d*$"
	missingcodepattern = re.compile(regex)
	matchobj = missingcodepattern.match(menagecode)

	if len(culturecode) > 0 and matchobj != None and matchobj.start() == 0:
		# needs fixing and can fix it
		menagecode = 'ME' + culturecode[0].upper() +  menagecode[2:]
		row[CODE_MENAGE] = menagecode

		

	
		

def fixMissingProducerCode(row):
	menagecode = row[CODE_MENAGE]

	regex = "ME[RCBMPH]*$"
	missingcodepattern = re.compile(regex)
	matchobj = missingcodepattern.match(menagecode)
	producercode = row[CODE_PRODUCER].upper().strip().replace(' ','')
	

	if len(producercode) > 1 and not isNa(producercode) and matchobj != None and matchobj.start() == 0:
		# is broken and we can fix it
		row[CODE_MENAGE] = 'ME' + producercode
		

		
>>>>>>> 43c2cd5d2a4525ec65ce140ef8008b2b3b42d627

def testWords(intext):

	regex = "ME[RCBMPH]\d+$"

	p = re.compile(regex)
	goodCodes = []
	badCodes = []

	# counters
	total = 0;
	badcount = 0;
	goodcount = 0;
	
	for inword in intext:
		inword = inword.upper().strip().replace(' ','');
		matchobj = p.match(inword);
		total = total +1

		if matchobj != None:
			# good codes
			print inword
			goodCodes.append(inword)
			goodcount = goodcount + 1;
		else:
			# bad codes
			badCodes.append(inword)
			badcount = badcount + 1

	
	writeList(goodCodes, 'C:/Users/jderiggi/Documents/AVANSEDb/beneficiary_registration/output/goodMenageCodes.csv')
	writeList(badCodes, 'C:/Users/jderiggi/Documents/AVANSEDb/beneficiary_registration/output/badMenageCodes.csv')

	# output
	print 'total:\t' + str(total)
	print 'badcount:\t' + str(badcount)
	print 'goodcount:\t' + str(goodcount)



def writeList(list, fileout):
	out = open(fileout, 'a')
	for item in list:
		out.write(item)
		out.write('\n')

	out.close()

# TODO update this as a 
def readAsList(filepath):
	lines=[]
	with open(filepath) as f:
		lines = f.read().splitlines();
<<<<<<< HEAD

	return lines;

# codes = readAsList('C:/Users/jderiggi/Documents/AVANSEDb/beneficiary_registration/allMenageCodes.csv')
# testWords(codes)

testMissingME('R3455')


=======
	f.close()
	return lines;


def readMenage():
	# entry path
	with codecs.open("C:/Users/jderiggi/Documents/AVANSEDb/beneficiary_registration/enregistrement_beneficiaire.csv") as csvfile:
		linereader = csv.DictReader(csvfile, dialect=csv.excel)
		allrows= []
		for row in linereader:
			fixBadCodes(row)
			allrows.append(row)

		writeRowsAsCSV('C:/Users/jderiggi/Documents/AVANSEDb/beneficiary_registration/output/cleanedMenage3.csv', allrows)
		

def writeRowsAsCSV(outpath, rows):
	outRows = open(outpath, 'a')
	outRows.write(getHeaderLine())
	menagecinhashes = []
	invalidrows = []	
	countinvalid = 0;
	for row in rows:
		
		hasheesh = hasValidHasheesh(row)
		print hasheesh
				
		if hasheesh != None and row[CHEF_MENAGE].strip().upper() == 'OUI' and hasheesh not in menagecinhashes:
			line = makeLineFromRow(row)
			outRows.write(line)
			menagecinhashes.append(hasheesh)

		elif hasheesh == None:
			# TODO write these out
			invalidrows.append(row)
			countinvalid = countinvalid + 1

	print len(menagecinhashes)
	print countinvalid
	writeRows('C:/Users/jderiggi/Documents/AVANSEDb/beneficiary_registration/output/invalidrecords.csv', invalidrows)
	outRows.close()

def writeRows(outpath, rows):
	outRows = open(outpath, 'a')
	outRows.write(getHeaderLine())
	for row in rows:
		outRows.write(makeLineFromRow(row))		
	outRows.close()

def hasValidHasheesh(row):
	
	# if len(row[CODE_MENAGE]) > 3 or len(row[CIN_NIF].strip().replace('-','').replace(' ','')) > 5:
	# 	return True

	if len(row[CIN_NIF].strip().replace('-','').replace(' ','')) > 5 and row[PRODUCER_NAME].strip().replace(' ','').upper() > 5:
		return '_'  + row[CIN_NIF].strip().replace('-','').replace(' ','') + row[PRODUCER_NAME].strip().replace(' ','').upper()

	if len(row[CIN_NIF].strip().replace('-','').replace(' ','')) > 5 :
		return '_'  + row[CIN_NIF].strip().replace('-','').replace(' ','') 	

	if row[LATITUDE].strip() > 4 and row[LONGITUDE].strip() > 4 and row[PRODUCER_NAME].strip().replace(' ','').upper() > 5:
		return row[LATITUDE].strip() + row[LONGITUDE].strip() + row[PRODUCER_NAME].strip().replace(' ','').upper()

	if len(row[TELEPHONE].strip().replace('-','').replace(' ','')) > 5 and row[PRODUCER_NAME].strip().replace(' ','').upper() > 5:
		return '_' + row[TELEPHONE].strip().replace('-','').replace(' ','') + row[PRODUCER_NAME].strip().replace(' ','').upper()

	if len(row[TELEPHONE].strip().replace('-','').replace(' ','')) > 4:
		return row[TELEPHONE].strip().replace('-','').replace(' ','')


	return None

# def makeHasheesh(row):
# 	# hasheesh = row[CODE_MENAGE] + row[CIN_NIF].strip().replace('-','').replace(' ','')
# 	hasheesh =  row[CIN_NIF].strip().replace('-','').replace(' ','')
# 	if len(hasheesh ) < 6:

# 		hasheesh =  row[TELEPHONE].strip().replace('-','').replace(' ','')

# 	return hasheesh

def makeLineFromRow(row):
	line = row[CODE_MENAGE] 
	line = line + ',' + row[CODE_PRODUCER]
	line = line + ',' + row[CODE_CULTURE]
	line = line + ',' + row[BASSIN_VERSANT]
	line = line + ',' + row[COMMUNE]
	line = line + ',' + row[LATITUDE]
	line = line + ',' + row[LONGITUDE]
	line = line + ',' + row[PRODUCER_NAME].strip().replace('-','').replace(' ','')
	line = line + ',' + '_' + row[CIN_NIF].strip().replace('-','').replace(' ','')
	line = line + ',' + row[TELEPHONE]
	line = line + ',' + row[SEX]
	line = line + ',' + row[CHEF_MENAGE] +  '\n'
	
	return line

def getHeaderLine():

	line = CODE_MENAGE 
	line = line + ',' + CODE_PRODUCER
	line = line + ',' + CODE_CULTURE
	line = line + ',' + BASSIN_VERSANT
	line = line + ',' + COMMUNE
	line = line + ',' + LATITUDE
	line = line + ',' + LONGITUDE
	line = line + ',' + PRODUCER_NAME
	line = line + ',' + CIN_NIF
	line = line + ',' + TELEPHONE
	line = line + ',' + SEX
	line = line + ',' + CHEF_MENAGE +  '\n'

	return line


readMenage()

# codes = readAsList('C:/Users/jderiggi/Documents/AVANSEDb/beneficiary_registration/allMenageCodes.csv')
# testWords(codes)

# test code testers with bad codes file:
# badCodes = readAsList('C:/Users/jderiggi/Documents/AVANSEDb/beneficiary_registration/output/badMenageCodes.csv')
# for badCode in badCodes:
# 	isMissingCropCode(badCode)
	
# 	# isMissingProducerCode(badCode)
>>>>>>> 43c2cd5d2a4525ec65ce140ef8008b2b3b42d627
