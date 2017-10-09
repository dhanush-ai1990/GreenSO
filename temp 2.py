import json, sys, os, xmltodict, csv
from os.path import join
from utils import *
import shutil
from sklearn.externals import joblib
Android_list =['android','android-studio','android-layout','android-fragments','android-intent']
ios_list = ['iphone','ios','cocos2d-iphone','ios7','ios5','xamarin.ios','ios4']
Android_posts =[]
Ios_posts =[]
flag = 0
for i, line in enumerate(open("/Users/MSR/Desktop/stackoverflow-neo4j/extracted/Posts.xml")):
    line = line.strip()
    if line.startswith("<row"):
        el = xmltodict.parse(line)['row']
        el = replace_keys(el)
        if el.get('tags'):
            eltags = [x.replace('<','') for x in el.get('tags').split('>')]
            for tag in [x for x in eltags if x]:
                if tag.lower() in Android_list:
                    Android_posts.append(el['id'])

                if tag.lower() in ios_list:
                    Ios_posts.append(el['id'])

    if (i%100000 ==0):
        print (i)
joblib.dump(Android_posts, 'Android_posts.pkl')
joblib.dump(Ios_posts, 'Ios_posts.pkl')
print(i,'posts ok')
