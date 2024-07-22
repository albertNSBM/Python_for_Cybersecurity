# loading the file first 

log_path=input('Enter the log path for analyis')

with open(log_path,'r') as log:
	data = log.readlines()
	
