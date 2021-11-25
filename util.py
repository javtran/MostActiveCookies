import csv, sys

'''
Parse the command line. Checks if the command contains valid arguments.
Returns file name of the csv file and the date to search for most active cookie
'''
def parseCommandLine(argv):
	if len(argv) < 4 or argv[2] != '-d':
		print("ERROR:  Please put in the correct filepath arguments, as shown below.")
		print("\t./most_active_cookie [csv file] -d [date]")
		sys.exit()
	
	filename = argv[1]
	
	date = argv[3]
	
	# check valid date
	if not checkValidDate(date):
		print("ERROR: time date doesn't match format yyyy-mm-dd")
		sys.exit()
	
	return filename, date
	
'''
Check if a given date is in the valid format yyyy-mm-dd. 
Returns 1 if the date is in the correct format. Returns 0 if the date is in the wrong format.
'''
def checkValidDate(date):
	try:
		year, month, day = date.split("-")
		if not year.isnumeric() or not month.isnumeric() or not day.isnumeric():
			return 0
		if len(year) != 4 or len(month) != 2 or len(day) != 2:
			return 0
		return 1
	except ValueError:
		return 0

'''
Parses through the csv file and append each data to the dictionary, mapping date to another dictionary that maps of cookies to its count.
Returns a the dictionary
'''
def parseCSV(filename):
	dictCookieByDate = dict()
	
	try:
		fileopen = open(filename,'r')
		reader = csv.reader(fileopen)
		
		linecounter = 0
		
		for line in reader:
			if linecounter == 0 or len(line) == 0:
				linecounter += 1
				continue
			linecounter += 1
			
			try: 
				cookie = line[0]
				timestamp = line[1]
				date, time = timestamp.split("T")
				
				if not checkValidDate(date):
					raise IndexError
				
				dictCookieByDate = appendDict(cookie, date, dictCookieByDate)
			except IndexError:
				print("Skipping line {}: in wrong format.".format(linecounter))
				
			
	except FileNotFoundError:
		print("ERROR: File not found.")
		sys.exit()
		
	return dictCookieByDate
	
'''
Appends parsed data to dictionary. The dictionary maps dates to another dictionary
which keeps track of the number of occurrences of a cookie of that date.
Returns updated dictionary.
'''
def appendDict(cookie, date, dic):
	if date in dic:
		if cookie in dic[date]:
			dic[date][cookie] += 1
		else:
			dic[date][cookie] = 1
		
	else:
		dic[date] = {cookie: 1} 
	return dic
	
'''
Prints out the dictionary for testing
'''
def printDict(dic):
	for date in dic:
		print("date: " + date)
		for cookie in dic[date]:
			print("\t{} : {}".format(cookie, dic[date][cookie]))
	return

'''
Gets the most active cookie(s) on a given date. Finds the highest occurence count of a given date.
Prints out any cookie that has the max occurence count.
If date is not found in the dictionary, no cookies are active on that date.
'''
def mostActiveCookie(dic, date):
	if date in dic:
		max_cnt = max(dic[date].values())
		for cookie, cnt in dic[date].items():
			if cnt == max_cnt:
				print(cookie)
	else:
		print("No cookies active on {}".format(date))
		
	return
	
