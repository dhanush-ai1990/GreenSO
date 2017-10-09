#This program will be used to play with the database for Green posts in StackOverFlow

import sqlite3
import json, sys, os, xmltodict, csv
from os.path import join
from utils import *
import shutil
from sklearn import *
import pickle
from sklearn.externals import joblib

data_path ='/Users/Dhanush/Desktop/Projects/GreenSO/Data/'
Database = sqlite3.connect('/Users/Dhanush/Desktop/Projects/GreenSO/Data/energy.db')
c = Database.cursor()
SQL = "select postid from `posts`"
c.execute(SQL)


Green_PostID_Query_results =[]
Green_PostID_Tags_results =[]
for row in c:
	Green_PostID_Query_results.append(row[0])


c.close()

d =Database.cursor()

SQL = "select field1 from `posts_with_tags`"
d.execute(SQL)
for row1 in d:
	Green_PostID_Tags_results.append(row[0])


print ("Total Posts from String Match")
print (len(Green_PostID_Query_results))
print ("Total Posts from Tag Match")
print (len(Green_PostID_Tags_results))

combined = Green_PostID_Tags_results + Green_PostID_Query_results

print ("Total Posts from combined")
print (len(combined))

unique = list(set(combined))
print ("Unique Green Posts")
print (len(unique))

for i in Green_PostID_Tags_results:
	if i not in Green_PostID_Query_results:
		print (" Not Tagged")

Android_Posts= joblib.load(data_path+'Android_posts.pkl')
Ios_posts= joblib.load(data_path+'Ios_posts.pkl')

print("Number of Android Posts")
print (len(Android_Posts))
print("Number of IOS Posts")
print (len(Ios_posts))

unique = set(unique)

Android_Posts = [int(i) for i in Android_Posts]
Ios_posts = [int(i) for i in Ios_posts]
#Now Lets find the Android Green Posts
Android_Posts = set(Android_Posts)
Android_green_posts = list(Android_Posts & unique)

#Now Lets find the IOS Green Posts
Ios_posts = set(Ios_posts)
Ios_green_posts = list(Ios_posts & unique)

print ("Number of Android Green Posts")
print (len(Android_green_posts))
print ("Number of Ios Green Posts")
print (len(Ios_green_posts))
d.close()
Database.close()
#Construct Query String
#ALl Green Posts
"""
string = ""
for i in combined:
	string= string + "Id = " + str(i) + " OR "
"""
#For Android Green
"""
string = ""
for i in Android_green_posts:
	string= string + "Id = " + str(i) + " OR "
print (string)
"""


#For Ios Green

"""
string = ""
for i in Ios_green_posts:
	string= string + "Id = " + str(i) + " OR "
print (string)


"""



#Read the Green Database

Database = sqlite3.connect('/Users/Dhanush/Desktop/Projects/GreenSO/Data/GreenDatabase.db')

#Get all Green Android Qns PostId to fetch answers

c = Database.cursor()
SQL = "select Id from `GreenPostsQuestions`"
c.execute(SQL)

AndroidGreen =[]
for row in c:
	AndroidGreen.append(row[0])

#print (AndroidGreen)
print (len(AndroidGreen))
c.close()



string = ""
for i in AndroidGreen:
	string= string + "ParentId = " + str(i) + " OR "
print (string)
"""

#Get all Ios Green question id to get answers

c = Database.cursor()
SQL = "select Id from `IOSGreen`"
c.execute(SQL)

IOSGreen =[]
for row in c:
	IOSGreen.append(row[0])

#print (IOSGreen)
#print (len(IOSGreen))

string = ""
for i in IOSGreen:
	string= string + "ParentId = " + str(i) + " OR "
print (string)

"""






