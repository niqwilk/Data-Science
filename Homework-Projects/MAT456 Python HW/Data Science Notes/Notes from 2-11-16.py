

    #class example - which letter is most common for first names?
    #we already have a list of first names
firstNames = ['Matt','Ed','Jay','Yolo','Meg']
    counts = {}
    for n in firstNames:
        counts[n[0]] = counts.get(n[0],0)+1
    print counts 

    #grouping temperatures together by highs
temps = [12,4,56,75,234,6,6,43,12,12,12,74,23,654,2]
tempCount = {}
for temp in temps:
    tempCount[temp] = tempCount.get(temp,0)+1
print tempCount 


""" Roll 10 times and add the sum (expectation work) """
