import os
import re

#specify path of directory
path = os.getcwd()

#Regex
pattern1 = re.compile(r"[7,8,9]\d{9}\D")
pattern2 = re.compile(r"\+91[7,8,9]\d{9}\D")
pattern3 = re.compile(r"\0[7,8,9]\d{9}\D")

result = []
txtFiles = []
file = []
ans = []

#get List of textFiles recursively 
for root, dirs, files in os.walk(path):
    for filename in files:
    	if filename.endswith('.txt'):
    		txtFiles.append(os.path.join(root,filename))	

#open Files for parsing data
for txtFile in txtFiles:
	with open(txtFile,'r') as f:
		file = f.readlines()
	if file:
		for line in file:
			ans.append(pattern1.findall(line))
			ans.append(pattern2.findall(line))
			ans.append(pattern3.findall(line))


#retrieve phone numbers
for value in ans:
	if value:
		for val in value:
			result.append(val[:-1])

print result