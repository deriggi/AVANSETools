# def testRead():
# 	with codecs.open("C:/Users/jderiggi/Documents/AVANSEDb/menage2.csv") as csvfile:

#''' 		linereader = csv.DictReader(csvfile, dialect=csv.excel)

# count bad codes
# fix bad codes
# count by crop
# count by crop and commune

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

	return lines;

# codes = readAsList('C:/Users/jderiggi/Documents/AVANSEDb/beneficiary_registration/allMenageCodes.csv')
# testWords(codes)

testMissingME('R3455')


