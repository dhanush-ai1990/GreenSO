import sqlite3
import json, sys, os, xmltodict, csv
from os.path import join
from utils import *
import shutil
from sklearn import *
import pickle
from sklearn.externals import joblib
from collections import Counter


Database = sqlite3.connect('/Users/Dhanush/Desktop/Projects/GreenSO/Data/GreenDatabase.db')
c = Database.cursor()
SQL = "select Body, Title from `AndroidGreenQuestions`"
c.execute(SQL)
d = Database.cursor()
SQL = "select 'Body' `AndroidGreenAnswers`"
d.execute(SQL)
list_title=[]
list_body=[]
for row in c:
	list_body.append(row[0])
	list_title.append(row[1])
for row in d:
	list_body.append(row[0])

"""
bag_of_words =[]
first_word =[]
for Title in list_title:
	temp_list =Title.lower().split(' ')
	first_word.append(temp_list[0])

data =[element.lower() for element in first_word]
counter = Counter(data)
counter_selected = 	counter.most_common(200)
for i in counter_selected:
	print(i[0],i[1])

"""

for qns in list_body:
	print ("---------------------------")
	print (qns)
