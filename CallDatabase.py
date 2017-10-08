#This program will be used to play with the database for Green posts in StackOverFlow

import sqlite3
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


print "Total Posts from String Match"
print len(Green_PostID_Query_results)
print "Total Posts from Tag Match"
print len(Green_PostID_Tags_results)

combined = Green_PostID_Tags_results + Green_PostID_Query_results

print "Total Posts from combined"
print len(combined)

unique = list(set(combined))
print "Unique Green Posts"
print len(unique)

for i in Green_PostID_Tags_results:
	if i not in Green_PostID_Query_results:
		print " Not Tagged"


