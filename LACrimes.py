#Cindy Zheng 
import csv
import matplotlib.pyplot as plt


age_group = {"0-18" : 0, "19-30":0, "31-50":0, "50+":0}
crime = {}

#draws a pie chart of the age groups of victims in west la
def showAge():
	age_labels = age_group.keys()
	size = age_group.values()
	plt.pie(size, labels=age_labels, startangle=90, autopct='%.1f%%')
	plt.title("Age groups of victims in West LA")
	plt.show()
	
#draws a bar graph of the different crimes committed in west la 
def showCrimeTypes():
	crime_labels = crime.keys()
	size = crime.values()
	index = range(0,len(crime_labels))
	plt.bar(index, size)
	plt.xlabel('Types of Crimes',fontsize = 5)
	plt.ylabel('Times Crime was committed', fontsize = 5)
	plt.xticks(index, crime_labels, fontsize=5, rotation=30)
	plt.title('Crimes in West LA')
	plt.show()

#sorts victims into age groups	
def sortAge(age):
	if(age <= 18 and age > 0):
		age_group["0-18"] += 1
	elif (age > 18 and age < 31):
		age_group["19-30"] += 1
	elif (age > 30 and age < 51):
		age_group["31-50"] += 1
	else:
		age_group["50+"] += 1

#processes data from the csv file
with open('Crime_Data_from_2010_to_Present.csv') as csvfile:
	readCSV = csv.reader(csvfile, delimiter=',')
	temp = []
	for row in readCSV:
		if(len(row) >= 4 and row[4] == '8' ):
			if(len(row) >= 10 and len(row[10]) > 1):
				sortAge(int(float(row[10])))
			if len(row) >= 8 and row[8] not in crime:
				crime[row[8]] = 1
			elif len(row) >= 8:
				crime[row[8]] += 1
			

plt.subplot(1, 2, 1)
showAge()
plt.subplot(1, 2, 2)
showCrimeTypes()