import sqlite3
import json, sys, os, xmltodict, csv
from os.path import join
from utils import *
import shutil
from sklearn import *
import pickle
from sklearn.externals import joblib


total_acceptedans = 0
total_score =0
neg_score = 0
total_views =0
no_views =0
answer_count =0
no_answer =0
comment_count=0
no_comment =0
favorite_count=0
no_fav=0
count=0
year_counter ={}
for i in range(2008,2018):
	year_counter[i] =0


"""
file1 = open('/Users/Dhanush/Downloads/Text/SOIOSANS.txt', 'r') 
print (year_counter)
#(postid) +","+str(date)+","+str(score)+","+str(viewcount)+","+str(answercount)+","+str(favoritecount)
for line in file1:
	line=line.strip()
	row = line.split(',')
	count+=1
	postid=row[0]
	#print (postid)
	#idtype=row[1]
	#print (idtype)

	#print (parentid)
	creationdate =row[1][0:4]
	year_counter[int(creationdate)] +=1
	#print (creationdate)
	score = row[2]
	if (score):
		total_score+=int(score)
		if (int(score) <0):
			neg_score+=1
	#print (score)
	view = row[3]
	if (view):
		total_views+=int(view)
		if (int(view) < 1):
			no_views+=1

	#print (view)
	answercount = row[4]
	if (answercount):
		answer_count+=int(answercount)
		if (int(answercount) <1):
			no_answer+=1

	favoritecount = row[5]
	if (favoritecount):
		favorite_count+=int(favoritecount)
		if (int(favoritecount) <1):
			no_fav+=1
	#print (favoritecount)


print ("Statistics for IOS Answers")
print ("Number of records: " + str(count))
print("Average Score for Posts: " + str(total_score/count))
print("Posts with negative scores: " + str(neg_score) +" Percentage: " +str(neg_score/count) )
print("Average Views for Posts: " + str(total_views/count))
print("Posts with no views: " + str(no_views) +" Percentage: " +str(no_views/count) )
print("Average Answer count for Posts: " + str(answer_count/count))
print("Posts with no answers: " + str(no_answer) +" Percentage: " +str(no_answer/count) )

print("Average Posts marked as favourite: " + str(favorite_count/count))
print("Posts never marked as favourites: " + str(no_fav) +" Percentage: " +str(no_fav/count) )
temp1=[]
temp2=[]
for item in year_counter:
	temp1.append(item)
	temp2.append(year_counter[item])

print("Yearly statistics")
print(temp1)
print(temp2)
"""
file1 = open('/Users/Dhanush/Downloads/Text/SOQNS.txt', 'r') 
file2 = open('/Users/Dhanush/Downloads/Text/SOANS.txt', 'r') 
from datetime import date
from datetime import datetime
def get_diff_of_dates(d1,d2):
	date_format = "%Y%m%d"
	a = datetime.strptime(str(d1), date_format)
	b = datetime.strptime(str(d2), date_format)

	delta = a-b
	return delta.days


answers_dict ={}

count =0
for line in file2:
	count+=1
	line=line.strip()
	row=line.split(',')
	date= int(row[1][0:10].replace('-',""))
	if (int(row[0]))  not in answers_dict:
		answers_dict[int(row[0])] = []
		answers_dict[int(row[0])].append(date)
	else:
		answers_dict[int(row[0])].append(date)

print ("Ans: " +str(count))

Questions_dict ={}
count =0
for line in file1:
	count+=1
	line=line.strip()
	row=line.split(',')
	date= int(row[1][0:10].replace('-',""))
	Questions_dict[int(row[0])] = date

print ("Qns: " +str(count))

count =0
a=0
total_days=0
for item in Questions_dict:
	if item in answers_dict:
		diff = get_diff_of_dates((min(answers_dict[item])),Questions_dict[item])
		print (diff)
		#print (diff,min(answers_dict[item]),Questions_dict[item])
		total_days+=diff
		count+=1
	else:
		a+=1
		continue


print ("No Ans: " +str(a))



print ("Median number of days to answer: " + str(total_days/count))	
