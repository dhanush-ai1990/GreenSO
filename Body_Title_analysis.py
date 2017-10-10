import sqlite3
import json, sys, os, xmltodict, csv
from os.path import join
from utils import *
import shutil
from sklearn import *
import pickle
from sklearn.externals import joblib
from collections import Counter
from bs4 import BeautifulSoup

Database = sqlite3.connect('/Users/Dhanush/Desktop/Projects/GreenSO/Data/GreenDatabase.db')
c = Database.cursor()
SQL = "select Body, Title from `AndroidGreenQuestions`"
c.execute(SQL)
d = Database.cursor()
SQL = "select Body from `AndroidGreenAnswers`"
d.execute(SQL)
list_title=[]
list_body=[]
code_body=[]
for row in c:
	soup = BeautifulSoup(row[0], 'html.parser')
	out = soup.findAll('p')
	temp =[]
	for text in out:
		temp.append(text.getText())
	string = " ".join(temp)

	list_body.append(string)
	list_title.append(row[1])
for row in d:
	soup = BeautifulSoup(row[0], 'html.parser')

	out = soup.findAll('p')
	code = soup.findAll('code')
	temp =[]
	temp1 =[]
	for text in out:
		temp.append(text.getText())
	string = " ".join(temp)
	list_body.append(string)
	for codes in code:
		temp1.append(text.getText())
	print (temp1)
	



bag_of_words =[]
first_word =[]
for Title in list_title:
	temp_list =Title.lower().split(' ')
	first_word.append(temp_list[0])

data =[element.lower() for element in first_word]
counter = Counter(data)
counter_selected = 	counter.most_common(200)
"""
for i in counter_selected:
	print(i[0],i[1])
"""

"""
for qns in list_body:
	print ("---------------------------")
	print (qns)
	
"""