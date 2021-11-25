# Most Active Cookie 
## Coding Task
Given a cookie log file in the following format: 

cookie,timestamp 
AtY0laUfhglK3lC7,2018-12-09T14:19:00+00:00 
SAZuXPGUrfbcn5UA,2018-12-09T10:13:00+00:00 
5UAVanZf6UtGyKVS,2018-12-09T07:25:00+00:00 
AtY0laUfhglK3lC7,2018-12-09T06:19:00+00:00 
SAZuXPGUrfbcn5UA,2018-12-08T22:03:00+00:00 
4sMM2LxV07bPJzwf,2018-12-08T21:30:00+00:00 
fbcn5UAVanZf6UtG,2018-12-08T09:30:00+00:00 
4sMM2LxV07bPJzwf,2018-12-07T23:30:00+00:00 

Write a command line program in your preferred language to process the log file and return the most active cookie for specified day. The example below shows how we'll execute your program.

### Command:

$ ./most_active_cookie cookie_log.csv -d 2018-12-09

### Output:

AtY0laUfhglK3lC7

We define the most active cookie as one seen in the log the most times during a given day. 

### Assumptions: 
- If multiple cookies meet that criteria, please return all of them on separate lines. 

$ ./most_active_cookie cookie_log.csv -d 2018-12-09

SAZuXPGUrfbcn5UA

4sMM2LxV07bPJzwf

fbcn5UAVanZf6UtG

- You're only allowed to use additional libraries for testing, logging and cli-parsing. There are libraries for
most languages which make this too easy (e.g pandas) and we’d like you to show off you coding skills.
- You can assume -d parameter takes date in UTC time zone.
- You have enough memory to store the contents of the whole file.
- Cookies in the log file are sorted by timestamp (most recent occurrence is first line of the file).

## Instructions
- Have Python 3.8.2 installed and updated
- Run the command in the following format:

./most_active_cookie [CSV FILE] -d [DATE]

ex. ./most_active_cookie cookie_log.csv -d 2018-12-09

#### [CSVFILE]
Any .csv file that exist within the directory

ex. cookie_log.csv

#### [DATE]
Any date that is in the format of yyyy-mm-dd

ex. 2021-11-23

## Files
- `most_active_cookie` - the main file that uses the functions in util.py to create the functionality of this task
- `util.py` - contains the small functions necessary for most_active_cookie (ex. parsing the command line, keeping count of cookie occurences of specific date in dictionary form, determining most active cookie on a specific date)
- `test.py` - testing script for the functions in util.py
- `cookie_log.csv` - a sample csv file applicable for most_active_cookie
