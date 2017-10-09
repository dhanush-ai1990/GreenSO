import json, sys, os, xmltodict, csv
from os.path import join
from utils import *
import shutil
from sklearn import *
import pickle
from sklearn.externals import joblib
file_Name1 = "Android_postid"
fileObject1 = open(file_Name1,'wb')
file_Name2 = "Ios_postid"
fileObject2 = open(file_Name2,'wb')
a= joblib.load('Android_posts.pkl')
b = joblib.load('Ios_posts.pkl')


print (a[1:25])


print (len(a))
print (len(b))

combined = a
combined.extend(b)
print (len(set(combined)))
