#Homework 3 Nicholas Wilk

import csv
import numpy as np
import matplotlib.pyplot as plt


def main():
      with open('NYPD_Motor_Vehicle_Collisions.csv', 'rb') as f:
        reader = csv.DictReader(f)
        time = [row['TIME'] for row in reader]
        hourCount = {}
        

        for timeString in time:
            c = timeString.find(":")
            hour = int(timeString[:c])
            hourCount[hour] = hourCount.get(hour,0)+1

        mean = float(sum(hourCount.values()))/24
        print "The mean number of accidents per hour is : ",mean

        variance = 0
        for i in hourCount:
            
            variance += float((hourCount.get(i) - mean )) ** 2 
           
        truevariance = (variance) / float(len(hourCount)-1)
        print "The Variance is : ", truevariance
        
    
main()
