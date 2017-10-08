



def get_line():
    with open("/Users/Dhanush/Desktop/StackOVerflowData/Users.xml") as file:
        for i in file:
            yield i

lines_required = 5
gen = get_line()
chunk = [next(gen) for i in range(lines_required)]

print chunk


SELECT * from Posts where ("body" LIKE '%energy consum%' OR
						   "body" LIKE '%energy efficien%' OR "body" LIKE '%energy sav%' OR
						   "body" LIKE '%energy sav%' OR






	);