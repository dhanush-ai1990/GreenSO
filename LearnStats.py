import sqlite3
import json, sys, os, xmltodict, csv
from os.path import join
from utils import *
import shutil
from sklearn import *
import pickle
from sklearn.externals import joblib

"""
Database = sqlite3.connect('/Users/Dhanush/Desktop/Projects/GreenSO/Data/GreenDatabase.db')
c = Database.cursor()
SQL = "select * from `IOSGreenAnswers`"
c.execute(SQL)

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
print (year_counter)
for row in c:
	count+=1
	postid=row[0]
	#print (postid)
	idtype=row[1]
	#print (idtype)
	acceptedans = row[2]
	if (acceptedans):
		total_acceptedans+=1
	#print (acceptedans)
	parentid=row[3]
	#print (parentid)
	creationdate =row[4][0:4]
	year_counter[int(creationdate)] +=1
	#print (creationdate)
	score = row[6]
	if (score):
		total_score+=int(score)
		if (int(score) <0):
			neg_score+=1
	#print (score)
	view = row[7]
	if (view):
		total_views+=int(view)
		if (int(view) < 1):
			no_views+=1

	#print (view)
	answercount = row[17]
	if (answercount):
		answer_count+=int(answercount)
		if (int(answercount) <1):
			no_answer+=1
	#print (answercount)
	commentcount = row[18]
	if (commentcount):
		comment_count+=int(commentcount)
		if (int(commentcount) <1):
			no_comment+=1
	#print (commentcount)
	favoritecount = row[19]
	if (favoritecount):
		favorite_count+=int(favoritecount)
		if (int(favoritecount) <1):
			no_fav+=1
	#print (favoritecount)


print ("Statistics for IOS Green Answers")
print ("Number of records: " + str(count))
print("Total Posts with Accepted Answers: " + str(total_acceptedans) +" out of: " + str(count) +" Percentage: " +str(total_acceptedans/count))
print("Average Score for Posts: " + str(total_score/count))
print("Posts with negative scores: " + str(neg_score) +" Percentage: " +str(neg_score/count) )
print("Average Views for Posts: " + str(total_views/count))
print("Posts with no views: " + str(no_views) +" Percentage: " +str(no_views/count) )
print("Average Answer count for Posts: " + str(answer_count/count))
print("Posts with no answers: " + str(no_answer) +" Percentage: " +str(no_answer/count) )
print("Average Comment count for Posts: " + str(comment_count/count))
print("Posts with no comments: " + str(no_comment) +" Percentage: " +str(no_comment/count) )
print("Average Posts marked as favorite: " + str(favorite_count/count))
print("Posts never marked as favorites: " + str(no_fav) +" Percentage: " +str(no_fav/count) )
temp1=[]
temp2=[]
for item in year_counter:
	temp1.append(item)
	temp2.append(year_counter[item])

print("Yearly statistics")
print(temp1)
print(temp2)
"""


#We need code for Avg Answer time
#Lets do for All Green Posts
from datetime import date
from datetime import datetime
def get_diff_of_dates(d1,d2):
	date_format = "%Y%m%d"
	a = datetime.strptime(str(d1), date_format)
	b = datetime.strptime(str(d2), date_format)

	delta = a-b
	return delta.days

Database = sqlite3.connect('/Users/Dhanush/Desktop/Projects/GreenSO/Data/GreenDatabase.db')
c = Database.cursor()
SQL = "select Parentid,CreationDate from `GreenPostsAnswers`"
c.execute(SQL)

answers_dict ={}
count =0
l1 =[]
for row in c:
	count+=1
	date= int(row[1][0:10].replace('-',""))
	if (int(row[0]))  not in answers_dict:
		answers_dict[int(row[0])] = []
		answers_dict[int(row[0])].append(date)
	else:
		answers_dict[int(row[0])].append(date)
	l1.append(int(row[0]))

c.close()

c = Database.cursor()
SQL = "select Parentid,CreationDate from `GreenPostsAnswers1`"
c.execute(SQL)

for row in c:
	count+=1
	date= int(row[1][0:10].replace('-',""))
	if (int(row[0]))  not in answers_dict:
		answers_dict[int(row[0])] = []
		answers_dict[int(row[0])].append(date)
	else:
		answers_dict[int(row[0])].append(date)
	l1.append(int(row[0]))

c.close()



d =Database.cursor()
SQL = "select Id,CreationDate from `GreenPostsQuestions`"
d.execute(SQL)
Questions_dict ={}
count =0
l2=[]
for row in d:
	count+=1
	date= int(row[1][0:10].replace('-',""))
	Questions_dict[int(row[0])] = date
	l2.append(int(row[0]))

d.close()

total_days =0
count =0
for item in Questions_dict:
	if item in answers_dict:
		count+=1
		diff = get_diff_of_dates((min(answers_dict[item])),Questions_dict[item])
		#print (diff,min(answers_dict[item]),Questions_dict[item])
		total_days+=diff
	else:
		print (item)


print (len(list(set(l1)&set(l2))))
print (count)
print ("Median number of days to answer: " + str(total_days/count))	









